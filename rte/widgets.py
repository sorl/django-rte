from django.conf import settings
from django import forms
from django.template.loader import render_to_string
from django.utils import simplejson


class TinyWidget(forms.Textarea):
    config = {}

    def __init__(self, attrs=None, config=None):
        self.config.update(config or {})
        super(TinyWidget, self).__init__(attrs)

    def render(self, name, value, attrs):
        editor_selector = 'tiny-%s' % attrs['id']
        attrs['class'] = editor_selector
        self.config['editor_selector'] = editor_selector
        s = super(TinyWidget, self).render(name, value, attrs)
        return s + render_to_string('rte/tiny.html', {
            'config': simplejson.dumps(self.config),
        })

    class Media:
        js = (
            'http://ajax.microsoft.com/ajax/jquery/jquery-1.5.min.js',
            'rte/tiny_mce/tiny_mce.js',
            'rte/tiny_mce/config.js',
        )

