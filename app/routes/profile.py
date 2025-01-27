from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.models import User, Course, Achievement
from app.forms import ProfileForm

profile = Blueprint('profile', __name__)

@profile.route('/profile')
@login_required
def view():
    stats = {
        'completed_courses': current_user.get_completed_courses().count(),
        'average_grade': current_user.get_average_grade(),
        'achievements_count': current_user.achievements.count()
    }
    recent_activities = current_user.get_recent_activities()
    return render_template('profile/view.html', stats=stats, activities=recent_activities)

@profile.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = ProfileForm(obj=current_user)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.bio = form.bio.data
        if form.avatar.data:
            file = form.avatar.data
            current_user.avatar_url = save_avatar(file)
        db.session.commit()
        return redirect(url_for('profile.view'))
    return render_template('profile/edit.html', form=form)
