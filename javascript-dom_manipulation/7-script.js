// Hacer una petición Fetch a la API de películas
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json()) // Convertir la respuesta a JSON
  .then(data => {
    // Seleccionar el ul con id "list_movies"
    const list = document.querySelector('#list_movies');

    // Recorrer cada película en la respuesta
    data.results.forEach(movie => {
      const item = document.createElement('li'); // Crear un nuevo <li>
      item.textContent = movie.title; // Poner el título de la película
      list.appendChild(item); // Agregarlo al ul
    });
  })
  .catch(error => {
    console.error('Error al obtener las películas:', error);
  });
