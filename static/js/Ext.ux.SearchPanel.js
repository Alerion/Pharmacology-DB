Ext.ux.SearchPanel = Ext.extend(Ext.grid.GridPanel, {
	title: 'Поиск',
	region: 'center',
    frame: true,
    border: false,
	layout: 'fit',
    enableColumnHide: false,
    enableColumnMove: false,
    enableHdMenu: false,
	id: 'search-panel',	
	store: new Ext.data.JsonStore({
		autoDestroy: true,
		url: URLS.search,
		fields: ['pk', 'name', 'value'],
		idProperty: 'pk',
		root: 'items',
	}),
	cm: new Ext.grid.ColumnModel({
    	columns: [
            {header: 'Название', dataIndex: 'name'},
            {header: 'Коэфициент', dataIndex: 'value'},
		]
    }),
    initComponent: function(){
		this.searchParam = {
			strong: false,
			type: ''
		};
		var default_type;
		Ext.each(CRITERIONS, function(item){
			item.checkHandler = this.selectMatrixHandler;
			item.scope = this;
			if (item.checked){
				this.searchParam.type = item.pk;
				default_type = item;
			};
		}, this);
        this.tbar = [
            {
				text: 'Строгий',
				enableToggle: true,
		        toggleHandler: function(item, selected){
					this.searchParam.strong = selected;
				},
		        pressed: this.searchParam.strong,
				scope: this
			},'-',{
                text: default_type.text,
                menu: { 
                    items: CRITERIONS
                },
				tooltip: default_type.info
            },'-',{
				text: 'Расчеты',
				handler: this.codeHandler,
				scope: this
			}
        ];
        Ext.ux.SearchPanel.superclass.initComponent.call(this);
		this.farmTree = Ext.getCmp('farm-tree');
    },//initComponent
	search: function(farm_pk){
		this.farm_pk = farm_pk;
		var illness = [];
		Ext.each(Ext.getCmp('illness-tree').getChecked(), function(node){
			this.push(node.attributes.pk);
		}, illness);
		this.getStore().load({
			params: {
				type: this.searchParam.type,
				strong: this.searchParam.strong && 'checked' || '',
				farm: farm_pk,
				illness: illness
			}
		});		
	},
	codeHandler: function(){
		var illness = [];
		Ext.each(Ext.getCmp('illness-tree').getChecked(), function(node){
			this.push(node.attributes.pk);
		}, illness);		
		var param = {
			farm: this.farm_pk,
			type: this.searchParam.type,
			strong: this.searchParam.strong && 'checked' || '',
			illness: illness
		}
		window.open(URLS.code+'?'+Ext.urlEncode(param), '_blank');
	},
	searchSuccess: function(response){
		var result = Ext.util.JSON.decode(response.responseText);
		console.log(result);
	},
	selectMatrixHandler: function(item, checked){
		if (checked){
			this.searchParam.type = item.pk;
			var menu = this.getTopToolbar().get(2);
			menu.setText(item.text);
			menu.setTooltip(item.info);
			Ext.each(item.illness, function(pk){
				this.getNodeById('ill_'+pk).getUI().toggleCheck(true);
			}, Ext.getCmp('illness-tree'));
		}
	}	
});

Ext.reg('ext:ux:search-panel', Ext.ux.SearchPanel);