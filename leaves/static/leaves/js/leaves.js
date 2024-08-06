document.getElementById('profile-icon').addEventListener('click', function() {
    var menu = document.getElementById('profile-menu');
    if (menu.style.display === 'block') {
        menu.style.display = 'none';
    } else {
        menu.style.display = 'block';
    }
});

document.getElementById('leave-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Simple form validation
    const employeeName = document.getElementById('employee-name').value.trim();
    const employeeId = document.getElementById('employee-id').value.trim();
    const leaveType = document.getElementById('leave-type').value;
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;
    const reason = document.getElementById('reason').value.trim();

    if (!employeeName || !employeeId || !leaveType || !startDate || !endDate || !reason) {
        alert('Please fill in all the fields.');
        return;
    }

    if (new Date(startDate) > new Date(endDate)) {
        alert('Start date cannot be later than end date.');
        return;
    }

    // Submit form (for now, just log the data)
    console.log({
        employeeName,
        employeeId,
        leaveType,
        startDate,
        endDate,
        reason
    });

    alert('Leave application submitted successfully.');
});
