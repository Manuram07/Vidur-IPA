function validateForm() {
    let name = document.getElementById("name");
    let email = document.getElementById("email");
    let password = document.getElementById("password");
    let confirmPassword = document.getElementById("confirmPassword");
    let isValid = true;

    document.querySelectorAll(".error").forEach(e => e.innerText = "");

    if (name.value.trim() === "") {
        setError(name, "Please enter your full name");
        isValid = false;
    }

    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (!email.value.match(emailPattern)) {
        setError(email, "Enter a valid email address");
        isValid = false;
    }

    if (password.value.length < 6) {
        setError(password, "Password must be at least 6 characters long");
        isValid = false;
    }

    if (confirmPassword.value !== password.value) {
        setError(confirmPassword, "Passwords do not match");
        isValid = false;
    }

    if (isValid) {
        alert("🎉 Registration Successful!");
    }

    return isValid;
}

function setError(input, message) {
    const formControl = input.parentElement;
    const errorMsg = formControl.querySelector(".error");
    errorMsg.innerText = message;
}
