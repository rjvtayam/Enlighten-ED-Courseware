from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from app.models import Discussion, Reply
from app.forms import DiscussionForm, ReplyForm

discussion = Blueprint('discussion', __name__)

@discussion.route('/courses/<int:course_id>/discussions')
@login_required
def index(course_id):
    discussions = Discussion.query.filter_by(course_id=course_id).order_by(Discussion.created_at.desc()).all()
    return render_template('discussion/index.html', discussions=discussions)

@discussion.route('/discussions/<int:discussion_id>')
@login_required
def view(discussion_id):
    discussion = Discussion.query.get_or_404(discussion_id)
    form = ReplyForm()
    return render_template('discussion/view.html', discussion=discussion, form=form)

@discussion.route('/discussions/<int:discussion_id>/reply', methods=['POST'])
@login_required
def reply(discussion_id):
    form = ReplyForm()
    if form.validate_on_submit():
        reply = Reply(
            content=form.content.data,
            user_id=current_user.id,
            discussion_id=discussion_id
        )
        db.session.add(reply)
        db.session.commit()
        return jsonify({'success': True, 'reply': reply.to_dict()})
    return jsonify({'success': False, 'errors': form.errors}), 400
