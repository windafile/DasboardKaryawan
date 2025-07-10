console.log("ini dari register2.js")
let nama = "Toni";
let umur = 37;
const kota = "Bandung";

console.log("Nama Saya:", nama);
console.log("Umur Saya:", umur);
console.log("Kota Asal:", kota);

//operator aritmatika
console.log("Cek umur sekarang:", umur);
let tahunLahir = 2025 - umur;
let isOnline = true;
console.log("nama:", nama);
console.log("umur:", umur);
console.log("Tahun Lahir:",tahunLahir);

//operator perbandingan
console.log("Umur Lebih Dari 17?", umur > 17);
console.log("Nama Adalah String?", typeof nama === "string");

//operator logika
let bolehMasuk = umur > 17 && isOnline;
console.log("Boleh Masuk?", bolehMasuk);

// if elese

if (umur >= 17) {
    console.log("boleh buat SIM");
} else {
    console.log("belum cukup umur buat SIM");
}