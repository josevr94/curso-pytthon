class Persona {

    // constructor
    constructor(nombre, edad) {
        this.nombre = nombre;
        this.edad = edad;
    }
    // metodo
    mostrarInfo(){
        console.log("nombre: " + this.nombre);
        console.log("edad: "+ this.edad);
    }

}

let persona1 = new Persona('juan perez', 30);
persona1.mostrarInfo();