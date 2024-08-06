// Profile menu toggle
document.getElementById('profile-icon').addEventListener('click', function() {
    var menu = document.getElementById('profile-menu');
    if (menu.style.display === 'block') {
        menu.style.display = 'none';
    } else {
        menu.style.display = 'block';
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const editButtons = document.querySelectorAll('.btn-success');
    const modals = document.querySelectorAll('.modal');
    const closeModalButtons = document.querySelectorAll('.modal .close');

    // Open edit modals
    editButtons.forEach(button => {
        console.log("------------------------------------------------------------------------------------------")
        button.addEventListener('click', function () {
            console.log("------------------------------------------------------------------------------------------")
            const modalId = this.getAttribute('data-modal-id');
            if (!modalId) {
                console.error('data-modal-id attribute is missing on this button:', this);
                return;
            }
            const modal = document.getElementById(modalId);
            if (modal) {
                modal.style.display = 'block';
            } else {
                console.error('Modal not found for ID:', modalId);
            }
        });
    });

    // Close modals
    closeModalButtons.forEach(button => {
        button.addEventListener('click', function () {
            this.closest('.modal').style.display = 'none';
        });
    });

    // Close modals when clicking outside of modal content
    window.addEventListener('click', function (event) {
        modals.forEach(modal => {
            if (event.target === modal) {
                modal.style.display = 'none';
            }
        });
    });
});

