from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import Assignment, Submission
from app.forms import AssignmentForm, SubmissionForm

assignment = Blueprint('assignment', __name__)

@assignment.route('/assignments/<int:assignment_id>/submit', methods=['GET', 'POST'])
@login_required
def submit(assignment_id):
    assignment = Assignment.query.get_or_404(assignment_id)
    if assignment.is_past_due:
        flash('This assignment is past due.', 'error')
        return redirect(url_for('course.view', course_id=assignment.course_id))
    
    form = SubmissionForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        submission = Submission(
            student_id=current_user.id,
            assignment_id=assignment_id,
            file_path=filename
        )
        db.session.add(submission)
        db.session.commit()
        flash('Assignment submitted successfully!', 'success')
        return redirect(url_for('course.view', course_id=assignment.course_id))
    return render_template('assignment/submit.html', 
                         assignment=assignment, 
                         form=form)
