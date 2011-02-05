from django.db import models
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _
from rte.widgets import TinyWidget


class RTEField(models.Field):
    """
    Rich Text Editor Field, we can't subclass TextField since ModelAdmin
    will search mro for a fitting widget.
    """
    description = _("Text")
    config = {}

    def get_internal_type(self):
        return "TextField"

    def get_prep_value(self, value):
        if isinstance(value, basestring) or value is None:
            return value
        return smart_unicode(value)

    def formfield(self, **kwargs):
        defaults = {'widget': TinyWidget(config=self.config)}
        defaults.update(kwargs)
        return super(RTEField, self).formfield(**defaults)

    def south_field_triple(self):
        from south.modelsinspector import introspector
        args, kwargs = introspector(self)
        return ('django.db.models.fields.TextField', args, kwargs)


