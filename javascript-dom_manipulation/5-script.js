// Seleccionar el div con id "update_header"
const updateHeader = document.querySelector('#update_header');

// Seleccionar el elemento <header>
const header = document.querySelector('header');

// Escuchar el evento click en el div
updateHeader.addEventListener('click', function() {
  header.textContent = 'New Header!!!';
});
