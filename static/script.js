
const contactForm = document.getElementById("contactForm");

if (contactForm) {
    contactForm.addEventListener("submit", async function (event) {
        event.preventDefault();

        const nameInput = document.getElementById("name");
        const messageInput = document.getElementById("message");
       const result = document.getElementById("response");
        const name = nameInput.value.trim();
        const message = messageInput.value.trim();

        // Validate empty fields
        if (!name || !message) {
            result.textContent = "Please enter both name and message.";
            return;
        }

        // Validate name length
        if (name.length > 50) {
            result.textContent = "Name must be 50 characters or fewer.";
            return;
        }

        // Validate message length
        if (message.length > 500) {
            result.textContent = "Message must be 500 characters or fewer.";
            return;
        }

        try {
            const response = await fetch("/api/contact", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    name: name,
                    message: message
                })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || "Something went wrong.");
            }

            result.textContent = data.message;
            contactForm.reset();

        } catch (error) {
            result.textContent = error.message;
        }
    });
}
