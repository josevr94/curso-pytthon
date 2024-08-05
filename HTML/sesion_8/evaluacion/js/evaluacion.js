let clientes = [
    {
        nombre: "jose",
        id: "jose123",
        contraseña: "1994",
        saldo: 20000
    },

    {
        nombre: "belen",
        id: "belen123",
        contraseña: "1990",
        saldo: 30000
    },

    {
        nombre: "antai",
        id: "antai123",
        contraseña: "2016",
        saldo: 15000
    },
    {
        nombre: "violeta",
        id: "violeta123",
        contraseña: "2015",
        saldo: 10000
    },
    {
        nombre: "paula",
        id: "violeta124",
        contraseña: "2016",
        saldo: 10000
    },
];

alert("Bienvenido a la Banca en Linea");
let identificacion = prompt("Ingrese su identificación");
let contraseña = prompt("Ingrese su contraseña");

const login = clientes.find(
    cliente => cliente.id == identificacion && cliente.contraseña == contraseña
);




if (login) {
    alert("Bienvenido " + login.nombre);
    while (true) {
    let option = parseInt(prompt("Ingresa una de las siguientes opciones: \n1. Ver saldo, \n2. Realizar giro, \n3. Realizar depósito y \n4. Salir"));
        switch (option) {
            case 1:
                alert("tu saldo es de: " + login.saldo);
                break;

            case 2:
                let giro = parseInt(prompt("ingresa el monto del giro"));
                if (giro > login.saldo) {
                    alert("No tienes suficiente saldo");
                } else {
                login.saldo = login.saldo - giro;
                alert("Giro realizado");
                alert("Tu nuevo saldo es de: " + login.saldo);
                }
                break;

            case 3:
                let deposito = parseInt(prompt("ingresa el monto del deposito"));
                login.saldo = login.saldo + deposito;
                alert("Depósito realizado");
                alert("Tu nuevo saldo es de: " + login.saldo);
                break;

            case 4:
                break;
        }
        if (option == 4) {
            alert("Hasta pronto");
            break;
        }
    }
    
} else {
    alert("No se encontro el cliente");
}



