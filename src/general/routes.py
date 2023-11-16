from src.general import bp
from flask import render_template, redirect, url_for
from src.general.date_formatting import get_hours_since, plural_hours
import random
from src.models import Curriculum, Posts, Thesis, Staff, Worktype, Courses
from sqlalchemy.sql.expression import func


@bp.route("/")
def index():
    ages = []
    news = (
        Posts.query.filter(Posts.type_id > 0)
        .order_by(Posts.rank.desc())
        .limit(10)
        .all()
    )
    for post in news:
        ages.append(plural_hours(int(get_hours_since(post.created_on))))

    return render_template("general/index.html", news=news, ages=ages)


@bp.route("/index.html")
def index_html():
    return redirect(url_for("index"))


@bp.route("/bachelor/admission.html")
def bachelor_admission():
    students = []
    theses = ()
    staff = ()
    records = Thesis.query.filter_by(recomended=True)
    print(records.count())
    if records.count():
        theses = records.order_by(func.random()).limit(4).all()
    else:
        theses = []
    staff = Staff.query.filter_by(still_working=True).limit(6).all()
    return render_template(
        "general/navbar/bachelor_admission.html",
        students=students,
        theses=theses,
        staff=staff,
    )


@bp.route("/frequently-asked-questions.html")
def frequently_asked_questions():
    return render_template("general/navbar/frequently_asked_questions.html")


@bp.route("/nooffer")
def nooffer():
    return render_template("nooffer.html")


@bp.route("/department/staff.html")
def department_staff():
    records = Staff.query.filter_by(still_working=True).all()
    staff = []

    # TODO: no need loop
    for s in records:
        position = s.position
        if s.science_degree:
            position = position + ", " + s.science_degree

        staff.append(
            {
                "name": s.user.get_name(),
                "position": position,
                "contacts": s.official_email,
                "avatar": s.user.avatar_uri,
                "id": s.id,
            }
        )

    return render_template("department_staff.html", staff=staff)


@bp.route("/master/information-systems-administration.html")
def master_information_systems_administration():
    return render_template("master_information-systems-administration.html")


@bp.route("/master/software-engineering.html")
def master_software_engineering():
    return render_template("master_software-engineering.html")



@bp.route("/bachelor/software-engineering.html")
def bachelor_software_engineering():
    curricula1 = (
        Curriculum.query.filter(Curriculum.course_id == 2)
        .filter(Curriculum.study_year == 1)
        .order_by(Curriculum.type)
        .all()
    )
    curricula2 = (
        Curriculum.query.filter(Curriculum.course_id == 2)
        .filter(Curriculum.study_year == 2)
        .order_by(Curriculum.type)
        .all()
    )
    curricula3 = (
        Curriculum.query.filter(Curriculum.course_id == 2)
        .filter(Curriculum.study_year == 3)
        .order_by(Curriculum.type)
        .all()
    )
    curricula4 = (
        Curriculum.query.filter(Curriculum.course_id == 2)
        .filter(Curriculum.study_year == 4)
        .order_by(Curriculum.type)
        .all()
    )

    return render_template(
        "bachelor_software-engineering.html",
        curricula1=curricula1,
        curricula2=curricula2,
        curricula3=curricula3,
        curricula4=curricula4,
    )



@bp.route("/contacts.html")
def contacts():
    return render_template("contacts.html")


@bp.route("/students/index.html")
def students():
    return render_template("students.html")


@bp.route("/bachelor/application.html")
def bachelor_application():
    return render_template("bachelor_application.html")


@bp.route("/bachelor/programming-technology.html")
def bachelor_programming_technology():
    curricula1 = (
        Curriculum.query.filter(Curriculum.course_id == 1)
        .filter(Curriculum.study_year == 1)
        .order_by(Curriculum.type)
        .all()
    )
    curricula2 = (
        Curriculum.query.filter(Curriculum.course_id == 1)
        .filter(Curriculum.study_year == 2)
        .order_by(Curriculum.type)
        .all()
    )
    curricula3 = (
        Curriculum.query.filter(Curriculum.course_id == 1)
        .filter(Curriculum.study_year == 3)
        .order_by(Curriculum.type)
        .all()
    )
    curricula4 = (
        Curriculum.query.filter(Curriculum.course_id == 1)
        .filter(Curriculum.study_year == 4)
        .order_by(Curriculum.type)
        .all()
    )

    return render_template(
        "bachelor_programming-technology.html",
        curricula1=curricula1,
        curricula2=curricula2,
        curricula3=curricula3,
        curricula4=curricula4,
    )


from flask_wtf import FlaskForm
from wtforms import SelectField


class ThesisFilter(FlaskForm):
    worktype = SelectField("worktype", choices=[])
    course = SelectField("course", choices=[])
    supervisor = SelectField("supervisor", choices=[])
    startdate = SelectField("worktype", choices=[])
    enddate = SelectField("worktype", choices=[])


@bp.route("/theses.html")
def theses_search():
    filter = ThesisFilter()
    hints = [
        '"Максим" можно искать как Максим, максим, Макс* или *акс*.',
        "Полнотекстовый поиск по названиям работ и авторам",
        '"Дом" можно искать как дом, д?м или д*м',
    ]

    hint = random.choice(hints)

    for sid in Thesis.query.with_entities(Thesis.type_id).distinct().all():
        type = Worktype.query.filter_by(id=sid[0]).first()

        filter.worktype.choices.append((sid[0], type.type))
        filter.worktype.choices.sort(key=lambda tup: tup[1])

    for sid in Thesis.query.with_entities(Thesis.course_id).distinct().all():
        course = Courses.query.filter_by(id=sid[0]).first()

        filter.course.choices.append((sid[0], course.name))
        filter.course.choices.sort(key=lambda tup: tup[1])

    dates = [
        theses.publish_year
        for theses in Thesis.query.filter(Thesis.temporary == False)
        .with_entities(Thesis.publish_year)
        .distinct()
    ]
    dates.sort(reverse=True)
    filter.startdate.choices = dates
    filter.enddate.choices = dates

    for sid in Thesis.query.with_entities(Thesis.supervisor_id).distinct().all():
        staff = Staff.query.filter_by(id=sid[0]).first()
        last_name = ""
        initials = ""

        if not staff:
            staff = Staff.query.filter_by(id=1).first()

        if staff.user.last_name:
            last_name = staff.user.last_name

        if staff.user.first_name:
            initials = initials + staff.user.first_name[0] + "."

        if staff.user.middle_name:
            initials = initials + staff.user.middle_name[0] + "."

        filter.supervisor.choices.append((sid[0], last_name + " " + initials))
        filter.supervisor.choices.sort(key=lambda tup: tup[1])

    filter.supervisor.choices.insert(0, (0, "Все"))
    filter.course.choices.insert(0, (0, "Все"))
    filter.worktype.choices.insert(0, (0, "Все"))
    return render_template("general/theses.html", filter=filter, hint=hint)
