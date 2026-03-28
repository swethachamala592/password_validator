async function checkPassword() {
    const password = document.getElementById("password").value;

    try {
        const response = await fetch("http://127.0.0.1:5000/validate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ password: password })
        });

        const data = await response.json();

        document.getElementById("result").innerText =
            data.is_valid ? "✅ Valid Password" : "❌ Invalid Password";

    } catch (error) {
        console.error("Error:", error);
        document.getElementById("result").innerText = "❌ Server error!";
    }
}