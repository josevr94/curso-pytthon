// console.log("hola desde la consola");
alert("calculadora")
console.log("bienvenidos a la calculadora basica");
var a;
var b;
var suma;
// a= 6666;
// b= 444324;
a = parseInt(prompt("ingresa un numero"));
b = parseInt(prompt("ingresa otro numero"));
total = suma(a, b)
alert("el resultado de la suma es: " + total);
total2 = resta(a, b);
alert("el resultado de la resta es: " + total2);
total3 = multiplicacion(a, b);
alert("el resultado de la multiplicacion es: " + total3);
total4 = division(a, b);
alert("el resultado de la division es: " + total4);
if( total3 == 0){
    alert("resultado vacio")
}

function suma(a, b) {
    resultado = a + b
    return resultado
}
function resta(a, b) {
    resultado = a - b
    return resultado
}
function multiplicacion(a, b) {
    resultado = a * b
    return resultado
}
function division(a, b) {
    if (a > b) {
        resultado = a / b
    } else {
        resultado = "no"
    }
    return resultado
}