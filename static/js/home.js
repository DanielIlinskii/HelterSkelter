
// Loading screen
window.addEventListener("load", function () {
    setTimeout(() => {
        const loadingScreen = document.getElementById("loadingScreen");
        loadingScreen.style.opacity = "0";
        setTimeout(() => {
            loadingScreen.style.display = "none";
        }, 500);
    }, 2000);
});

// Menu functionality
document.addEventListener("DOMContentLoaded", function () {

    // Task checkboxes
    const taskCheckboxes = document.querySelectorAll(
        ".task-checkbox input"
    );
    taskCheckboxes.forEach((checkbox) => {
        checkbox.addEventListener("change", function () {
            const taskItem = this.closest(".task-item");
            if (this.checked) {
                taskItem.style.opacity = "0.6";
                taskItem.querySelector(".task-title").style.textDecoration =
                    "line-through";
            } else {
                taskItem.style.opacity = "1";
                taskItem.querySelector(".task-title").style.textDecoration =
                    "none";
            }
        });
    });

    // Floating Action Button
    const fab = document.querySelector(".fab");
    fab.addEventListener("click", function () {
        this.style.transform = "translateY(-5px) scale(1.2) rotate(45deg)";
        setTimeout(() => {
            this.style.transform = "translateY(-5px) scale(1.1)";
        }, 200);
    });

    // Hover effects for cards
    const cards = document.querySelectorAll(".stat-card, .client-card");
    cards.forEach((card) => {
        card.addEventListener("mouseenter", function () {
            this.style.transform = "translateY(-10px) scale(1.02)";
        });

        card.addEventListener("mouseleave", function () {
            this.style.transform = "translateY(0) scale(1)";
        });
    });
});

// Mobile menu toggle
function toggleMobileMenu() {
    const sidebar = document.getElementById("sidebar");
    const overlay = document.getElementById("mobileOverlay");

    sidebar.classList.toggle("active");

    if (sidebar.classList.contains("active")) {
        overlay.style.display = "block";
        document.body.style.overflow = "hidden";
    } else {
        overlay.style.display = "none";
        document.body.style.overflow = "auto";
    }
}

// Smooth scroll for section actions
document.querySelectorAll(".section-action").forEach((action) => {
    action.addEventListener("click", function () {
        this.style.transform = "translateY(-3px)";
        setTimeout(() => {
            this.style.transform = "translateY(0)";
        }, 200);
    });
});

// Search functionality
const searchInput = document.querySelector(".search-bar input");
searchInput.addEventListener("focus", function () {
    this.parentElement.style.transform = "scale(1.02)";
});

searchInput.addEventListener("blur", function () {
    this.parentElement.style.transform = "scale(1)";
});


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

