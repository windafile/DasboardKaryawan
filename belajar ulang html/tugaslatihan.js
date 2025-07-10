
function cekNilai() {
const nama = document.getElementById("nama").value;
const nilai = parseInt(document.getElementById("nilai").value);
const hasil = document.getElementById("hasil");

if (nama === "" || isNaN(nilai)) {
    hasil.innerHTML= "Masukan nama dan nilai kamu";
    return;
}
if (nilai <0 || nilai >100) {
    hasil.innerHTML = "Input Tidak Valid, Isi Denagn Angka 0-100";
    return;
}
if (nilai < 45) {
    hasil.innerHTML= `Maaf ${nama}, Kamu tidak LULUS!`;
} else if (nilai < 65) {
    hasil.innerHTML= `Mantap ${nama}, Kamu lulus dengan Nilai yang cukup`;
} else if (nilai < 75) {
    hasil.innerHTML= `Oke ${nama}, kamu lulus dengan Nilai yang bagus`;
} else {
    hasil.innerHTML= `LUAR BIASA ${nama}, Kamu LULUSAN TERBAIK TAHUN INI`;
}
}