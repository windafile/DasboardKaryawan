const kotak = document.getElementById("kotak");
/*ketika mouse masuk kotak*/
kotak.addEventListener("mouseover", function() {
    kotak.textContent = "Eaaaaa";
})
/*kerika mouse keluar kotak*/
kotak.addEventListener("mouseout", function() {
    kotak.textContent = "Toel dong";
})