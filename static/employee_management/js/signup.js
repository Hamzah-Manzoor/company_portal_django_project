document.getElementById('signup-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get form values
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;
    const joiningDate = document.getElementById('joining-date').value;
    const position = document.getElementById('position').value.trim();
    const employeeId = document.getElementById('employee-id').value.trim();
    const birthdate = document.getElementById('birthdate').value;

    // Validate passwords match
    if (password !== confirmPassword) {
        alert('Passwords do not match.');
        return;
    }

    // Simple form validation
    if (!email || !password || !confirmPassword || !joiningDate || !position || !employeeId || !birthdate) {
        alert('Please fill in all the fields.');
        return;
    }

    // Sign up process (for now, just log the data)
    console.log({
        email,
        password,
        joiningDate,
        position,
        employeeId,
        birthdate
    });

    alert('Sign up successful.');
});
