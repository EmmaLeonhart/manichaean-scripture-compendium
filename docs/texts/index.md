---
title: Texts
---

{% assign texts = site.pages | where: "text", true | sort: "order" %}
{% for t in texts %}
- [{{ t.title }}]({{ t.url | relative_url }}): {{ t.summary }} <span class="sec">({{ t.original_language }}; {{ t.rights }})</span>
{% endfor %}

More texts are on the way. See the [plan](../about/#plan).
