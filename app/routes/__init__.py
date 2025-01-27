from .auth import auth
from .course import course
from .assignment import assignment
from .discussion import discussion
from .profile import profile

# This makes the blueprints available directly from the routes package
__all__ = ['auth', 'course', 'assignment', 'discussion', 'profile']
