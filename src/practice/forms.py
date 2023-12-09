from wtforms import SelectField, StringField, DateTimeField, validators
from flask_wtf import FlaskForm
from wtforms.widgets import TextArea
from datetime import datetime


class CurrentWorktypeArea(FlaskForm):
    worktype = SelectField("worktype", choices=[])
    area = SelectField("area", choices=[])


class ChooseTopic(FlaskForm):
    topic = StringField(
        "topic",
        description="Например, реализация алгоритма контекстно-свободной достижимости на OpenCL",
    )
    staff = SelectField("staff", choices=[])
    consultant = StringField(
        "consultant", description="ФИО консультанта, должность и компания"
    )


class DeadlineTemp(FlaskForm):
    area = SelectField("area", choices=[], validators=[validators.Optional()])
    worktype = SelectField("worktype", choices=[], validators=[validators.Optional()])
    choose_topic = DateTimeField("choose_topic")
    submit_work_for_review = DateTimeField("submit_work_for_review")
    upload_reviews = DateTimeField("upload_reviews")
    pre_defense = DateTimeField("pre_defense")
    defense = DateTimeField("defense")


class AddGoal(FlaskForm):
    goal = StringField(
        "goal",
        description="Например, модификация библиотеки COLMAP оптимальным алгоритмом локализации некалиброванной камеры относительно облака 3D точек.",
    )


class AddTask(FlaskForm):
    task_text = StringField(
        "task_text", description="Например, научиться работать с ajax."
    )


class UserAddReport(FlaskForm):
    was_done = StringField(
        "was_done",
        description="Например: Провел сравнение моего проекта с аналогами. "
        "Составил таблицу, проанализировал результаты. Сформулировал, чем "
        "мой проект лучше остальных. и занес в текст введения полученную"
        " информацию.",
        widget=TextArea(),
    )
    planned_to_do = StringField(
        "planned_to_do",
        description="Например: В ближайшее время планирую дописать введение, "
        "изучить MySQL по курсам на Stepik, составить схему баз "
        "данных для моего проекта.",
        widget=TextArea(),
    )


class StaffAddCommentToReport(FlaskForm):
    comment = StringField(
        "comment",
        description="Можете дать студенту обратную связь по отчёту",
        widget=TextArea(),
    )


class ChooseCourseAndYear(FlaskForm):
    course = SelectField("course", choices=[])

    current_year = datetime.now().year
    years = [
        (str(year), str(year)) for year in range(current_year - 5, current_year + 3)
    ]
    publish_year = SelectField("publish_year", choices=years, default=str(current_year))
