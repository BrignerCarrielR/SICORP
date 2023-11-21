console.log(usuarios);
console.log(admin);


function EnviarCodigo() {
    let correo = document.getElementById('correo').value;
    usuarios.forEach(function (usuario) {
        // Accede a las propiedades del usuario

        if (correo == usuario.correo) {
            console.log('Su contraseña es: ', usuario.contraseña)

            // Envía el correo utilizando EmailJS después de realizar la solicitud
            const serviceID = 'service_atvwoci';
            const templateID = 'template_gxjy74d';
            const userID = 'MSBVq_POAKjwB1Ucr';

            // Define los datos del correo
            const dataCorreo = {
                nombre: usuario.nombres, // Utiliza el nombre del cliente
                correo: usuario.correo,
                cont: usuario.contraseña
            };

            // Envía el correo utilizando EmailJS
            emailjs.send(serviceID, templateID, dataCorreo, userID)
                .then(function (response) {
                    console.log('Correo enviado con éxito:', response);
                })
                .catch(function (error) {
                    console.error('Error al enviar el correo:', error);
                });
        }

    });
}

function EnviarCodigoadmin() {
    let correo = document.getElementById('correo').value;
    admin.forEach(function (admin) {
        // Accede a las propiedades del usuario

        if (correo == admin.correo) {
            console.log('Su contraseña es: ', admin.contraseña)

            // Envía el correo utilizando EmailJS después de realizar la solicitud
            const serviceID = 'service_atvwoci';
            const templateID = 'template_gxjy74d';
            const userID = 'MSBVq_POAKjwB1Ucr';

            // Define los datos del correo
            const dataCorreo = {
                nombre: admin.nombres, // Utiliza el nombre del cliente
                correo: admin.correo,
                cont: admin.contraseña
            };

            // Envía el correo utilizando EmailJS
            emailjs.send(serviceID, templateID, dataCorreo, userID)
                .then(function (response) {
                    console.log('Correo enviado con éxito:', response);
                })
                .catch(function (error) {
                    console.error('Error al enviar el correo:', error);
                });
        }

    });
}















