from flask_login import UserMixin
from src.extensions import db
from datetime import datetime

diploma_themes_level = db.Table(
    "diploma_themes_level",
    db.Column(
        "themes_level_id",
        db.Integer,
        db.ForeignKey("themes_level.id"),
        primary_key=True,
    ),
    db.Column(
        "diploma_themes_id",
        db.Integer,
        db.ForeignKey("diploma_themes.id"),
        primary_key=True,
    ),
)
diploma_themes_tag = db.Table(
    "diploma_themes_tag",
    db.Column(
        "diploma_themes_tag_id",
        db.Integer,
        db.ForeignKey("diploma_themes_tags.id"),
        primary_key=True,
    ),
    db.Column(
        "diploma_themes_id",
        db.Integer,
        db.ForeignKey("diploma_themes.id"),
        primary_key=True,
    ),
)
internships_format = db.Table(
    "internships_format",
    db.Column(
        "internships_format_id",
        db.Integer,
        db.ForeignKey("internship_format.id"),
        primary_key=True,
    ),
    db.Column(
        "internships_id", db.Integer, db.ForeignKey("internships.id"), primary_key=True
    ),
)
internships_tag = db.Table(
    "internships_tag",
    db.Column(
        "internships_tag_id",
        db.Integer,
        db.ForeignKey("internship_tag.id"),
        primary_key=True,
    ),
    db.Column(
        "internships_id", db.Integer, db.ForeignKey("internships.id"), primary_key=True
    ),
)
tag = db.Table(
    "tag",
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id"), primary_key=True),
    db.Column("thesis_id", db.Integer, db.ForeignKey("thesis.id"), primary_key=True),
)

# https://felx.me/2021/08/29/improving-the-hacker-news-ranking-algorithm.html
def post_ranking_score(upvotes=1, age=0, views=1):
    u = upvotes**0.8
    a = (age + 2) ** 1.8
    return (u / a) / (views + 1)

class SummerSchool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, default=2021, nullable=False)
    project_name = db.Column(db.String(1024), nullable=False)
    description = db.Column(db.String(2048), nullable=False)
    tech = db.Column(db.String(1024), nullable=False)
    repo = db.Column(db.String(1024), nullable=True)
    demos = db.Column(db.String(1024), nullable=True)
    advisors = db.Column(db.String(1024), nullable=False)
    requirements = db.Column(db.String(1024), nullable=False)

class Users(db.Model, UserMixin):
    __searchable__ = ["first_name", "middle_name", "last_name"]

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(255), unique=True, nullable=True)
    password_hash = db.Column(db.String(255), unique=False, nullable=True)

    first_name = db.Column(db.String(255), nullable=False)
    middle_name = db.Column(db.String(255), nullable=True)
    last_name = db.Column(db.String(255), nullable=True)

    avatar_uri = db.Column(db.String(512), default="empty.jpg", nullable=False)

    role = db.Column(db.Integer, default=0, nullable=False)
    how_to_contact = db.Column(db.String(512), default="", nullable=True)

    vk_id = db.Column(db.String(255), nullable=True)
    fb_id = db.Column(db.String(255), nullable=True)
    google_id = db.Column(db.String(255), nullable=True)

    staff = db.relationship("Staff", backref=db.backref("user", uselist=False))
    news = db.relationship("Posts", backref=db.backref("author", uselist=False))
    diploma_themes_supervisor = db.relationship(
        "DiplomaThemes",
        backref=db.backref("supervisor", uselist=False),
        foreign_keys="DiplomaThemes.supervisor_id",
    )
    diploma_themes_thesis_supervisor = db.relationship(
        "DiplomaThemes",
        backref=db.backref("supervisor_thesis", uselist=False),
        foreign_keys="DiplomaThemes.supervisor_thesis_id",
    )
    diploma_themes_consultant = db.relationship(
        "DiplomaThemes",
        backref=db.backref("consultant", uselist=False),
        foreign_keys="DiplomaThemes.consultant_id",
    )
    diploma_themes_author = db.relationship(
        "DiplomaThemes",
        backref=db.backref("author", uselist=False),
        foreign_keys="DiplomaThemes.author_id",
    )

    current_thesises = db.relationship(
        "CurrentThesis", backref=db.backref("user", uselist=False)
    )
    thesises = db.relationship("Thesis", backref=db.backref("owner", uselist=False))
    thesis_on_review_author = db.relationship(
        "ThesisOnReview", backref=db.backref("author", uselist=False)
    )

    reviewer = db.relationship("Reviewer", back_populates="user")

    all_user_votes = db.relationship("PostVote", back_populates="user")
    internship_author = db.relationship(
        "Internships",
        backref=db.backref("user", uselist=False),
        foreign_keys="Internships.author_id",
    )

    def get_name(self):
        full_name = ""
        if self.last_name:
            full_name = str(self.last_name)

        if self.first_name:
            full_name = full_name + " " + self.first_name

        if self.middle_name:
            full_name = full_name + " " + self.middle_name

        return full_name

    def is_staff(self):
        return Staff.query.filter_by(user_id=self.id).first() is not None

    def __str__(self):
        full_name = ""
        if self.last_name:
            full_name = str(self.last_name)

        if self.first_name:
            full_name = full_name + " " + self.first_name

        if self.middle_name:
            full_name = full_name + " " + self.middle_name

        if self.email:
            return full_name + " (" + self.email + ")"
        else:
            return full_name

    def __repr__(self):
        full_name = ""
        if self.last_name:
            full_name = full_name + self.last_name

        if self.first_name:
            full_name = full_name + " " + self.first_name

        if self.middle_name:
            full_name = full_name + " " + self.middle_name

        return full_name

