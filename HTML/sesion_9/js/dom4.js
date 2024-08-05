// // var selectorid = document.getElementById('parrafo');
// // console.log(selectorid);
// var selectorEtiqueta = document.getElementsByTagName('h1');
// console.log(selectorEtiqueta);
// var selectorClass = document.getElementsByClassName('contenedor');
// console.log(selectorClass);
// var selectorId = document.getElementById('parrafo').innerHTML;
// console.log(selectorId);
// var selectorid= document.getElementById('parrafo');
// console.log(selectorid);
// var selectorIde = document.getElementById('parrafo').innerHTML;
// console.log(selectorIde);

// // creando elementos

// var creandoelemento = document.createElement('div');
// var creandoelemento2 = document.createElement('p');
// creandoelemento2.textContent="esto lo cree dentro del div";
// creandoelemento.append(creandoelemento2);
// document.body.appendChild(creandoelemento);

function mostrarMensaje(){
    document.getElementById('caja2').style.display="block";
}
function ocultarMensaje(){
    document.getElementById('caja2').style.display="none";
}
function mostrarconClick(){
    document.getElementById('contenido').style.display="none";
}
function ocultarconClick(){
    document.getElementById('contenido').style.display="block";
}