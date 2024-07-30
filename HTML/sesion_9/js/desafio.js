document.addEventListener('DOMContentLoaded', function () {
    const taskInput = document.getElementById('taskInput');
    const addTaskBtn = document.getElementById('addTaskBtn');
    const taskList = document.getElementById('taskList');

    // Función para agregar una nueva tarea
    function addTask() {
        const taskText = taskInput.value;
        if (taskText !== "") {
            const li = document.createElement('li');
            li.textContent = taskText;

            // Botón de eliminar
            const deleteBtn = document.createElement('button');
            deleteBtn.textContent = 'Eliminar';
            deleteBtn.classList.add('delete-btn');
            deleteBtn.onclick = function () {
                taskList.removeChild(li);
            };

            li.appendChild(deleteBtn);

            // Marcar como completada
            li.onclick = function () {
                li.classList.toggle('completed');
            };

            taskList.appendChild(li);
            taskInput.value = "";
        }
    }

    // Agregar tarea al hacer clic en el botón
    addTaskBtn.addEventListener('click', addTask);

    // Agregar tarea al presionar Enter
    taskInput.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            addTask();
        }
    });
});