//ini komentar, gak dibaca komputer
console.log("Halo Dari JavaScript!!!");

//script untuk narik dari HTML
const tombol = document.getElementById("tombol");

//tambahan aksi pas tombol di klik
tombol.addEventListener("click", function () {
    alert("SELAMAT BELAJAR JAVASCRIPT KAKA BOSS!!!");

});
// variable : tempat nyimpen data
let nama = "Kaka boss Toni";
let umur = 37;
const tgllahir = "04-05-1988";
let kota = "Bandung";
let hobi = "ngoding";
console.log("Nama Saya " + nama);
console.log("Umur Saya " + umur);
console.log("Hobi Saya " + hobi);
console.log("Kota Asal " + kota);
console.log("Kapan Kamu Lahir " + tgllahir);
//-------percabangan umur---------
let umursekarang = 28;

if (umur >= 17) {
    console.log("kamu udah gede buat bisa bikin KTP.");
} else {
    console.log("kamu belum cukup umur.");
}

//----js nilai-----
let nilaiujian = 85;

if (nilaiujian >= 90) {
    console.log("Nilai Kamu A");
} else if (nilaiujian >= 80) {
    console.log("Nilai Kamu B");
} else if (nilaiujian >= 70) {
    console.log("Nilai Kamu C");
} else if (nilaiujian >= 60) {
    console.log("Nilai Kamu D");
} else if (nilaiujian >= 50) {
    console.log("nilai Kamu E");
}

//----operator logika
let usia = 37;
let punyaKTP = true;

if (usia >=17 && punyaKTP) {
    console.log("kamu bisa daftar bukin SIM");
}
//----(or) salah satu data cukup
let adaKTP = false;
let adaSIM = true;

if (adaKTP || adaSIM) {
    console.log("kamu bisa verifikasi akun.");
}
//----(not) kebalikannya
let bayar = false;

if (!bayar) {
    console.log("Bayar dulu dong!!!");
}
//---latihan
let username = "kakaboss"
let password = "qwerty"

if (username === "kakaboss" && password === "qwerty") {
    console.log("Login Berhasil, SELAMAT DATANG");
} else {
    console.log("Periksa kembali username dan pasworrd anda");
}
