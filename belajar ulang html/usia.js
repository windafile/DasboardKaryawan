function cekKategori() {
    const umur = parseInt(document.getElementById("inputUmur").value);
    const hasil = document.getElementById("hasil");


if (isNaN(umur)) {
    hasil.innerHTML = "Isi kolom dengan usia kamu";
    return;
}

if (umur < 5) {
    hasil.innerHTML = "masih Balita";
} else if (umur < 13) {
    hasil.innerHTML = "masih Anaka-anak";
} else if  (umur < 18) {
    hasil.innerHTML = "masih Remaja";
} else if (umur < 30) { 
    hasil.innerHTML = "sudah Dewasa";
} else {
    hasil.innerHTML = "kamu TUA BANGKA";
}
}