class DiplomaThemes(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(512), nullable=False)
    description = db.Column(db.String(2048), nullable=True)
    requirements = db.Column(db.String(2048), nullable=True)
    status = db.Column(
        db.Integer, default=0, nullable=False
    )  # 0 - new, 1 - need update, 2 - approved, 3 - archive, 4 - rejected

    comment = db.Column(db.String(2048), nullable=True)

    levels = db.relationship(
        "ThemesLevel",
        secondary=diploma_themes_level,
        lazy="subquery",
        backref=db.backref("diploma_themes", lazy=True),
        order_by=diploma_themes_level.c.themes_level_id,
    )

    company_id = db.Column(db.Integer, db.ForeignKey("company.id"))
    company = db.relationship("Company", back_populates="theme")

    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    supervisor_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    supervisor_thesis_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=True
    )
    consultant_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"{self.title}"

    def __str__(self):
        return f"{self.title}"

class DiplomaThemesTags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    tags = db.relationship(
        "DiplomaThemes",
        secondary=diploma_themes_tag,
        lazy="subquery",
        backref=db.backref("diploma_themes_tags", lazy=True),
    )

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    official_email = db.Column(db.String(255), unique=True, nullable=False)
    position = db.Column(db.String(255), nullable=False)
    science_degree = db.Column(db.String(255), nullable=True)
    still_working = db.Column(db.Boolean, default=False, nullable=False)

    supervisor = db.relationship(
        "Thesis", backref=db.backref("supervisor"), foreign_keys="Thesis.supervisor_id"
    )
    adviser = db.relationship(
        "Thesis", backref=db.backref("reviewer"), foreign_keys="Thesis.reviewer_id"
    )
    current_thesises = db.relationship(
        "CurrentThesis", backref=db.backref("supervisor")
    )

    def __repr__(self):
        return "<%r>" % self.official_email

    def __str__(self):
        return self.user.get_name()

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(2048), nullable=False)
    uri = db.Column(db.String(1024), nullable=True)
    domain = db.Column(db.String(512), nullable=True)
    text = db.Column(db.String(4096), nullable=True)
    votes = db.Column(db.Integer, nullable=False, default=1)
    views = db.Column(db.Integer, nullable=False, default=1)

    created_on = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime(timezone=True),
        server_default=db.func.now(),
        server_onupdate=db.func.now(),
    )

    rank = db.Column(db.Float, nullable=False, default=post_ranking_score)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    all_news_votes = db.relationship("PostVote", back_populates="post")

    type_id = db.Column(db.Integer, db.ForeignKey("post_type.id"))
    type = db.relationship("PostType", back_populates="post")

