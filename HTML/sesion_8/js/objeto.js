let mochila ={
    // pripiedades del objeto
    color: 'negro',
    tamaño: '20cm',
    numero_bolsillos: 2,
    numeroCierres: 2,
    // metod del objeto
    abrir_tapa: function(){
        console.log("la tapa de la mochila esta abierta");
    },
    cerrarTapa: function(){
        console.log("la tapa de la mochila esta cerrada");
    }
}
// accediendo a las propiedades del objeto
console.log(mochila.color);
console.log(mochila.tamaño);
// accediendo a los metodos del objeto
mochila.abrir_tapa();
mochila.cerrarTapa();
console.log(mochila);