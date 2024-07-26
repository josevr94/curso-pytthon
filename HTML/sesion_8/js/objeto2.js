// metdo constructor
function Mochila(color, tamaño,numero_bolsillos,numeroCierre) {

    // la palabra en verde despues de function es una clase que siempre va en mayuscula la primera letra
    
    
    // propiedades
    this.color = color;
    this.tamaño = tamaño;
    this.numeroCierre = numeroCierre;
    this.numero_bolsillos = numero_bolsillos;

    this.abrir_tapa =  function(){
        console.log("la tapa de la mochila esta abierta");
    },
    this.cerrarTapa= function(){
        console.log("la tapa de la mochila esta cerrada");
    }
}
// creando instancias de objetas
let mochila1= new Mochila ("negra","pequeña",2,2);
let mochila2= new Mochila ("roja", "mediana", 2, 2);
let mochila3= new Mochila ("negra", "grande",10,10)

// aciendo las propiedades de las instancias
console.log(mochila1.color);
console.log(mochila2.color);
console.log(mochila3.color);

mochila2.abrir_tapa();
mochila1.cerrarTapa();