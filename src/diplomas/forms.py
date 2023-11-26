from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, widgets, SelectMultipleField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired


class DiplomaThemesFilter(FlaskForm):
    company = SelectField("company", choices=[])
    level = SelectField("level", choices=[])
    supervisor = SelectField("supervisor", choices=[])


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class UserAddTheme(FlaskForm):
    title = StringField(
        "title",
        description="Например, реализация алгоритма контекстно-свободной достижимости на OpenCL",
        validators=[DataRequired()],
    )
    description = StringField(
        "description",
        description="Например, необходимо адаптировать библиотеку CLSparse для работы с булевыми матрицами и реализовать алгоритм поиска путей с КС ограничениями, используя результаты адаптации. Провести сравнение с аналогами на существующих данных, проанализировать результаты.",
        widget=TextArea(),
    )
    requirements = StringField(
        "requirements",
        description="Например, умение программировать на OpenCL C. Умение читать и понимать код на OpenCL C.",
        widget=TextArea(),
    )
    levels = MultiCheckboxField("levels", coerce=int)
    consultant = StringField("consultant")
    company = SelectField("company", choices=[])


class UserEditTheme(FlaskForm):
    comment = StringField("comment")
    title = StringField("title", validators=[DataRequired()])
    description = StringField(
        "description", widget=TextArea(), validators=[DataRequired()]
    )
    requirements = StringField("requirements", widget=TextArea())
    levels = MultiCheckboxField("Levels", coerce=int)
    consultant = StringField("consultant")
    company = SelectField("company", choices=[])
    supervisor = StringField("supervisor")
    theme_id = StringField("theme_id")
    status = StringField("status")
