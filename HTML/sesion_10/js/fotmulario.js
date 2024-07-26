$(document).ready(function() {
    $('#simpleform').on('submit', function(event) {
        event.preventDefault(); // Evita el envío del formulario

        let isValid = true;
        let errorMessage = '';
        let successMessage = '';

        // Limpiar mensajes previos
        $('.error').remove();
        $('#formMessage').empty();

        // Validación del nombre de usuario
        const username = $('#username').val().trim();
        if (username === '') {
            isValid = false;
            $('#username').after('<span class="error">El nombre de usuario es obligatorio.</span>');
        }

        // Validación del correo electrónico
        const email = $('#email').val().trim();
        if (email === '') {
            isValid = false;
            $('#email').after('<span class="error">El correo electrónico es obligatorio.</span>');
        } else {
            const emailPattern = /^[^@]+@[^@]+\.[a-zA-Z]{2,}$/;
            if (!emailPattern.test(email)) {
                isValid = false;
                $('#email').after('<span class="error">Ingrese un correo electrónico válido.</span>');
            }
        }

        // Validación de la contraseña
        const password = $('#password').val().trim();
        if (password === '') {
            isValid = false;
            $('#password').after('<span class="error">La contraseña es obligatoria.</span>');
        }

        // Mostrar mensaje de éxito o error
        if (isValid) {
            successMessage = '<p class="aceppted">Formulario enviado exitosamente.</p>';
            $('#formMessage').html(successMessage);
            // Aquí puedes agregar la lógica para enviar el formulario al servidor si es necesario.
        } else {
            errorMessage = '<p class="error">Por favor, corrige los errores en el formulario.</p>';
            $('#formMessage').html(errorMessage);
        }
    });
});