class PostVote(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    user = db.relationship("Users", back_populates="all_user_votes")

    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    post = db.relationship("Posts", back_populates="all_news_votes")

    upvote = db.Column(db.Boolean, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        if self.upvote:
            vote = "Up"
        else:
            vote = "Down"
        return "<Vote - {}, from {} for {}>".format(
            vote, self.user.get_name(), self.post.title
        )

class PostType(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    type = db.Column(db.Integer, nullable=False, default=1)
    name = db.Column(db.String(512), nullable=False)

    post = db.relationship("Posts", back_populates="type")

    def __str__(self):
        return self.name

class CurrentThesis(db.Model):
    __tablename__ = "current_thesis"

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    area_id = db.Column(db.Integer, db.ForeignKey("areas_of_study.id"), nullable=True)

    title = db.Column(db.String(512), nullable=True)

    supervisor_id = db.Column(db.Integer, db.ForeignKey("staff.id"), nullable=True)
    worktype_id = db.Column(db.Integer, db.ForeignKey("worktype.id"), nullable=False)
    consultant = db.Column(db.String(2048), nullable=True)

    goal = db.Column(db.String(2048), nullable=True)

    text_uri = db.Column(db.String(512), nullable=True)
    supervisor_review_uri = db.Column(db.String(512), nullable=True)
    reviewer_review_uri = db.Column(db.String(512), nullable=True)
    presentation_uri = db.Column(db.String(512), nullable=True)

    text_link = db.Column(db.String(2048), nullable=True)
    presentation_link = db.Column(db.String(2048), nullable=True)
    code_link = db.Column(db.String(2048), nullable=True)
    account_name = db.Column(db.String(512), nullable=True)

    reports = db.relationship("ThesisReport", backref=db.backref("practice"))
    tasks = db.relationship("ThesisTask", backref=db.backref("practice"))

    archived = db.Column(db.Boolean, default=False)
    deleted = db.Column(db.Boolean, default=False)
    status = db.Column(db.Integer, default=1)
    # 1 - active practice
    # 2 - past practice

    def __init__(self, author_id, worktype_id, area_id):
        self.author_id = author_id
        self.worktype_id = worktype_id
        self.area_id = area_id

    def __repr__(self):
        return self.title

class Thesis(db.Model):
    __searchable__ = ["name_ru", "description", "author", "text"]

    id = db.Column(db.Integer, primary_key=True)

    type_id = db.Column(db.Integer, db.ForeignKey("worktype.id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)

    area_id = db.Column(db.Integer, db.ForeignKey("areas_of_study.id"), nullable=True)

    name_ru = db.Column(db.String(512), nullable=False)
    name_en = db.Column(db.String(512), nullable=True)
    description = db.Column(db.String(4096), nullable=True)

    text_uri = db.Column(db.String(512), nullable=True)
    old_text_uri = db.Column(db.String(512), nullable=True)
    presentation_uri = db.Column(db.String(512), nullable=True)
    supervisor_review_uri = db.Column(db.String(512), nullable=True)
    reviewer_review_uri = db.Column(db.String(512), nullable=True)
    source_uri = db.Column(db.String(512), nullable=True)

    author = db.Column(db.String(512), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    supervisor_id = db.Column(db.Integer, db.ForeignKey("staff.id"), nullable=True)
    reviewer_id = db.Column(db.Integer, db.ForeignKey("staff.id"), nullable=True)

    publish_year = db.Column(db.Integer, nullable=False)
    recomended = db.Column(db.Boolean, default=False, nullable=False)
    temporary = db.Column(db.Boolean, default=False, nullable=False)
    text = db.Column(db.Text, nullable=True)

    # 0 - success review (or not needed)
    # 1 - need to review
    # 2 - on review (in progress)
    # 3 - failed to review
    review_status = db.Column(db.Integer, nullable=True, default=10)

    review = db.relationship("ThesisReview", back_populates="thesis")

    download_thesis = db.Column(db.Integer, default=0, nullable=True)
    download_presentation = db.Column(db.Integer, default=0, nullable=True)

class ThesisReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    thesis_id = db.Column(db.Integer, db.ForeignKey("thesis.id"))
    thesis = db.relationship("Thesis", back_populates="review")

    thesis_on_review_id = db.Column(db.Integer, db.ForeignKey("thesis_on_review.id"))
    thesis_on_review = db.relationship("ThesisOnReview", back_populates="review")

    o1 = db.Column(db.Integer, nullable=True)
    o1_comment = db.Column(db.String(1024), nullable=True)
    o2 = db.Column(db.Integer, nullable=True)
    o2_comment = db.Column(db.String(1024), nullable=True)
    t1 = db.Column(db.Integer, nullable=True)
    t1_comment = db.Column(db.String(1024), nullable=True)
    t2 = db.Column(db.Integer, nullable=True)
    t2_comment = db.Column(db.String(1024), nullable=True)
    p1 = db.Column(db.Integer, nullable=True)
    p1_comment = db.Column(db.String(1024), nullable=True)
    p2 = db.Column(db.Integer, nullable=True)
    p2_comment = db.Column(db.String(1024), nullable=True)

    verdict = db.Column(db.Integer, nullable=False, default=0)
    overall_comment = db.Column(db.String(1024), nullable=True)

    review_file_uri = db.Column(db.String(512), nullable=True)

class ThesisOnReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    type_id = db.Column(db.Integer, db.ForeignKey("worktype.id"), nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey("areas_of_study.id"), nullable=True)

    thesis_on_review_type_id = db.Column(
        db.Integer, db.ForeignKey("thesis_on_review_worktype.id"), nullable=True
    )

    name_ru = db.Column(db.String(512), nullable=False)

    text_uri = db.Column(db.String(512), nullable=True)
    presentation_uri = db.Column(db.String(512), nullable=True)
    source_uri = db.Column(db.String(512), nullable=True)

    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    reviewer_id = db.Column(db.Integer, db.ForeignKey("reviewer.id"), nullable=True)
    reviewer = db.relationship("Reviewer", back_populates="reviewer")

    supervisor_id = db.Column(db.Integer, db.ForeignKey("staff.id"), nullable=True)

    # 0 - success review (or not needed)
    # 1 - need to review
    # 2 - on review (in progress)
    # 3 - failed to review
    review_status = db.Column(db.Integer, nullable=True, default=10)
    review = db.relationship("ThesisReview", back_populates="thesis_on_review")

    # 0 - is active
    # 1 - not active
    deleted = db.Column(db.Integer, nullable=True, default=0)

class Reviewer(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("Users", back_populates="reviewer")

    company_id = db.Column(db.Integer, db.ForeignKey("company.id"), nullable=True)
    company = db.relationship("Company", back_populates="reviewer")

    reviewer = db.relationship("ThesisOnReview", back_populates="reviewer")

    def __str__(self):
        return self.user.get_name()

class Internships(db.Model):
    __tablename__ = "internships"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name_vacancy = db.Column(db.String(70), nullable=False)
    salary = db.Column(db.String(30), nullable=False)
    company = db.relationship("InternshipCompany", back_populates="internship")
    company_id = db.Column(db.Integer, db.ForeignKey("internship_company.id"))
    requirements = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    more_inf = db.Column(db.String, nullable=True)  # ссылка на сайт
    description = db.Column(
        db.String, nullable=True
    )  # короткое описание того, чем нужно будет заниматься
    location = db.Column(db.String(50), nullable=True)
    format = db.relationship(
        "InternshipFormat",
        secondary=internships_format,
        lazy="subquery",
        backref=db.backref("internship", lazy=True),
        order_by=internships_format.c.internships_format_id,
    )
    tag = db.relationship(
        "InternshipTag",
        secondary=internships_tag,
        lazy="subquery",
        backref=db.backref("internship", lazy=True),
        order_by=internships_tag.c.internships_tag_id,
    )

    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return self.name_vacancy

    def __self__(self):
        return self.name_vacancy

class ThemesLevel(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    level = db.Column(db.String(512), nullable=False)

    #    theme = db.relationship('DiplomaThemes', back_populates='level')
    #    themes_id = db.Column(db.Integer, db.ForeignKey('diploma_themes.id'))

    def __str__(self):
        return f"{self.level}"

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(512), nullable=False)
    logo_uri = db.Column(db.String(512), nullable=True)
    status = db.Column(db.Integer, default=0, nullable=True)

    theme = db.relationship("DiplomaThemes", back_populates="company")
    reviewer = db.relationship("Reviewer", back_populates="company")

    def __str__(self):
        return f"{self.name}"

class ThesisReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    current_thesis_id = db.Column(db.Integer, db.ForeignKey("current_thesis.id"))

    was_done = db.Column(db.String(2048), nullable=True)
    planned_to_do = db.Column(db.String(2048), nullable=True)
    time = db.Column(db.DateTime, default=datetime.utcnow)

    deleted = db.Column(db.Boolean, default=False)

    comment = db.Column(db.String(2048), nullable=True)
    comment_time = db.Column(db.DateTime, nullable=True)

    def __init__(self, was_done, planned_to_do, current_thesis_id, author_id):
        self.was_done = was_done
        self.planned_to_do = planned_to_do
        self.current_thesis_id = current_thesis_id
        self.author_id = author_id

class ThesisTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_text = db.Column(db.String(2048), nullable=False)
    deleted = db.Column(db.Boolean, default=False)
    current_thesis_id = db.Column(db.Integer, db.ForeignKey("current_thesis.id"))

    def __init__(self, task_text, current_thesis_id):
        self.task_text = task_text
        self.current_thesis_id = current_thesis_id

    def __repr__(self):
        return self.task_text

class InternshipCompany(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512), nullable=False)
    logo_uri = db.Column(db.String(512), nullable=True)
    internship = db.relationship("Internships", back_populates="company")

    def __str__(self):
        return self.name

class InternshipFormat(db.Model):
    __tablename__ = "internship_format"

    id = db.Column(db.Integer, primary_key=True)
    format = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return "{self.format}"

class InternshipTag(db.Model):
    __tablename__ = "internship_tag"

    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return self.tag

class NotificationPractice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipient_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    content = db.Column(db.String(512), nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    viewed = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, recipient_id, content):
        self.recipient_id = recipient_id
        self.content = content

    def __repr__(self):
        return self.content

class Deadline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    worktype_id = db.Column(db.Integer, db.ForeignKey("worktype.id"), nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey("areas_of_study.id"), nullable=False)

    choose_topic = db.Column(db.DateTime, nullable=True)
    submit_work_for_review = db.Column(db.DateTime, nullable=True)
    upload_reviews = db.Column(db.DateTime, nullable=True)

    pre_defense = db.Column(db.DateTime, nullable=True)
    defense = db.Column(db.DateTime, nullable=True)

class Worktype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255), nullable=False)

    thesis = db.relationship("Thesis", backref=db.backref("type", uselist=False))
    thesis_on_review = db.relationship(
        "ThesisOnReview", backref=db.backref("worktype", uselist=False)
    )
    current_thesis = db.relationship("CurrentThesis", backref=db.backref("worktype"))
    deadline = db.relationship(
        "Deadline", backref=db.backref("worktype", uselist=False)
    )

    def __repr__(self):
        return self.type

class ThesisOnReviewWorktype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255), nullable=False)

    thesis_on_review = db.relationship(
        "ThesisOnReview", backref=db.backref("thesis_on_review_worktype", uselist=False)
    )

    def __repr__(self):
        return self.type

class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(15), nullable=False)

    thesis = db.relationship("Thesis", backref=db.backref("course", uselist=False))
    curriculum = db.relationship(
        "Curriculum", backref=db.backref("course", uselist=False)
    )

    def __repr__(self):
        return "<%r>" % (self.name)

class AreasOfStudy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(512), nullable=False)

    current_thesis = db.relationship(
        "CurrentThesis", backref=db.backref("area", uselist=False)
    )
    thesis = db.relationship("Thesis", backref=db.backref("area", uselist=False))
    thesis_on_review = db.relationship(
        "ThesisOnReview", backref=db.backref("area", uselist=False)
    )

    def __repr__(self):
        return self.area

class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    tags = db.relationship(
        "Thesis", secondary=tag, lazy="subquery", backref=db.backref("tags", lazy=True)
    )

class Curriculum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    discipline = db.Column(db.String(256), nullable=False)
    study_year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1024), nullable=True)
    type = db.Column(db.Integer, nullable=False, default=1)

    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)

class PromoCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(512), nullable=False)

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # 0 - Mail
    type = db.Column(db.Integer, default=0, nullable=False)

    recipient = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(512), nullable=True)
    content = db.Column(db.String(8192), nullable=True)
