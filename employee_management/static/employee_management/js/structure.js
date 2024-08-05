document.addEventListener('DOMContentLoaded', function() {
    // Load header
    fetch('header.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('header').innerHTML = data;
        })
        .catch(error => console.error('Error loading header:', error));

    // Load footer
    fetch('footer.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('footer').innerHTML = data;
        })
        .catch(error => console.error('Error loading footer:', error));

    // Load specific page content
    // const urlParams = new URLSearchParams(window.location.search);
    // const page = urlParams.get('page') || 'index.html';
    // fetch(page)
    //     .then(response => response.text())
    //     .then(data => {
    //         document.getElementById('content').innerHTML = data;
    //     })
    //     .catch(error => console.error('Error loading content:', error));
});
