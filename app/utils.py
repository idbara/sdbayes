from flask import url_for
from wtforms.compat import text_type
from wtforms.fields import Field
from wtforms.widgets import HiddenInput


def register_template_utils(app):
    """Register Jinja 2 helpers (called from __init__.py)."""
    @app.template_test()
    def equalto(value, other):
        return value == other

    @app.template_global()
    def is_hidden_field(field):
        from wtforms.fields import HiddenField
        return isinstance(field, HiddenField)

    app.add_template_global(index_for_role)


def index_for_role(role):
    return url_for(role.index)


class CustomSelectField(Field):
    widget = HiddenInput()

    def __init__(self,
                 label='',
                 validators=None,
                 multiple=False,
                 choices=[],
                 allow_custom=True,
                 **kwargs):
        super(CustomSelectField, self).__init__(label, validators, **kwargs)
        self.multiple = multiple
        self.choices = choices
        self.allow_custom = allow_custom

    def _value(self):
        return text_type(self.data) if self.data is not None else ''

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = valuelist[1]
            self.raw_data = [valuelist[1]]
        else:
            self.data = ''


def int_to_month(m):
    s = ''
    if m == 1:
        s = "Januari"
    elif m == 2:
        s = "Februari"
    elif m == 3:
        s = "Maret"
    elif m == 4:
        s = "April"
    elif m == 5:
        s = "Mei"
    elif m == 6:
        s = "Juni"
    elif m == 7:
        s = "Juli"
    elif m == 8:
        s = "Agustus"
    elif m == 9:
        s = "September"
    elif m == 10:
        s = "Oktober"
    elif m == 11:
        s = "November"
    elif m == 12:
        s = "Desember"
    return s