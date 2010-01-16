Ext.ns('DrugEdit');

DrugEdit.choices = [
    [9, 9],
    [7, 7],
    [5, 5],
    [3, 3],
    [1, 1],
    ['1/3', '1/3'],
    ['1/5', '1/5'],
    ['1/7', '1/7'],
    ['1/9', '1/9']
];

DrugEdit.columns = [
    {
    	header: "Name",
    	dataIndex: "criterion",
    	editable: false,
    	align: "left"
    },
    {% for item in items %}
    	{
    		header: "{{ item.name }}",
    		dataIndex: "{{ item.store_column }}",
    		pk: "{{ item.pk }}"
    	}{% if not forloop.last %},{% endif %}
    {% endfor %}
];

DrugEdit.fields = [
    "criterion",
    "criterion_pk",
    {% for item in items %}
	   	"{{ item.store_column }}"{% if not forloop.last %},{% endif %}
    {% endfor %}                   
];

DrugEdit.load_params = [
    {% for item in items %}
	   	{{ item.pk }}{% if not forloop.last %},{% endif %}
    {% endfor %}                   
];