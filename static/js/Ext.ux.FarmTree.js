Ext.ux.FarmTree = Ext.extend(Ext.tree.TreePanel, {
    title: 'Фармэфект',
    frame: true,
    border: false,
    region: 'west',
    rootVisible: false,
    lines: false,
    dataUrl: URLS.farm_tree,
    width: '20%',
	id: 'farm-tree',
    root: {
        nodeType: 'async',
        text: 'root',
        id: 'root',
        expanded: true
	},
	listeners: {
        'checkchange': function(node, checked){
            if(checked){
                node.getUI().addClass('selected');
            }else{
                node.getUI().removeClass('selected');
            }
        },
		'click': function(node){
			var search_panel = Ext.getCmp('search-panel');
			search_panel.search(node.attributes.pk);
		}
	}
});

Ext.reg('ext:ux:farm-tree', Ext.ux.FarmTree);