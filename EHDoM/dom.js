function tampilkanNama() { 
  const inputNama = document.getElementById("nama").value; 
  const hasil = document.getElementById("hasil"); 

  if (inputNama.trim() === "") {
    hasil.textContent = "Nama tidak boleh kosong!";
    hasil.style.color = "red";
  } else {
    hasil.textContent = "Halo, " + inputNama + "!";
    hasil.style.color = "green";
  }
}

/* ✅ Kapan function dipakai?
Fungsi dipakai kalau lu butuh bikin potongan kode yang bisa dipanggil berulang. */
/* const: bikin variable tetap atau nilai yg gakan ganti*/
/*value fungsinya amnil isi dari element*/
/* document.get /* tugasnya cari element dari html sesuai nama dalam kurung */