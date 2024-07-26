var opcion = parseInt(prompt("¡Hola! Soy Eva, tu asistente virtual del Servicio al Cliente de Mentel. Estoy aquí para ayudarte en lo que necesides.\nEscribe el número de la opción que buscas: \n1.- Boletas y Pagos \n2.- Señal y llamadas \n3.- Oferta comercial  \n4.- Otras consultas"))
if (opcion ==1 || opcion == 2 || opcion == 3 || opcion == 4) {
    switch (opcion) {
    case 1:
        // console.log("hi");
        boletasypagos();
        break;
    case 2:
        señalYllamadas();
        break
    case 3:
        ofertaComercial();
    case 4:
        otrasConsultas();
}
}else {
    alert("La opcion ingresada no es valida, Gracias por preferirnos");
}

function boletasypagos() {
    opcion2 = parseInt(prompt("1.- ver boletas/ 2.- pagar cuentas"))
    switch (opcion2) {
        case 1:
            alert("haga click para descargar su boleta");
        case 2:
            alert("usted esta siendo transferido espere porfavor");
    }
}
function señalYllamadas() {
    opcion2 = parseInt(prompt("1.- problemas con la señal / 2.- problemas con las llamadas"))
    switch (opcion2) {
        case 1:
            prompt("a continuacion escriba su solicitud")
            alert("estimado usuario, su consulta:'quisiera saber porque no ha llegado mi producto codigo 1234 ha sido ingresada con exito. pronto sera contactado por uno de nuestro ejecutivos")
            break
        case 2:
            prompt("a continuacion escriba su solicitud")
            alert("estimado usuario, su solicitud:tengo problemas con la señal en avenida siempre viva ha sido ingresada con exito, pronto sera contactado por uno de nuestros ejecutivos")
            break
    }
}

function ofertaComercial() {
    opcion = (prompt("mentel tiene una oferta comercial acorde a tus necesidades para conocer mas informacion y ser asesorado personalmente por un ejecutivo escriba si y un ejecutivo te llamara de lo contrario ingrese no"))
    if (opcion == "si") {
        alert("un ejecutivo se contactara con usted")
    } else if (opcion == "no") {
        alert("Gracias por preferir nuestro servicio")
 
    } else {
        alert("la opcion no es valida, lea con atencion")
        ofertaComercial()
    }
}

function otrasConsultas() {
    prompt("a continuacion escriba su solicitud")
    alert("estimado usuario, su consulta:'quisiera saber porque no ha llegado mi producto codigo 1234 ha sido ingresada con exito. pronto sera contactado por uno de nuestro ejecutivos")
}
// opcion2 = prompt("1.-ver boletas / 2.-pagar cuentas");
// switch (opcion2) {
//     case 1:
//         alerta1 = alert("haga click para descargar su boleta");
//         return alerta1
//     case 2:
//         alerta2 = alert("usted esta siendo transferido espere porfavor");
//         return alerta2
// }

// if (opcion == 1) {
//     verboletas()
// } else if (opcion == 2) {
//     var opcion3 = prompt("selecciona una opcion, 1.-problemas con la señal, 2.-problemas con las llamadas")
//     if (opcion3 == 1 || 2) {
//         prompt("a continuacion escriba su solicitud")
//         alert("estimado usuario, su solicitud:tengo problemas con la señal en avenida siempre viva ha sido ingresada con exito, pronto sera contactado por uno de nuestros ejecutivos")
//     }

// } else if (opcion == 3) {
//     var opcion4 = prompt("mentel tiene una oferta comercial acorde a tus necesidades para conocer mas informacion y ser asesorado personalmente por un ejecutivo escriba 'si' y un ejecutivo te llamar. de lo contrario ingrese 'no'")
//     if (opcion4 == "si3") {
//         alert("un ejecutivo contactara con usted")
//     } else {
//         alert("Gracias por preferir nuestro servicio")
//     }
// } else if (opcion == 4) {
//     prompt("a continuacion escriba su consulta")
//     alert("estimado usuario, su consulta:'quisiera saber porque no ha llegado mi producto codigo 1234 ha sido ingresada con exito. pronto sera contactado por uno de nuestro ejecutivos")
// } else {
//     alert("la opcion ingresada no es valida. gracias por preferir nuestros servicios")
// }
// //FUNCIONES
// function verboleta{
//     var opcion2 = prompt("selecciona una opcion: 1.- ver boleta, 2.-pagar cuenta")
//     if (opcion2 == 1) {
//         alert("haga click aqui para descargar su boleta")
//     } else {
//         alert("usted esta siendo transferido, espere porfavor")
//     }
// }
