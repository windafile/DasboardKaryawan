let jumlahklik = 0;

function hitungklik() {
    jumlahklik++;
    document.getElementById("counter").textContent = jumlahklik;
}
function resetklik() {
    jumlahklik = 0;
    document.getElementById("counter").textContent = jumlahklik;
}