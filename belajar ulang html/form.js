function cekForm() {
    const nama = document.getElementById("nama").value.trim();
    const email = document.getElementById("email").value.trim();
    const umur = parseInt(document.getElementById("umur").value);
     // pasrseInt fungsinya untuk mengubah string menjadi integer (angka)
    
    const hasil = document.getElementById("hasil");
    hasil.innerHTML = "";
    if (nama === ""||
        email === ""||
        isNaN(umur)) {
        hasil.innerHTML = `<p style="color:red;">Semua Kolom Harus Di Isi Dengan Benar!</p>`;
        return;
    }
    if (umur < 17) {
        hasil.innerHTML = `<p style="color:red;">Maaf ${nama}, Umur Kamu Belum Cukup Untuk Mendaftar SIM!</p>`;
        return;
    }
        hasil.innerHTML = `<p style="color:green;">Hore ${nama}, Email Kamu ${email} dan Umur kamu ${umur} tahun, Layak Membuat SIM</p>`;
}