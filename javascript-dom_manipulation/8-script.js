window.addEventListener('DOMContentLoaded', function() {
    // Hacer la petición Fetch
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
      .then(response => response.json()) // Convertir respuesta a JSON
      .then(data => {
        // Seleccionar el div con id "hello"
        const helloDiv = document.querySelector('#hello');
        
        // Mostrar el valor de "hello"
        helloDiv.textContent = data.hello;
      })
      .catch(error => {
        console.error('Error al obtener el saludo:', error);
      });
  });
  