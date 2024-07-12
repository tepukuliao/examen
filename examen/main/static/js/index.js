$(document).ready(function(){
    var texto = $("#texto-acerca").text(); // Obtener el texto del párrafo
    $("#texto-acerca").empty(); // Vaciar el párrafo
    
    // Recorrer el texto letra por letra y agregarlo gradualmente al párrafo
    $.each(texto.split(""), function(i, letra){
      setTimeout(function(){
        $("#texto-acerca").append(letra);
      }, 40 * i); // Cambiar la velocidad de escritura ajustando el número
    });
});


let map;

async function initMap(){
  
  
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerView } = await google.maps.importLibrary("marker");

  map = new Map(document.getElementById("map"), {
    center: {lat: -33.0241813659668, lng: -71.5575180053711}, 
    zoom: 18,
  }
  );
  const position = { lat: -33.0241813659668, lng: -71.5575180053711 };
  const marker = new google.maps.Marker({
    map: map,
    position: position,
    title: "Viña",
    label: {
      text: "Reptilia Chile", // Nombre del marcador
      color: "black", // Color del texto
      fontWeight: "bold" // Estilo del texto
  }
  });
  
}

initMap();


