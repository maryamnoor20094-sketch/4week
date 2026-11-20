
const form = document.getElementById("contactForm");
const responseMessage = document.getElementById("response");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const message = document.getElementById("message").value.trim();

    if (!name || !message) {
        responseMessage.textContent = "Please complete all fields.";
        return;
    }

    try {
        const response = await fetch("/api/contact", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ name, message })
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.error || "Submission failed.");
        }

        responseMessage.textContent = result.message;
        form.reset();

    } catch (error) {
        responseMessage.textContent = error.message;
    }
});
