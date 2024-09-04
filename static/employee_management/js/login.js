document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get form values
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Simple form validation
    if (!email || !password) {
        alert('Please fill in both fields.');
        return;
    }

    // Login process (for now, just log the data)
    console.log({
        email,
        password
    });

    alert('Login successful.');
});
