// Show popup after 3 seconds
window.addEventListener("load", function() {
    setTimeout(function() {
        document.getElementById("newsletter-popup").style.display = "flex";
    }, 3000);
});

// Close popup
document.addEventListener("DOMContentLoaded", function() {
    const closeBtn = document.getElementById("close-popup");
    const popup = document.getElementById("newsletter-popup");

    closeBtn.addEventListener("click", function() {
        popup.style.display = "none";
    });

    // Optional: close when clicking outside popup
    window.addEventListener("click", function(e) {
        if (e.target === popup) {
            popup.style.display = "none";
        }
    });
});
