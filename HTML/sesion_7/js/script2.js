// alert("Hola bienvenido a la caja");
document.body.innerHTML=("Hola bienvenido a la caja")
alert("Es usted Residente o viajero?, para residente presione 1, para viajero 2");
opcion = parseInt(prompt("coloque su opcion aqui"));
alert("Tiene algun cupon de descuento?")

iva = 1.19;
opciondescuento = parseInt(prompt("si Tiene algun cupon de descuento?,si tiene alguno coloque 3, sino coloque 0"))
prompt("que articulo lleva");
a = parseInt(prompt("Que valor tiene el articulo?"));
b = parseInt(prompt("que cantidad lleva de este mismo articulo"));

if (opciondescuento == 3)
    switch (opcion) {

        case 1:
            c = parseInt(prompt("de cuanto es su cupon?"))
            total = cupon(a, b);
            alert("Debe pagar: " + total);
            break
        case 2:
            c = parseInt(prompt("de cuanto es su cupon?"))
            total2 = multiplicacion(a, b);
            alert("Debe pagar: " + total2);
            break
        default:
            alert("Opcion no valida, leer correctamente las opciones");
            break;

    } else {
    switch (opcion) {
        case 1:
            total2 = multiplicacion2(a, b);
            alert("Debe pagar: " + total2);
            break;
        case 2:
            total = multiplicacion(a, b);
            alert("Debe pagar: " + total);
            break;
        default:
            alert("Opcion no valida, leer correctamente las opciones");
            break;
    }
}


function multiplicacion(a, b) {
    resultado = a * b - c
    return resultado
}
function multiplicacion2(a, b) {
    resultado = a * b * iva - c
    return resultado
}
function cupon(a, b) {
    resultado = a * b * iva - c
    return resultado

}