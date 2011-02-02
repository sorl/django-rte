django-rte
==========
A rich-text-tinymce-widget with model field for Django.

Example model usage::

    from rte import RTEField

    class MyModel(models.Model):
        content = RTEField()


Example Widget usage::

    from rte import TinyWidget

    def MyForm(forms.Form):
        content = forms.TextField(widget=TinyWidget(config={'language': 'en'}))

