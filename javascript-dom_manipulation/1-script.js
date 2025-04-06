// Seleccionar el div con id "red_header"
const redHeader = document.querySelector('#red_header');

// Seleccionar el elemento <header>
const header = document.querySelector('header');

// Escuchar el evento click en el div
redHeader.addEventListener('click', function() {
  header.style.color = '#FF0000';
});
