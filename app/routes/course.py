from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import Course, Material, Enrollment
from app.forms import CourseForm, MaterialForm

course = Blueprint('course', __name__)

@course.route('/courses/create', methods=['GET', 'POST'])
@login_required
def create():
    if current_user.role != 'teacher':
        flash('Access denied.', 'error')
        return redirect(url_for('main.dashboard'))
    
    form = CourseForm()
    if form.validate_on_submit():
        course = Course(
            title=form.title.data,
            description=form.description.data,
            teacher_id=current_user.id
        )
        db.session.add(course)
        db.session.commit()
        flash('Course created successfully!', 'success')
        return redirect(url_for('course.view', course_id=course.id))
    return render_template('course/create.html', form=form)

@course.route('/courses/<int:course_id>')
@login_required
def view(course_id):
    course = Course.query.get_or_404(course_id)
    is_enrolled = current_user.role == 'teacher' or \
                  Enrollment.query.filter_by(
                      student_id=current_user.id,
                      course_id=course_id
                  ).first() is not None
    
    if not is_enrolled:
        flash('Please enroll in the course to view its content.', 'error')
        return redirect(url_for('main.dashboard'))
    
    progress = course.get_progress(current_user.id) if current_user.role == 'student' else None
    return render_template('course/view.html', 
                         course=course, 
                         progress=progress)
