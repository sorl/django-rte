from django.db import models
from django.utils.encoding import smart_unicode
from django.utils.translation import get_language, ugettext_lazy as _
from rte.widgets import TinyWidget


class RTEField(models.Field):
    """
    Rich Text Editor Field, we can't subclass TextField since ModelAdmin
    will search mro for a fitting widget.
    """
    description = _('Text')
    config = {}

    def __init__(self, *args, **kwargs):
        self.config.update(kwargs.pop('config', {}))
        language = get_language().split('_')[0].lower()
        self.config.setdefault('language', language)
        super(RTEField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return 'TextField'

    def get_prep_value(self, value):
        if isinstance(value, basestring) or value is None:
            return value
        return smart_unicode(value)

    def formfield(self, **kwargs):
        kwargs.setdefault('widget', TinyWidget(config=self.config))
        return super(RTEField, self).formfield(**kwargs)

    def south_field_triple(self):
        from south.modelsinspector import introspector
        args, kwargs = introspector(self)
        return ('django.db.models.fields.TextField', args, kwargs)

