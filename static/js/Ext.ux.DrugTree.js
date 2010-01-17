Ext.ux.DrugTree = Ext.extend(Ext.tree.TreePanel, {
    title: 'Drugs',
    frame: true,
    border: false,
    region: 'west',
    rootVisible: false,
    lines: false,
    dataUrl: URLS.drugs_tree,
    width: '20%',
    root: {
        nodeType: 'async',
        text: 'root',
        id: 'root',
        expanded: true
	},
	listeners: {
		click: function(node){
			if (node.leaf) {
				var panel = this.getInfoPanel();//Ext.getCmp('drug-info-panel');
				panel.load({
					url: panel.url,
					params: {
						'pk': node.attributes.pk
					}
				});
				var store = this.getDrugStore();
				store.current_drug = node.attributes.pk;
				store.load({
					params: {
						'pk': node.attributes.pk
					}
				});
			}
		}
	},
	getInfoPanel: function(){
		var _panel;
		return function(){
			return _panel || (_panel = Ext.getCmp('drug-info-panel')) || _panel;
		}
	}(),//getInfoPanel
	getDrugStore: function(){
		var _store;
		return function(){
			return _store || (_store = Ext.getCmp('drug-edit-grid').getStore()) || _store;
		}
	}(),//getDrugStore
});

Ext.reg('ext:ux:drug-tree', Ext.ux.DrugTree);