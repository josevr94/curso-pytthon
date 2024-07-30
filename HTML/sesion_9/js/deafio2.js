$(document).ready(function() {
    // Evento de envío del formulario
    $('#survey-form').submit(function(event) {
        event.preventDefault();
        
        const name = $('#name').val();
        const email = $('#email').val();
        const rating = $('#rating').val();
        const comments = $('#comments').val();

        if (name && email && rating && comments) {
            $('#result-name').text(`Nombre: ${name}`);
            $('#result-email').text(`Correo Electrónico: ${email}`);
            $('#result-rating').text(`Calificación: ${rating}`);
            $('#result-comments').text(`Comentarios: ${comments}`);

            $('#results').removeClass('hidden');
            $('#results').css('background-color', getRandomColor());

            alert('¡Gracias por completar la encuesta!');
        } else {
            alert('Por favor, completa todos los campos.');
        }
    });

    // Evento para mostrar/ocultar resultados
    $('#toggle-results').click(function() {
        $('#results').slideToggle();
    });

    // Función para obtener un color aleatorio
    function getRandomColor() {
        const letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }
});