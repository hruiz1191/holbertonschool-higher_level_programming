// Hacer una petición Fetch a la API
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json()) // Convertir la respuesta a JSON
  .then(data => {
    // Seleccionar el div con id "character"
    const character = document.querySelector('#character');
    
    // Actualizar el contenido con el nombre del personaje
    character.textContent = data.name;
  })
  .catch(error => {
    console.error('Error al obtener el personaje:', error);
  });
