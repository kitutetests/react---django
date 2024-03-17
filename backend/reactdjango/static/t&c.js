document.addEventListener('DOMContentLoaded', function() {
    const termsLink = document.getElementById('terms-link');
    const termsPopup = document.getElementById('terms-popup');
    const closeTerms = document.getElementById('times');

    termsLink.addEventListener('click', function(event) {
        event.preventDefault();
        termsPopup.style.display = 'block';
    });

    closeTerms.addEventListener('click', function() {
        termsPopup.style.display = 'none';
    });
});