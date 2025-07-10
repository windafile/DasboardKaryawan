function hitung() {
    const lebar = parseInt(document.getElementById("inputLebar").value);
    const panjang = parseInt(document.getElementById("inputPanjang").value);
    const tinggi = parseInt(document.getElementById("inputTinggi").value);
    const hasil = document.getElementById("hasil");

    if (isNaN (lebar) || isNaN (panjang) || isNaN (tinggi)) {
        hasil.innerHTML = "Semua kolom wajib di isi!";
        return;
    }
    const volume = lebar * panjang * tinggi;
    hasil.innerHTML =`Hasil volume = ${volume}`;

}