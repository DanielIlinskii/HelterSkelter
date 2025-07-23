
// Loading screen
window.addEventListener("load", function () {
    setTimeout(() => {
        const loadingScreen = document.getElementById("loadingScreen");
        loadingScreen.style.opacity = "0";
        setTimeout(() => {
            loadingScreen.style.display = "none";
        }, 500);
    }, 1500);
});

// Menu functionality
document.addEventListener("DOMContentLoaded", function () {
    // Navigation items
    const navItems = document.querySelectorAll(".nav-item");
    navItems.forEach((item) => {
        item.addEventListener("click", function () {
            navItems.forEach((i) => i.classList.remove("active"));
            this.classList.add("active");

            if (window.innerWidth <= 768) {
                toggleMobileMenu();
            }
        });
    });
});