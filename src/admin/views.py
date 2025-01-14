from flask import redirect, url_for, render_template, session, current_app
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.fields import QuerySelectField
from src.models import (
    Users,
    Staff,
    Worktype,
    Courses,
    AreasOfStudy,
    DiplomaThemes,
)
from src.notification import add_mail_notification
from src.extensions import db
from wtforms import TextAreaField, SelectField
from flask_admin import AdminIndexView, expose
from src.notification import NotificationTemplates

ADMIN_ROLE_LEVEL = 5
REVIEW_ROLE_LEVEL = 3
THESIS_ROLE_LEVEL = 2


# Base model view with access and inaccess methods
class SeAdminModelView(ModelView):
    can_set_page_size = True

    def is_accessible(self):
        if current_user.is_authenticated:
            if current_user.role >= ADMIN_ROLE_LEVEL:
                return True
        else:
            return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("auth.login_index"))


class SeAdminModelViewThesis(SeAdminModelView):
    column_list = (
        "name_ru",
        "name_en",
        "author",
        "supervisor",
        "publish_year",
        "recomended",
        "temporary",
        "review_status",
        "download_thesis",
        "download_presentation",
    )
    form_extra_fields = {
        "supervisor": QuerySelectField(
            "Научный руководитель",
            query_factory=lambda: Staff.query.all(),
            get_pk=lambda staff: staff.id,
        ),
        "owner": QuerySelectField(
            "Author user",
            query_factory=lambda: Users.query.all(),
            get_pk=lambda user: user.id,
        ),
        "type": QuerySelectField(
            "Тип работы",
            query_factory=lambda: Worktype.query.all(),
            get_pk=lambda t: t.id,
        ),
        "course": QuerySelectField(
            "Курс",
            query_factory=lambda: Courses.query.all(),
            get_label=lambda c: c.name,
            get_pk=lambda c: c.id,
        ),
        "area": QuerySelectField(
            "Направление обучения",
            query_factory=lambda: AreasOfStudy.query.all(),
            get_pk=lambda c: c.id,
        ),
    }


class SeAdminModelViewReviewer(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated:
            if current_user.role >= REVIEW_ROLE_LEVEL:
                return True
        else:
            return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("auth.login_index"))

    pass


class SeAdminIndexView(AdminIndexView):
    @expose("/")
    def index(self):
        thesis_key = current_app.config["SECRET_KEY_THESIS"]
        return self.render("admin/index.html", thesis_key=thesis_key)

    def is_accessible(self):
        if current_user.is_authenticated:
            if current_user.role >= THESIS_ROLE_LEVEL:
                return True
        else:
            return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("auth.login_index"))


class SeAdminModelViewUsers(SeAdminModelView):
    column_exclude_list = [
        "password_hash",
        "internship_author",
        "current_thesises",
        "diploma_themes_author",
        "diploma_themes_consultant",
        "diploma_themes_thesis_supervisor",
        "diploma_themes_supervisor",
        "news",
        "staff",
        "all_user_votes",
        "reviewer",
        "thesis_on_review_author",
        "thesises",
    ]
    form_excluded_columns = [
        "password_hash",
        "internship_author",
        "current_thesises",
        "diploma_themes_author",
        "diploma_themes_consultant",
        "diploma_themes_thesis_supervisor",
        "diploma_themes_supervisor",
        "news",
        "staff",
        "all_user_votes",
        "reviewer",
        "thesis_on_review_author",
        "thesises",
    ]
    column_display_pk = True

    pass


class SeAdminModelViewSummerSchool(SeAdminModelView):
    form_overrides = {
        "description": TextAreaField,
        "repo": TextAreaField,
        "demos": TextAreaField,
    }

    form_widget_args = {
        "description": {"rows": 10, "style": "font-family: monospace; width: 680px;"},
        "project_name": {"style": "width: 680px;"},
        "tech": {"rows": 3, "style": "font-family: monospace; width: 680px;"},
        "repo": {"rows": 3, "style": "font-family: monospace; width: 680px;"},
        "demos": {"rows": 3, "style": "font-family: monospace; width: 680px;"},
        "advisors": {"rows": 2, "style": "font-family: monospace; width: 680px;"},
        "requirements": {"rows": 3, "style": "font-family: monospace; width: 680px;"},
    }

    pass


class SeAdminModelViewStaff(SeAdminModelView):
    column_list = (
        "user",
        "official_email",
        "position",
        "science_degree",
        "still_working",
    )
    form_columns = (
        "user",
        "official_email",
        "position",
        "science_degree",
        "still_working",
    )
    form_choices = {
        "science_degree": [
            ("", ""),
            ("д.ф.-м.н.", "д.ф.-м.н."),
            ("д.т.н.", "д.т.н."),
            ("к.ф.-м.н.", "к.ф.-м.н."),
            ("к.т.н.", "к.т.н."),
        ]
    }
    form_extra_fields = {
        "user": QuerySelectField(
            "User",
            query_factory=lambda: Users.query.all(),
            get_pk=lambda user: user.id,
        )
    }


