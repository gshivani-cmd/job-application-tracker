
document.addEventListener("DOMContentLoaded", () => {
    const savedTheme = localStorage.getItem("job-tracker-theme");

    if (savedTheme === "dark") {
        document.body.classList.add("dark-mode");
    }

    const themeButton = document.createElement("button");
    themeButton.id = "theme-toggle";
    themeButton.type = "button";
    themeButton.setAttribute("aria-label", "Toggle dark mode");
    document.body.appendChild(themeButton);

    function updateThemeButton() {
        const isDark = document.body.classList.contains("dark-mode");
        themeButton.textContent = isDark ? "☀️ Light mode" : "🌙 Dark mode";
    }

    updateThemeButton();

    themeButton.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");

        const isDark = document.body.classList.contains("dark-mode");

        localStorage.setItem(
            "job-tracker-theme",
            isDark ? "dark" : "light"
        );

        updateThemeButton();
    });

    // Hide flash notifications after 4 seconds.
    document.querySelectorAll(".flash, .message").forEach((message) => {
        setTimeout(() => {
            message.style.transition = "opacity 0.4s";
            message.style.opacity = "0";

            setTimeout(() => message.remove(), 400);
        }, 4000);
    });
});
