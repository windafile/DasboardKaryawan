document.getElementById("registerForm").addEventListener("submit", function (e) {
    e.preventDefault(); // Biar ga reload

    const username = document.getElementById("regusername").value.trim();
    const password = document.getElementById("regpassword").value.trim();
    const password2 = document.getElementById("regpassword2").value.trim();
    const email = document.getElementById("regemail").value.trim();
    const email2 = document.getElementById("regemail2").value.trim();
    const pesan = document.getElementById("pesan");

    // Validasi kosong
    if (!username || !password || !password2 || !email || !email2) {
        pesan.textContent = "Semua kolom wajib diisi.";
        pesan.style.color = "red";
        return;
    }

    // Validasi email
    if (!email.includes("@") || !email.includes(".")) {
        pesan.textContent = "Email tidak valid.";
        pesan.style.color = "orange";
        return;
    }

    if (email !== email2) {
        pesan.textContent = "Email tidak cocok.";
        pesan.style.color = "orange";
        return;
    }

    // Validasi password
    if (password !== password2) {
        pesan.textContent = "Password tidak cocok.";
        pesan.style.color = "orange";
        return;
    }

    if (password.length < 5) {
        pesan.textContent = "Password minimal 5 karakter.";
        pesan.style.color = "orange";
        return;
    }

    // Simpan ke localStorage
    const dataUser = { username, password, email };
    localStorage.setItem("dataUser", JSON.stringify(dataUser));

    pesan.textContent = "Registrasi Berhasil! Akun siap digunakan.";
    pesan.style.color = "green";
});
