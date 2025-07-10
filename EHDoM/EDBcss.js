const semuaTombol = document.querySelectorAll(".tombol");

semuaTombol.forEach(function(tombol) {
  const teksHover = tombol.dataset.hover;
  const teksKlik = tombol.dataset.klik;

  function mouseover() {
    tombol.textContent = teksHover;
  }
  function mouseout() {
    tombol.textContent = tombol.dataset.defaultText || tombol.innerText;
  }
  // simpan isi awal tombol ke data-defaultText
  tombol.dataset.defaultText = tombol.innerText;

  tombol.addEventListener("mouseover", mouseover);
  tombol.addEventListener("mouseout", mouseout);

  tombol.addEventListener("click", function() {
    tombol.textContent= teksKlik;
    tombol.classList.add("sudah-diklik");

    //mematikan hover agar warna tidak berubah lagi
    tombol.removeEventListener("mouseover", mouseover);
    tombol.removeEventListener("mouseout", mouseout);
  })
})