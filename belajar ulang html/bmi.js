function cekBMI() {
    const berat = parseFloat(document.getElementById("berat").value);
    const tinggiCm = parseFloat(document.getElementById("tinggi").value); 
    const hasil = document.getElementById("hasil");
// pareFloat untuk mengubah string angka desimal menjadi angka asli bertipe desimal supaya bisa dihitung (float)
    if (isNaN(berat) || isNaN(tinggiCm) || berat <= 0 || tinggi <= 0) {
        hasil.innerHTML= "Masukan Berat Badan dan Tinggi Kamu";
        return;
    }

    const tinggiMeter = tinggiCm / 100;
    const bmi = berat / (tinggiMeter * tinggiMeter);
    const kategori = getKategoriBMI(bmi);

    hasil.innerHTML = `BMI kamu: ${bmi.toFixed(1)} (${kategori})` //toFixed membulatkan angka di belakang koma
}

function getKategoriBMI(bmi) {
    if (bmi < 18.5) {
        return "Kurus";
    } else if (bmi < 25) {
        return "Ideal";
    } else if (bmi < 30) {
        return "Gemuk";
    } else {
        return "Lu butuh olah raga";
    }

}