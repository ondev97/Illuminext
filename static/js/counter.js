let countercolumn = document.querySelectorAll(".counter .main .column");

let cou = 0;

const count = () => {
  cou++;
  if (countercolumn[0].dataset.count >= cou) {
    countercolumn[0].children[0].innerHTML = cou;
  }
  if (countercolumn[1].dataset.count >= cou) {
    countercolumn[1].children[0].innerHTML = cou;
  }
  if (countercolumn[2].dataset.count >= cou) {
    countercolumn[2].children[0].innerHTML = cou;
  }
  if (countercolumn[3].dataset.count >= cou) {
    countercolumn[3].children[0].innerHTML = cou;
  }
};

let timer = setInterval(count, 1);
