// Course-related functionality
class CourseManager {
    constructor() {
        this.initializeEventListeners();
    }

    initializeEventListeners() {
        // Handle material completion
        document.querySelectorAll('.complete-material').forEach(button => {
            button.addEventListener('click', this.handleMaterialCompletion.bind(this));
        });

        // Handle course enrollment
        const enrollButton = document.querySelector('.enroll-button');
        if (enrollButton) {
            enrollButton.addEventListener('click', this.handleEnrollment.bind(this));
        }
    }

    async handleMaterialCompletion(event) {
        const materialId = event.target.dataset.materialId;
        try {
            const response = await fetch(`/api/materials/${materialId}/complete`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
            });
            const data = await response.json();
            
            if (data.success) {
                this.updateProgressBar(data.progress);
                event.target.classList.add('completed');
            }
        } catch (error) {
            console.error('Error completing material:', error);
        }
    }

    async handleEnrollment(event) {
        const courseId = event.target.dataset.courseId;
        try {
            const response = await fetch(`/api/courses/${courseId}/enroll`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
            });
            const data = await response.json();
            
            if (data.success) {
                window.location.reload();
            }
        } catch (error) {
            console.error('Error enrolling in course:', error);
        }
    }

    updateProgressBar(progress) {
        const progressBar = document.querySelector('.progress-bar');
        const progressText = document.querySelector('.progress-text');
        
        if (progressBar && progressText) {
            progressBar.style.width = `${progress}%`;
            progressText.textContent = `${progress}% Complete`;
        }
    }
}

// Initialize course manager
document.addEventListener('DOMContentLoaded', () => {
    new CourseManager();
});
