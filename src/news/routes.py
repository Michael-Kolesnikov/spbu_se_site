import textile
from src.news import bp
from flask import redirect, render_template, url_for, flash, request
from src.models import Posts, PostVote, post_ranking_score
from src.extensions import db
from urllib.parse import urlparse
from flask_login import current_user, login_required
from src.date_formatting import plural_hours, get_hours_since


def list_news():
    page = request.args.get("page", default=1, type=int)
    ages = []

    news = Posts.query.order_by(Posts.rank.desc()).paginate(
        per_page=20, page=page, error_out=False
    )

    for post in news.items:
        ages.append(plural_hours(int(get_hours_since(post.created_on))))

    return render_template("news/news.html", news=news, ages=ages)


bp.add_url_rule("/news/", view_func=list_news)
bp.add_url_rule("/news/index.html", view_func=list_news)


@bp.route("/news/item.html")
def get_post():
    post_id = request.args.get("post", type=int)

    if not post_id:
        return redirect(url_for("news.list_news"))

    post = Posts.query.filter_by(id=post_id).first_or_404()

    post.views = post.views + 1

    # Recalculate rank
    age = get_hours_since(post.created_on)
    post.rank = post_ranking_score(post.votes, age, post.views)
    db.session.commit()

    if post.uri:
        return redirect(post.uri)

    return render_template("news/post.html", post=post)


@bp.route("/news/submit.html", methods=["GET", "POST"])
@login_required
def submit_post():
    if request.method == "POST":
        title = request.form.get("title")
        post_uri = request.form.get("post_uri")
        post_text = request.form.get("post_text")

        if not title:
            flash("Заголовок у новости обязательное поле.")
            return render_template("news/submit.html")

        if not post_uri and not post_text:
            flash("У новости должна быть ссылка или текст")
            return render_template("news/submit.html")

        if post_uri:
            domain = urlparse(post_uri).netloc
            post = Posts(
                title=title, uri=post_uri, domain=domain, author_id=current_user.id
            )
        else:
            formated_text = textile.textile(post_text)
            post = Posts(title=title, text=formated_text, author_id=current_user.id)

        db.session.add(post)
        db.session.commit()

        return redirect(url_for("news.list_news"))

    return render_template("news/submit.html")


@bp.route("/news/post_vote", methods=["GET", "POST"])
@login_required
def post_vote():
    post_id = request.args.get("post_id", type=int)
    action_vote = request.args.get("action_vote", type=int)

    if not post_id:
        return render_template(url_for("general.index"))

    post = Posts.query.filter_by(id=post_id).first_or_404()

    if post.author.id == current_user.id:
        flash("Нельзя голосовать за свой пост!", category="error")
        return redirect(request.referrer)

    vote = PostVote.query.filter_by(user=current_user, post=post).first()

    if vote:
        if vote.upvote != bool(int(action_vote)):
            vote.upvote = bool(int(action_vote))

            if action_vote:
                post.votes = post.votes + 1
            else:
                post.votes = post.votes - 1

            # Recalculate rank
            age = get_hours_since(post.created_on)
            post.rank = post_ranking_score(post.votes, age, post.views)
            db.session.commit()

            return redirect(request.referrer)
        else:
            flash("Вы уже проголосовали за этот пост!", category="error")
            return redirect(request.referrer)

    vote = PostVote(user=current_user, post=post, upvote=bool(int(action_vote)))

    if action_vote:
        post.votes = post.votes + 1
    else:
        post.votes = post.votes - 1

    # Recalculate rank
    age = get_hours_since(post.created_on)
    post.rank = post_ranking_score(post.votes, age, post.views)

    db.session.add(vote)
    db.session.commit()
    return redirect(request.referrer)


@bp.route("/news/delete")
@login_required
def delete_post():
    post_id = request.args.get("post_id", type=int)

    if not post_id:
        return redirect(url_for("news.list_news"))

    post = Posts.query.filter_by(id=post_id).first_or_404()

    if post.author.id != current_user.id:
        return redirect(url_for("news.get_post", post=post_id))

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for("news.list_news"))
