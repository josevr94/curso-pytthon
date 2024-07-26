
const students = [
    { name: 'Jonh', grade: 75 },
    { name: 'Jane', grade: 93 },
    { name: 'Samantha', grade: 90 },
    { name: 'Michael', grade: 94 }
];

// 1. Ordenar en orden descendente
students.sort((a,b ) => b.name - a.name);
console.log('Orden descendente:', students);

// 2. Reversar el arreglo
students.reverse();
console.log('Reversar el arreglo:', students);

// 3. Encontrar el primer estudiante con calificación mayor a 90
const firstStudentAbove90 = students.find(student => student.grade > 90);
console.log('Primer estudiante con calificación mayor a 90:', firstStudentAbove90);

// Crear un array
let frutas = ["Manzana", "Banana", "Cereza"];

// Obtener la longitud del array
console.log("Longitud del array:", frutas.length); // Output: 3

// Añadir un elemento al final del array (push)
frutas.push("Durazno");
console.log("Después de push:", frutas); // Output: ["Manzana", "Banana", "Cereza", "Durazno"]

// Eliminar el último elemento del array (pop)
let ultimaFruta = frutas.pop();
console.log("Después de pop:", frutas); // Output: ["Manzana", "Banana", "Cereza"]
console.log("Última fruta:", ultimaFruta); // Output: "Durazno"

// Eliminar el primer elemento del array (shift)
let primeraFruta = frutas.shift();
console.log("Después de shift:", frutas); // Output: ["Banana", "Cereza"]
console.log("Primera fruta:", primeraFruta); // Output: "Manzana"

// Añadir un elemento al principio del array (unshift)
frutas.unshift("Fresa");
console.log("Después de unshift:", frutas); // Output: ["Fresa", "Banana", "Cereza"]

// Revertir el orden del array (reverse)
frutas.reverse();
console.log("Después de reverse:", frutas); // Output: ["Cereza", "Banana", "Fresa"]

