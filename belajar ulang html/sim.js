function cekSim() {
    const umur = parseInt(document.getElementById("inputUmur").value);
    const hasil =document.getElementById("hasil");

    if (isNaN(umur)) {
        hasil.innerHTML = "Masukan Angka Untuk Mengatahui Kamu Layak Atau Tidak";
        return;
    }
    if (umur >= 17) {
        hasil.innerHTML= "Kamu boleh buat SIM!!!";
    } else {
        hasil.innerHTML= "kamu belum layak dan pantas mendapat SIM";

    }

}