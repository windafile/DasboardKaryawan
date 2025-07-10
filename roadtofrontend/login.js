document.getElementById("loginBtn").addEventListener("click", function () {
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();
    const pesan = document.getElementById("pesan");

    if (username === "" || password === "") {
        pesan.textContent = "Isi dulu lah kocak!!!.";
        pesan.style.color = "red";
    } else if (username === "kakaboss" && password === "qwerty") {
        pesan.textContent = "Selamat datang bro sis";
        pesan.style.color = "lightgreen";
    } else {
        pesan.textContent = "Mau Ngapain Lu Login, signUp dulu kocak!!!";
        pesan.style.color = "orange";
    }
});