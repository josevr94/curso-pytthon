const entrada = document.getElementById("entrada");
const button = document.getElementById("button");
const list = document.getElementById("list");
const textinput = entrada.value;
    console.log(textinput);

function agregarElementoAlista(){
    
    const nuevoElement = document.createElement("li");
    nuevoElement.textContent = entrada.value;
    
}