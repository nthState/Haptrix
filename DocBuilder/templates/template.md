# {{ title }}

{% if breadcrumbs %}
---
Navigation: {% for crumb in breadcrumbs %}[{{ crumb.linkText | replace(".md", "") }}]({{ crumb.link }}){{ " - " if not loop.last else "" }}{% endfor %}
---
{% endif %}


{{ body }}

{% if bodyImage %}
![Image]({{ bodyImage }})
{% endif %}

---

{% for section in sections %}
### {{ section.title }}

{{ section.text }}

{% if section.image %}![section.imageTooltip]({{ section.image }}){% endif %}
{% if section.videoFile %}![]({{ section.videoFile }}){% endif %}
{% if section.link %}[{% if section.linkText %}{{ section.linkText | replace(".md", "") }}{% else %}{{ section.link | replace(".md", "") }}{% endif %}]({{ section.link }}){% endif %}
{% if section.externalLink %}[{{ section.externalLink }}]({{ section.externalLink }}){% endif %}
{% endfor %}

{% if related %}

## Related
---
{% for item in related %}
- [{{ item | replace(".md", "") }}]({{ item }})
{% endfor %}
---
{% endif %}

---

If you didn't find what you were looking for, please [send me a message](mailto:contact+help@haptrix.com)