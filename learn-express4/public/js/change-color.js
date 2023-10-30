const heading = document.querySelector('.heading');
const text = document.querySelector('#text');
heading.onclick = function() {
  heading.style.color = "red";
}
text.onclick = function() {
  text.style.color = "blue";
}

// updated 2019
const input = document.getElementById("search-input");
const searchBtn = document.getElementById("search-btn");

const expand = () => {
  searchBtn.classList.toggle("close");
  input.classList.toggle("square");
};

searchBtn.addEventListener("click", expand);