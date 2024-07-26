// var n_articulos = parseInt(prompt("Numero de articulos que desea comprar"));
// for(var inicio=1; inicio<=n_articulos; inicio++){
//     var precio_articulo= parseInt(prompt("Dame precio de articulo: "+inicio))
//     var cantidad_articulo= parseInt(prompt("Dame cantidad: "+ inicio))
// console.log("Precio de articulo: "+precio_articulo);
// console.log("cantidad: "+ cantidad_articulo);
// console.log(calcular_Subtotal(precio_articulo,cantidad_articulo));
// }

// ciclo do while
// var numero = parseInt(prompt("ingresa un numero"))
var numero;
var x=1
do {
    console.log("x");
    x = x + 1;
} while (x< numero);


// try catch
var numero2 = parseInt(prompt("ingresa un numero"));
try{
    if(numero2 != 10)throw new Error("El numero no es 10")
}catch (error){
    console.log("La ejecucion se hizo de manera Correcta");
}




function calcular_Subtotal(precio, cantidad) {
    subtotal = precio * cantidad;
    return subtotal;
}

