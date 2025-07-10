function cekSIM() {
    const input = document.getElementById("daftarUmur").value;
    const umurList = input.split(",").map(u => parseInt(u.trim()));
    const output = document.getElementById("output");

    output.innerHTML = "";  //fungsinya reset ouput
    
 for (let i= 0; i < umurList.length; i++) {

    const umur = umurList[i];
    
    const status = umur >= 17 ? "Boleh Buat SIM" : "Belum Bisa Buat SIM";

    const baris = `<p>Orang ke-${i + 1} (Umur ${umur}): ${status}</p>`;
    output.innerHTML += baris;
 }
}