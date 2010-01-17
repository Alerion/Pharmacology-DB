Ext.ux.CategoryTree = Ext.extend(Ext.tree.TreePanel, {
    title: 'Farmaction',
    frame: true,
    border: false,
    region: 'east',
    rootVisible: false,
    lines: false,
    dataUrl: URLS.farmaction_tree,
    width: '20%',
    root: {
        nodeType: 'async',
        text: 'root',
        id: 'root',
        expanded: true
	},
	listeners: {
		click: function(node){
			document.location = node.attributes.url;
		}
	}
});

Ext.reg('ext:ux:category-tree', Ext.ux.CategoryTree);