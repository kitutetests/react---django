
document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.querySelector('.moon');

    // Function to update icon based on current mode
    function updateTheme() {
        const isDarkMode = localStorage.getItem('darkMode') === 'true';
        document.body.classList.toggle('dark-mode', isDarkMode);

        // Toggle between moon and sun icons
        const currentIcon = toggleButton.querySelector('i');
        if (isDarkMode) {
            currentIcon.classList.remove('fa-moon-o');
            currentIcon.classList.add('fa-sun-o');
        } else {
            currentIcon.classList.remove('fa-sun-o');
            currentIcon.classList.add('fa-moon-o');
        }
    }

    // Update theme based on user preference
    updateTheme();

    toggleButton.addEventListener('click', function() {
        // Toggle dark mode class on body
        document.body.classList.toggle('dark-mode');
        // Toggle dark mode value in localStorage
        const isDarkMode = document.body.classList.contains('dark-mode');
        localStorage.setItem('darkMode', isDarkMode);

        // Update icon based on mode
        updateTheme();
    });
});
