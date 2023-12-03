from src.extensions import db
from src.models import Users, Notification


def add_mail_notification(user_id, title, content):
    if not Users.query.filter_by(id=user_id).first():
        return

    n = Notification(recipient=user_id, title=title, content=content)
    db.session.add(n)
    db.session.commit()
