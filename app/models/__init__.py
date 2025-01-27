from .user import User
from .course import Course
from .material import Material
from .assignment import Assignment
from .submission import Submission
from .discussion import Discussion, Reply

# This makes the models available directly from the models package
__all__ = ['User', 'Course', 'Material', 'Assignment', 'Submission', 'Discussion', 'Reply']
