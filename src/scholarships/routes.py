from src.scholarships import bp
from flask import render_template


@bp.route("/students/scholarships.html")
def scholarships():
    return render_template("scholarships/students_scholarships.html")


@bp.route("/scholarships/1.html")
def get_scholarships_1():
    return render_template("scholarships/scholarships_types/scholarships/1.html")


@bp.route("/scholarships/2.html")
def get_scholarships_2():
    return render_template("scholarships/scholarships_types/cholarships/2.html")


@bp.route("/scholarships/3.html")
def get_scholarships_3():
    return render_template("scholarships/scholarships_types/scholarships/3.html")


@bp.route("/scholarships/4.html")
def get_scholarships_4():
    return render_template("scholarships/scholarships_types/scholarships/4.html")


@bp.route("/scholarships/5.html")
def get_scholarships_5():
    return render_template("scholarships/scholarships_types/scholarships/5.html")


@bp.route("/scholarships/6.html")
def get_scholarships_6():
    return render_template("scholarships/scholarships_types/scholarships/6.html")


@bp.route("/scholarships/7.html")
def get_scholarships_7():
    return render_template("scholarships/scholarships_types/scholarships/7.html")


@bp.route("/scholarships/8.html")
def get_scholarships_8():
    return render_template("scholarships/scholarships_types/scholarships/8.html")


@bp.route("/scholarships/9.html")
def get_scholarships_9():
    return render_template("scholarships/scholarships_types/scholarships/9.html")


@bp.route("/scholarships/10.html")
def get_scholarships_10():
    return render_template("scholarships/scholarships_types/scholarships/10.html")


@bp.route("/scholarships/11.html")
def get_scholarships_11():
    return render_template("scholarships/scholarships_types/scholarships/11.html")


@bp.route("/scholarships/12.html")
def get_scholarships_12():
    return render_template("scholarships/scholarships_types/scholarships/12.html")


@bp.route("/scholarships/13.html")
def get_scholarships_13():
    return render_template("scholarships/scholarships_types/scholarships/13.html")
