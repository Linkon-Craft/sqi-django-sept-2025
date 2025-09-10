document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("searchInput");
    const products = document.querySelectorAll(".pro");

    searchInput.addEventListener("keyup", () => {
        const query = searchInput.value.toLowerCase();

        products.forEach(product => {
            const title = product.querySelector("h3").textContent.toLowerCase();
            if (title.includes(query)) {
                product.style.display = "block";
            } else {
                product.style.display = "none";
            }
        });
    });
});
