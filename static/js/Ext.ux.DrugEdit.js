Ext.ux.DrugEditCombo = new Ext.form.ComboBox({
    typeAhead: true,
    triggerAction: 'all',
    mode: 'local',
    store: new Ext.data.ArrayStore({
        id: 0,
        fields: [
            'pk',
            'displayText'
        ],
        data: DrugEdit.choices
    }),
    valueField: 'pk',
    displayField: 'displayText',
    value: 1
});

Ext.ux.DrugEdit = Ext.extend(Ext.grid.EditorGridPanel, {
	id: 'drug-edit-grid',
    frame: true,
    border: false,
    flex: 0.8,
    enableColumnHide: false,
    enableColumnMove: false,
    enableHdMenu: false,
    clicksToEdit: 1,
    saveUrl: URLS.save_drug_value,
    store: new Ext.data.JsonStore({
    	url: URLS.load_drug_grid,
    	fields: DrugEdit.fields,
    	baseParams: {'pks': DrugEdit.load_params},
    	root: 'items'
    }),
    cm: new Ext.grid.ColumnModel({
    	columns: DrugEdit.columns,
    	defaults: {
    		editor: Ext.ux.DrugEditCombo,
    		align: 'right'
    	}
    }),
    listeners: {
		afteredit: function(e){
			Ext.Ajax.request({
				url: this.saveUrl,
				params: {
					value: e.value,
					left: this.getStore().current_drug,
					top: e.field.substr(3),
					criterion: e.record.data.criterion_pk
				}
			});
		}
	}
});

Ext.reg('ext:ux:drug-edit', Ext.ux.DrugEdit);