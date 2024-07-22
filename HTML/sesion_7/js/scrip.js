// console.log("hola desde la consola");
alert("calculadora")
alert("Opciones: 1. Suma, 2. Resta, 3. Multiplicacion, 4. Division")
opcion = parseInt(prompt("Escriba el numero de la opcion"));
var a;
var b;
a = parseInt(prompt("ingresa un numero"));
b = parseInt(prompt("ingresa otro numero"));
if (a == 0 && b == 0) {
    alert("Los numero son 0, No se puede hacer operaciones");
} else {
    switch (opcion) {
        case 1:
            total = suma(a, b);
            alert("el resultado de la suma es: " + total);
            break;
        case 2:
            total2 = resta(a, b);
            alert("el resultado de la resta es: " + total2);
            break;
        case 3:
            total3 = multiplicacion(a, b);
            alert("el resultado de la multiplicacion es: " + total3);
            break;
        case 4:
            total4 = division(a, b);
            alert("el resultado de la division es: " + total4);
            break;
        default:
            alert("la opcion no es valida, lea con atencion");
    }
}

alert("Gracias por usar esta humilde Calculadora")

function suma(a, b) {
    resultado = a + b
    return resultado
}
function resta(a, b) {
    resultado = a - b
    return resultado
}
function multiplicacion(a, b) {
    // total3 = a*b
    if (a == 0 || b == 0 ) {
        resultado = "Multiplicacion vacia"
    } else {
        a * b
    }
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