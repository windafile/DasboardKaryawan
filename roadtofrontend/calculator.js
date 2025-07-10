document.getElementById("hitung").addEventListener("click", function(){
    const angka1 = parseFloat(document.getElementById('angka1').value);
    const angka2 = parseFloat(document.getElementById('angka2').value);
    const operator = document.getElementById("operator").value;

    let hasil;

    if (isNaN(angka1) || isNaN(angka2)) {
        hasil = "Isi dulu kedua angkanya ya, bre!";
    } else if (operator === "+") {
        hasil = angka1 + angka2;
    } else if (operator === "-") {
        hasil = angka1 - angka2;
    } else if (operator === "*") {
        hasil = angka1 * angka2;
    } else if (operator === "/") {
        if (angka2 === 0) {
            hasil = "Gak bisa dibagi 0, bre!!";
        } else {
            hasil = angka1 / angka2;
        }
    } else {
        hasil = "oprasi tidak diketahui";
    }

    document.getElementById("hasil").textContent = hasil;
});