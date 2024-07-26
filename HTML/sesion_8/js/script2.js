// Datos de ejemplo
const alumnos = ["Roberto Hernandez", "Ana Gómez", "Luis Pérez"];
const calificaciones = [6, 3, 8]; // Las calificaciones corresponden a los alumnos en el mismo orden

// Función para mostrar el menú
function mostrarMenu() {
    const opcion = prompt("Seleccione una opción:\n1. Ver lista de alumnos\n2. Ver calificaciones de alumnos\n3. Calcular el promedio del grupo");
    
    switch(opcion) {
        case '1':
            verListaAlumnos();
            break;
        case '2':
            verCalificaciones();
            break;
        case '3':
            calcularPromedio();
            break;
        default:
            console.log("Opción no válida.");
            mostrarMenu(); // Volver a mostrar el menú en caso de opción no válida
    }
}

// Función para ver la lista de alumnos
function verListaAlumnos() {
    console.log("Lista de Alumnos:");
    for (let i = 0; i < alumnos.length; i++) {
        console.log(`${i + 1}. ${alumnos[i]}`);
    }
}

// Función para ver las calificaciones de los alumnos
function verCalificaciones() {
    console.log("Calificaciones de Alumnos:");
    for (let i = 0; i < calificaciones.length; i++) {
        let estado = calificaciones[i] <= 3 ? "Reprobado" : "Aprobado";
        console.log(`Alumno ${i + 1}: Calificación: ${calificaciones[i]}, ${estado}`);
    }
}

// Función para calcular el promedio del grupo
function calcularPromedio() {
    let suma = 0;
    for (let i = 0; i < calificaciones.length; i++) {
        console.log(suma += calificaciones[i]); 
    }
    let promedio = suma / calificaciones.length;
    console.log("El promedio del grupo es:" + promedio );
}

// Llamar a la función para mostrar el menú
mostrarMenu();