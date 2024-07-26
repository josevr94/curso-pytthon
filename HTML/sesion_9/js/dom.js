// obtener elementos del dom y guardarlo en variables
const titulo = document.getElementById("titulo");
const descripcion= document.getElementById("descripcion");
const bottonAgregar= document.getElementById("botonAgregar");
const botonCambiar= document.getElementById("botonCambiar");


function agregarElemento() {
    // crear un nuevo elemento <p>
    const nuevoParrafo = document.createElement("p");
    // añadir un texto al elemento
    nuevoParrafo.textContent = "este es un nuevo parrafo agregado desde JS";
    // añadir una clase al nuevo elemento
    nuevoParrafo.classList.add("nuevo-elemento");
    // insertar un elemento al body
    document.body.appendChild(nuevoParrafo);

}
function cambiarValor() {
    // cambiar el contenido del parrafo
    descripcion.textContent = "aqui estuvo josev.";
    descripcion.classList.add("resaltado");
}

botonAgregar.addEventListener("click", agregarElemento);
botonCambiar.addEventListener("click", cambiarValor); 