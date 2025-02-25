function validateForm() {
  const username = document.getElementById("username").value.trim();
  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value.trim();

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const passwordRegex =
    /^(?=.*[!@#$%^&*(),.?":{}|<>])(?=.*\d)(?=.*[a-z])(?=.*[A-Z])/;

  let valid = true;

  clearErrors();

  if (username.length === 0) {
    showError("usernameError", "Username is required.");
    valid = false;
  }

  if (username.length < 3) {
    showError("usernameError", "Username must be at least 3 characters long.");
    valid = false;
  }

  if (!emailRegex.test(email)) {
    showError("emailError", "Invalid email format.");
    valid = false;
  }

  if (password.length < 8) {
    showError("passwordError", "Password must be at least 8 characters long.");
    valid = false;
  } else if (!passwordRegex.test(password)) {
    showError(
      "passwordError",
      "Password must contain at least one special character, one digit, one uppercase letter, and one lowercase letter.",
    );
    valid = false;
  }

  if (!phoneRegex.test(phoneNumber)) {
    showError("phoneNumberError", "Phone number must start with 98 or 97 and be exactly 10 digits long.");
    valid = false;
  }

  return valid;
}

function clearErrors() {
  document.getElementById("usernameError").textContent = "";
  document.getElementById("emailError").textContent = "";
  document.getElementById("passwordError").textContent = "";
  document.getElementById("phoneNumberError").textContent = "";
}

function showError(elementId, message) {
  document.getElementById(elementId).textContent = message;
}
