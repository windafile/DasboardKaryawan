// Materi: JavaScript Dasar (Bagian 1)

// 1. Menampilkan teks ke browser (console dan halaman)
console.log("Halo Dunia!");

// 2. Variabel
let nama = "Toni";
const umur = 37;

// 3. Tipe data
let angka = 10; // Number
let teks = "Belajar JS"; // String
let benar = true; // Boolean

// 4. Operasi dasar
let hasilTambah = 5 + 3;
let hasilKali = 4 * 2;
let hasilGabung = "Halo " + nama;

// 5. Alert dan Prompt (buka di browser)
// alert("Ini alert");
// let inputNama = prompt("Siapa nama kamu?");
// alert("Halo " + inputNama);

// 6. Fungsi
function sapa(namaUser) {
  return "Halo, " + namaUser + "!";
}
console.log(sapa("Boss Toni"));

// 7. Kondisi IF
let nilai = 85;
if (nilai >= 80) {
  console.log("Nilai bagus!");
} else {
  console.log("Perlu belajar lebih giat");
}

// 8. Perulangan FOR
for (let i = 1; i <= 5; i++) {
  console.log("Perulangan ke-" + i);
}
function togglePassword() {
  const pwInput = document.getElementById("password");
  pwInput.type = pwInput.type === "password" ? "text" : "password";
}
function kirimData() {
  const nama = document.getElementById("nama").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const hasil = document.getElementById("hasil");
  hasil.innerHTML = `
    <div style="background-color: #d4edda; padding: 15px; border-radius: 8px; border: 1px solid #c3e6cb;">
      <p><strong>Nama:</strong> ${nama}</p>
      <p><strong>Email:</strong> ${email}</p>
      <p><strong>Password:</strong> ${password}</p>
    </div>
  `;
}