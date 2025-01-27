from functools import wraps
from flask import abort
from flask_login import current_user

def teacher_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'teacher':
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

def course_access_required(f):
    @wraps(f)
    def decorated_function(course_id, *args, **kwargs):
        course = Course.query.get_or_404(course_id)
        if not current_user.has_access_to_course(course):
            abort(403)
        return f(course_id, *args, **kwargs)
    return decorated_function
