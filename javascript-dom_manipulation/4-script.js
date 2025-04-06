// Seleccionar el div con id "add_item"
const addItem = document.querySelector('#add_item');

// Seleccionar el ul con clase "my_list"
const myList = document.querySelector('.my_list');

// Escuchar el evento click en el div
addItem.addEventListener('click', function() {
  // Crear un nuevo elemento <li>
  const newItem = document.createElement('li');
  
  // Agregarle el texto "Item"
  newItem.textContent = 'Item';
  
  // Insertar el nuevo <li> en el <ul>
  myList.appendChild(newItem);
});
