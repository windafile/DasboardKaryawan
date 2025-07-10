function hitungLuas(p, l) {
return p * l;
}
function tampilkanHasil() {
    const panjang = parseInt(document.getElementById("panjang").value);
    const lebar = parseInt(document.getElementById("lebar").value);
    const output = document.getElementById("output");

    if (isNaN(panjang) || isNaN(lebar)) {
        output.innerHTML= "isi kolom terlebih dahulu";
        return;
    }
    const luas= hitungLuas(panjang, lebar);
    output.innerHTML=`Luas persegi adalah: ${luas}`;
}