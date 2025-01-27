from app import db
from datetime import datetime

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    teacher_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    materials = db.relationship('Material', backref='course', lazy='dynamic')
    assignments = db.relationship('Assignment', backref='course', lazy='dynamic')
    enrollments = db.relationship('Enrollment', backref='course', lazy='dynamic')
    
    def get_progress(self, student_id):
        completed = Progress.query.filter_by(
            student_id=student_id,
            course_id=self.id,
            completed=True
        ).count()
        total = self.materials.count()
        return (completed / total * 100) if total > 0 else 0
