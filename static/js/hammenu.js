const bars = document.querySelector("#bars");
const cont = document.querySelector("#conte");
let active = false;

bars.addEventListener("click", function () {
  if (!active) {
    bars.innerHTML = '<i class="fas fa-times"></i>';
    cont.classList.remove("ncc");
    cont.classList.add("ac");
    active = true;
  } else {
    bars.innerHTML = '<i class="fas fa-bars"></i>';
    cont.classList.remove("ac");
    cont.classList.add("ncc");
    active = false;
  }
});
