// Main JavaScript functionality
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    const tooltips = document.querySelectorAll('[data-tooltip]');
    tooltips.forEach(tooltip => {
        tippy(tooltip, {
            content: tooltip.getAttribute('data-tooltip'),
            placement: 'top',
        });
    });

    // Handle notifications
    const notificationBell = document.getElementById('notification-bell');
    if (notificationBell) {
        const socket = io();
        
        socket.on('connect', () => {
            socket.emit('join', { room: `user_${currentUserId}` });
        });

        socket.on('new_notification', (data) => {
            updateNotificationCount(data.count);
            showNotificationToast(data.message);
        });
    }
});

// Notification handling
function updateNotificationCount(count) {
    const badge = document.querySelector('.notification-badge');
    if (badge) {
        badge.textContent = count;
        badge.classList.toggle('hidden', count === 0);
    }
}

function showNotificationToast(message) {
    Toastify({
        text: message,
        duration: 3000,
        gravity: "top",
        position: "right",
        backgroundColor: "#4F46E5",
    }).showToast();
}
