function gantiWarna() {
    const kode = Math.floor(Math.random() * 16777215).toString(16).padStart(6, "0");
    const warna = `#${kode}`;


document.body.style.backgroundColor = warna;
document.getElementById("kodeWarna").textContent = `Warna Sekarang ${warna}`;
}