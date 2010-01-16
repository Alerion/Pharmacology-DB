Ext.ux.SearchPanel = Ext.extend(Ext.grid.GridPanel, {
	title: 'Search',
	region: 'center',
    frame: true,
    border: false,
	layout: 'fit',
    enableColumnHide: false,
    enableColumnMove: false,
    enableHdMenu: false,	
	store: new Ext.data.JsonStore({
		autoDestroy: true,
		url: URLS.search,
		fields: ['pk', 'name', 'value'],
		idProperty: 'pk',
		root: 'items',
	}),
	cm: new Ext.grid.ColumnModel({
    	columns: [
            {header: 'Name', dataIndex: 'name'},
            {header: 'Value', dataIndex: 'value'},
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
				text: 'Search',
				handler: this.searchHandler,
				scope: this
			}
        ];
        Ext.ux.SearchPanel.superclass.initComponent.call(this);
		this.illnessTree = Ext.getCmp('illness-tree');
    },//initComponent
	searchHandler: function(){
		var illnesses = [];
		Ext.each(this.illnessTree.getChecked(), function(item){
			this.push(item.attributes.pk);
		}, illnesses);
		this.getStore().load({
			params: {
				type: this.searchParam.type,
				strong: this.searchParam.strong && 'checked' || '',
				illnesses: illnesses
			}
		});
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
		}
	}	
});

Ext.reg('ext:ux:search-panel', Ext.ux.SearchPanel);