Ext.ux.IllnessTree = Ext.extend(Ext.tree.TreePanel, {
    title: 'Illness',
    frame: true,
    border: false,
    region: 'west',
    rootVisible: false,
    lines: false,
    dataUrl: URLS.illness_tree,
    width: '20%',
	id: 'illness-tree',
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
        }
	}
});

Ext.reg('ext:ux:illness-tree', Ext.ux.IllnessTree);