// declarar un arreglo

var regiones = ["santiago","antofagasta","viña del mar","bio-bio"];
// imprimir un arreglo
console.log(regiones);
// obtener una posicion especifica de un arreglo
console.log(regiones[1]);
// recorrido de un arreglo y agregamos una cadena
for(var i =0; i<regiones.length;i++){
    console.log(regiones[i]);
}
// agregando un valor al arreglo
regiones.push("Maule")
console.log(regiones);
regiones.pop();
console.log(regiones);
regiones.pop();
console.log(regiones);
regiones.pop();
console.log(regiones);
regiones.pop();
console.log(regiones);
regiones.push("los lagos")
console.log(regiones);
regiones.shift();
console.log(regiones);
regiones.unshift("RANCAGUA")
console.log(regiones);
regiones.push("PAINE")
regiones.push("BUIN")
console.log(regiones);
for(var i =0; i<regiones.length;i++){
    console.log(regiones[i]);
}
console.log(regiones[0]);
// recorremos un arreglo y hacemos una operacion
var precios=[805,995,3483,2223,454,654,34]
for(var i =0; i<precios.length;i++){
    console.log(precios[i]);
    console.log(precios[i]*1.19);
}