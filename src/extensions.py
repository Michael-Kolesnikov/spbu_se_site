import shutil
from flask_login import LoginManager
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
from flask import current_app
from os import urandom
from werkzeug.security import generate_password_hash
from src.data import areas, users, staff

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)

from src.models import (
    AreasOfStudy,
    Company,
    Courses,
    Curriculum,
    DiplomaThemes,
    InternshipFormat,
    InternshipTag,
    Posts,
    Tags,
    ThemesLevel,
    Thesis,
    Users,
    Staff,
    Worktype,
)
from src.data import (
    wtypes,
    curriculum,
    posts,
    courses,
    tags,
    thesis,
    company,
    d_themes,
    themes_level,
    internship_formats,
    internship_tags,
)


login_manager = LoginManager()
login_manager.login_view = "login_index"


def init_db():
    # Check if databases directory exists. If not, create it
    db_dir = Path(current_app.config["SQLITE_DATABASE_PATH"])
    if not db_dir.exists():
        db_dir.mkdir()
    # Check if db file already exists. If so, backup it
    db_file = Path(
        current_app.config["SQLITE_DATABASE_PATH"]
        + current_app.config["SQLITE_DATABASE_NAME"]
    )
    if db_file.is_file():
        shutil.copyfile(
            current_app.config["SQLITE_DATABASE_PATH"]
            + current_app.config["SQLITE_DATABASE_NAME"],
            current_app.config["SQLITE_DATABASE_PATH"]
            + current_app.config["SQLITE_DATABASE_BACKUP_NAME"],
        )
    # Init DB
    db.session.commit()  # https://stackoverflow.com/questions/24289808/drop-all-freezes-in-flask-with-sqlalchemy
    db.drop_all()
    db.create_all()

    # Create areas
    print("Create areas")
    for area in areas:
        a = AreasOfStudy(area=area["area"])

        db.session.add(a)
        db.session.commit()

    # Create users
    print("Create users")
    for user in users:
        u = Users(
            email=user["email"],
            password_hash=generate_password_hash(urandom(16).hex()),
            first_name=user["first_name"],
            last_name=user["last_name"],
            middle_name=user["middle_name"],
            avatar_uri=user["avatar_uri"],
        )

        db.session.add(u)
        db.session.commit()
    # Create staff
    print("Create staff")
    for user in staff:
        u = Users.query.filter_by(email=user["official_email"]).first()

        if "science_degree" in user:
            s = Staff(
                position=user["position"],
                science_degree=user["science_degree"],
                official_email=user["official_email"],
                still_working=user["still_working"],
                user_id=u.id,
            )
        else:
            s = Staff(
                position=user["position"],
                official_email=user["official_email"],
                still_working=user["still_working"],
                user_id=u.id,
            )

        db.session.add(s)
        db.session.commit()

    # Create WorkTypes
    print("Create worktypes")
    for w in wtypes:
        wt = Worktype(type=w["type"])
        db.session.add(wt)
        db.session.commit()

    # Create Courses
    print("Create courses")
    for course in courses:
        c = Courses(name=course["name"], code=course["code"])
        db.session.add(c)
        db.session.commit()

    # Create Curriculum
    print("Create curriculum")
    for cur in curriculum:
        if "type" in cur:
            c = Curriculum(
                year=cur["year"],
                discipline=cur["discipline"],
                study_year=cur["study_year"],
                type=cur["type"],
                course_id=cur["course_id"],
            )
        else:
            c = Curriculum(
                year=cur["year"],
                discipline=cur["discipline"],
                study_year=cur["study_year"],
                course_id=cur["course_id"],
            )

        db.session.add(c)
        db.session.commit()

    # Create News
    print("Create news")
    for cur in posts:
        if "uri" in cur:
            c = Posts(
                title=cur["title"],
                uri=cur["uri"],
                domain="se.math.spbu.ru",
                author_id=cur["author_id"],
            )
        else:
            c = Posts(title=cur["title"], text=cur["text"], author_id=cur["author_id"])

        db.session.add(c)
        db.session.commit()

    for tag in tags:
        t = Tags(name=tag["name"])
        db.session.add(t)
        db.session.commit()

    # Create Thesis
    print("Create thesis")
    for work in thesis:
        if "source_uri" in work:
            t = Thesis(
                name_ru=work["name_ru"],
                name_en=work["name_en"],
                description=work["description"],
                text_uri=work["text_uri"],
                presentation_uri=work["presentation_uri"],
                supervisor_review_uri=work["supervisor_review_uri"],
                reviewer_review_uri=work["reviewer_review_uri"],
                author=work["author"],
                supervisor_id=work["supervisor_id"],
                reviewer_id=work["reviewer_id"],
                publish_year=work["publish_year"],
                type_id=work["type_id"],
                course_id=1,
                source_uri=work["source_uri"],
            )
        else:
            t = Thesis(
                name_ru=work["name_ru"],
                name_en=work["name_en"],
                description=work["description"],
                text_uri=work["text_uri"],
                presentation_uri=work["presentation_uri"],
                supervisor_review_uri=work["supervisor_review_uri"],
                reviewer_review_uri=work["reviewer_review_uri"],
                author=work["author"],
                supervisor_id=work["supervisor_id"],
                reviewer_id=work["reviewer_id"],
                publish_year=work["publish_year"],
                type_id=work["type_id"],
                course_id=1,
            )

        db.session.add(t)
        db.session.commit()

        # Adds tags
        records = Tags.query.all()
        for tag in records:
            t.tags.append(tag)
            db.session.commit()

    # Create Companies
    print("Create companies")
    for cur in company:
        c = Company(name=cur["name"], logo_uri=cur["logo_uri"])

        db.session.add(c)
        db.session.commit()

    # Create ThemesLevels
    print("Create diploma theme levels")
    for cur in themes_level:
        c = ThemesLevel(level=cur["level"])

        db.session.add(c)
        db.session.commit()

    # Create DiplomaThems
    print("Create diploma themes")
    for cur in d_themes:
        c = DiplomaThemes(
            title=cur["title"],
            description=cur["description"],
            company_id=cur["company_id"],
            supervisor_id=cur["supervisor_id"],
            consultant_id=cur["consultant_id"],
            author_id=cur["author_id"],
            status=cur["status"],
        )

        for tl_id in cur["levels"]:
            c.levels.append(ThemesLevel.query.filter_by(id=tl_id).first())

        db.session.add(c)
        db.session.commit()

    # Create InternshipsFormat
    print("Create internship formats")
    print("Create addinternship formats")
    for cur in internship_formats:
        c = InternshipFormat(format=cur["format"])

        db.session.add(c)
        db.session.commit()

    print("Create internship tags")
    for cur in internship_tags:
        t = InternshipTag(tag=cur["tag"])

        db.session.add(t)
        db.session.commit()
