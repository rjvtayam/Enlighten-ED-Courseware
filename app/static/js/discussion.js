// Discussion forum functionality
class DiscussionManager {
    constructor() {
        this.initializeEditor();
        this.initializeEventListeners();
    }

    initializeEditor() {
        const editors = document.querySelectorAll('.markdown-editor');
        editors.forEach(editor => {
            new EasyMDE({
                element: editor,
                spellChecker: false,
                status: false,
                toolbar: ['bold', 'italic', 'heading', '|', 'quote', 'unordered-list', 'ordered-list', '|', 'link', 'image', '|', 'preview'],
            });
        });
    }

    initializeEventListeners() {
        // Handle reply form submissions
        document.querySelectorAll('.reply-form').forEach(form => {
            form.addEventListener('submit', this.handleReplySubmission.bind(this));
        });

        // Handle topic creation
        const createTopicForm = document.querySelector('#create-topic-form');
        if (createTopicForm) {
            createTopicForm.addEventListener('submit', this.handleTopicCreation.bind(this));
        }
    }

    async handleReplySubmission(event) {
        event.preventDefault();
        const form = event.target;
        const formData = new FormData(form);

        try {
            const response = await fetch(form.action, {
                method: 'POST',
                body: formData,
            });
            const data = await response.json();
            
            if (data.success) {
                this.addReplyToDiscussion(data.reply);
                form.reset();
            }
        } catch (error) {
            console.error('Error submitting reply:', error);
        }
    }

    async handleTopicCreation(event) {
        event.preventDefault();
        const form = event.target;
        const formData = new FormData(form);

        try {
            const response = await fetch(form.action, {
                method: 'POST',
                body: formData,
            });
            const data = await response.json();
            
            if (data.success) {
                window.location.href = data.redirect_url;
            }
        } catch (error) {
            console.error('Error creating topic:', error);
        }
    }

    addReplyToDiscussion(reply) {
        const repliesContainer = document.querySelector('.replies-container');
        const replyTemplate = `
            <div class="reply-item">
                <div class="reply-header">
                    <img src="${reply.author.avatar_url}" class="avatar">
                    <span class="author">${reply.author.username}</span>
                    <span class="timestamp">${reply.created_at}</span>
                </div>
                <div class="reply-content">
                    ${reply.content}
                </div>
            </div>
        `;
        repliesContainer.insertAdjacentHTML('beforeend', replyTemplate);
    }
}

// Initialize discussion manager
document.addEventListener('DOMContentLoaded', () => {
    new DiscussionManager();
});
