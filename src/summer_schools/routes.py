from src.summer_schools import bp
from flask import render_template
from src.models import SummerSchool

@bp.route("/summer_school_2021.html")
def summer_school_2021():
    projects = SummerSchool.query.filter_by(year=2021).all()
    projects = ()
    return render_template("summer_schools/summer_school_2021.html", projects=projects)

@bp.route("/summer_school_2022.html")
def summer_school_2022():
    projects = SummerSchool.query.filter_by(year=2022).all()
    projects = ()
    return render_template("summer_schools/summer_school_2022.html", projects=projects)