class SeAdminModelViewNews(SeAdminModelView):
    pass


class SeAdminModelViewDiplomaThemes(SeAdminModelView):
    column_labels = dict(
        supervisor_thesis="Научный руководитель ВКР",
        supervisor="Научный руководитель учебных практик",
        comment="Комментарий (что необходимо исправить)",
        status="Статус темы",
        requirements="Требования к студенту",
        title="Название темы",
        description="Описание темы",
        company="Кто представляет тему",
        levels="Уровень темы",
        consultant="Консультант",
        author="Автор темы (кто предложил)",
    )
    column_choices = {
        "status": [
            (0, "На проверке"),
            (1, "Требуется доработка"),
            (2, "Одобрена"),
            (4, "Отклонена"),
        ]
    }

    form_overrides = {
        "description": TextAreaField,
        "requirements": TextAreaField,
        "comment": TextAreaField,
        "status": SelectField,
    }
    form_args = dict(
        status=dict(
            choices=[
                (0, "На проверке"),
                (1, "Требуется доработка"),
                (2, "Одобрена"),
                (4, "Отклонена"),
            ],
            coerce=int,
        )
    )
    form_widget_args = {
        "description": {"rows": 10, "style": "width: 100%;"},
        "comment": {"rows": 4, "style": "width: 100%;"},
        "requirements": {"rows": 4, "style": "width: 100%;"},
    }

    pass


class SeAdminModelViewReviewDiplomaThemes(SeAdminModelViewReviewer):
    can_delete = False
    column_list = (
        "status",
        "comment",
        "title",
        "description",
        "requirements",
        "levels",
        "company",
    )
    column_labels = dict(
        supervisor_thesis="Научный руководитель ВКР",
        supervisor="Научный руководитель учебных практик",
        comment="Комментарий (что нужно исправить, если требуется доработка, или почему тема отклонена)",
        status="Статус темы",
        requirements="Требования к студенту",
        title="Название темы",
        description="Описание темы",
        company="Кто представляет тему",
        levels="Уровень темы",
        consultant="Консультант",
        author="Автор темы (кто предложил)",
    )

    form_overrides = {
        "description": TextAreaField,
        "requirements": TextAreaField,
        "comment": TextAreaField,
        "status": SelectField,
    }

    form_args = dict(
        status=dict(
            choices=[
                (0, "На проверке"),
                (1, "Требуется доработка"),
                (2, "Одобрена"),
                (4, "Отклонена"),
            ],
            coerce=int,
        )
    )

    column_choices = {
        "status": [(0, "На проверке"), (1, "Требуется доработка"), (2, "Одобрена")]
    }

    form_widget_args = {
        "description": {
            "rows": 10,
            "style": "width: 100%;",
        },
        "requirements": {"rows": 3, "style": "width: 100%;"},
        "title": {"readonly": False},
        "level": {"disabled": True},
        "company": {"disabled": False},
        "author": {"readonly": True},
        "comment": {
            "rows": 5,
            "style": "width: 100%;",
        },
    }

    def on_form_prefill(self, form, id):
        session["previous_status"] = DiplomaThemes.query.filter_by(id=id).first().status

    def on_model_change(self, form, model, is_created):
        previous_status = session.get("previous_status")
        if previous_status != model.status and model.status == 4:
            add_mail_notification(
                model.author_id,
                "[SE site] Ваша тема отклонена",
                render_template(
                    NotificationTemplates.DIPLOMA_THEMES_REJECTED.value,
                    title=model.title,
                    comment=model.comment,
                ),
            )
        if previous_status != model.status and model.status == 1:
            add_mail_notification(
                model.author_id,
                "[SE site] Требуется доработка для Вашей темы",
                render_template(
                    NotificationTemplates.DIPLOMA_THEMES_NEED_UPDATE.value,
                    title=model.title,
                    comment=model.comment,
                ),
            )

    def get_query(self):
        return self.session.query(self.model).filter(self.model.status < 2)

    def get_count_query(self):
        return self.session.query(db.func.count("*")).filter(self.model.status < 2)

    pass


class SeAdminModelViewCurrentThesis(SeAdminModelView):
    column_list = (
        "title",
        "user",
        "area",
        "worktype",
        "supervisor",
        "deleted",
        "status",
    )
    column_labels = dict(
        title="Название темы",
        user="Студент",
        area="Направление обучения",
        worktype="Тип работы",
        supervisor="Научный руководитель",
        deleted="Удалена",
        status="Статус",
    )
    column_choices = {"status": [(1, "Текущая работа"), (2, "Завершенная работа")]}
