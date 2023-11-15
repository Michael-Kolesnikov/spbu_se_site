from wtforms import SelectField, StringField, widgets, SelectMultipleField
from flask_wtf import FlaskForm
from wtforms.widgets import TextArea


class InternshipsFilter(FlaskForm):
    format = SelectField("format", choices=[])
    company = SelectField("company", choices=[])
    language = SelectField("language", choices=[])
    tag = SelectField("tag", choices=[])


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class AddInternship(FlaskForm):
    requirements = StringField("requirements", widget=TextArea())
    company = SelectField("company", choices=[])
    name_vacancy = StringField("name_vacancy")
    salary = StringField("salary")
    location = StringField("location")
    more_inf = StringField("more_inf")
    description = StringField("description", widget=TextArea())
    format = MultiCheckboxField("format", coerce=int)
    tag = StringField("tag")
