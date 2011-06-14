django-rte
==========
A rich-text-tinymce-widget with model field for Django.


Requirements
------------
Django >= 1.3


Installation
------------
::

    pip install django-rte


Configuration
-------------
First include ``rte`` in your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'rte',
        ...
    )

Now you can either go with the default base configuration or you can define your
own.  Either way you can always overwrite attributes by passing a config dict to
either the model field or the widget. If you want to set a different base
configuration you just need to place a new config file ``'rte/tiny.config.js'``.

Language is automatically detected for you, should you need to explicitly set a
different language you need to do this in the field or widget config dict and
not in the ``'rte/tine.config.js'`` file.


Examples
--------
Example model usage::

    from rte import RTEField

    class MyModel(models.Model):
        content = RTEField()


Example Widget usage::

    from rte import TinyWidget

    def MyForm(forms.Form):
        content = forms.TextField(widget=TinyWidget(config={'language': 'en'}))

