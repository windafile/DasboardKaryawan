const toggleBtn = document.getElementById("togelPassword");
const passwordInput = document.getElementById("password");

toggleBtn.addEventListener("click", () => {
  const isPassword = passwordInput.getAttribute("type") === "password";
  passwordInput.setAttribute("type", isPassword ? "text" : "password");
  toggleBtn.textContent = isPassword ? "👁️" : "🔒";
});

function showError(inputId, message) {
  const input = document.getElementById(inputId);
  const wrapper = input.closest(".form-group");
  const small = wrapper.querySelector(".error-message");
  small.textContent = message;
  small.style.display = "block";
}

function resetErrorMessage() {
  const errors = document.querySelectorAll(".error-message");
  errors.forEach((error) => {
    error.textContent = "";
    error.style.display = "none";
  });
}

document.getElementById("formRegister").addEventListener("submit", function (event) {
  resetErrorMessage();

  const nama = document.getElementById("nama").value.trim();
  const email = document.getElementById("email").value.trim();
  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();

  let isValid = true;

  if (nama === "") {
    showError("nama", "Nama tidak boleh kosong");
    isValid = false;
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    showError("email", "Format email tidak valid");
    isValid = false;
  }

  if (username.length < 4) {
    showError("username", "Username minimal 4 karakter");
    isValid = false;
  }

  if (password.length < 5) {
    showError("password", "Password terlalu lemah (min 5 karakter)");
    isValid = false;
  }

  if (!isValid) {
    event.preventDefault();
  }
});

// isPassword adalah sebuah variable boolean (isinya cuma true atau false) 
// yang dipakai untuk cek apakah input password sedang di sembunyian atau tidak