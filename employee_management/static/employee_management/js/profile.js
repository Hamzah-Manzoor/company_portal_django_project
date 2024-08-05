document.getElementById('profile-icon').addEventListener('click', function() {
    var menu = document.getElementById('profile-menu');
    if (menu.style.display === 'block') {
        menu.style.display = 'none';
    } else {
        menu.style.display = 'block';
    }
});

document.addEventListener('DOMContentLoaded', () => {
    const profileForm = document.getElementById('profile-form');

    profileForm.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent the form from submitting the default way

        const formData = new FormData(profileForm);
        const url = profileForm.getAttribute('action'); // Get the form's action URL
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                },
                body: formData,
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const result = await response.json();

            if (result.success) {
                displayMessage('Profile updated successfully!', 'success');
            } else {
                displayMessage('Error updating profile. Please try again.', 'error');
            }
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
            displayMessage('Error updating profile. Please try again.', 'error');
        }
    });

    function displayMessage(message, type) {
        const messagesContainer = document.querySelector('.messages');
        const messageItem = document.createElement('li');
        messageItem.textContent = message;
        messageItem.classList.add(type);
        messagesContainer.appendChild(messageItem);

        // Remove the message after a few seconds
        setTimeout(() => {
            messageItem.remove();
        }, 5000);
    }
});
