var URLS = {
	{% for item in urls %}
		{{ item.0 }}: "{{ item.1 }}?pk={{ group_pk }}"{% if not forloop.last %},{% endif %}
	{% endfor %}
}