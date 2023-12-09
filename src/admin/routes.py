from src import admin, db
from src.models import (
    Users,
    Staff,
    Thesis,
    SummerSchool,
    Posts,
    DiplomaThemes,
    CurrentThesis,
)
from src.admin.views import (
    SeAdminModelViewUsers,
    SeAdminModelViewStaff,
    SeAdminModelViewThesis,
    SeAdminModelViewSummerSchool,
    SeAdminModelViewNews,
    SeAdminModelViewDiplomaThemes,
    SeAdminModelViewReviewDiplomaThemes,
    SeAdminModelViewCurrentThesis,
)

admin.add_view(SeAdminModelViewUsers(Users, db.session))
admin.add_view(SeAdminModelViewStaff(Staff, db.session))
admin.add_view(SeAdminModelViewThesis(Thesis, db.session))
admin.add_view(SeAdminModelViewSummerSchool(SummerSchool, db.session))
admin.add_view(SeAdminModelViewNews(Posts, db.session))
admin.add_view(
    SeAdminModelViewDiplomaThemes(DiplomaThemes, db.session, endpoint="diplomathemes")
)
admin.add_view(
    SeAdminModelViewReviewDiplomaThemes(
        DiplomaThemes,
        db.session,
        endpoint="reviewdiplomathemes",
        name="Review DiplomaThemes",
    )
)
admin.add_view(SeAdminModelViewCurrentThesis(CurrentThesis, db.session))
