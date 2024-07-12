
document.getElementById("formulario").addEventListener("submit", function(event) {
    event.preventDefault();  // Evita el envío del formulario

    var nombre = document.getElementById("nombre").value;
    var usuario = document.getElementById("usuario").value;
    var correo = document.getElementById("correo").value;
    var contraseña = document.getElementById("contraseña").value;
    var pais = document.getElementById("pais").value;
    var telefono = document.getElementById("telefono").value;

    if (validarFormulario(nombre, usuario, correo, contraseña, telefono)) {
        var user = {
            nombre: nombre,
            usuario: usuario,
            correo: correo,
            contraseña: contraseña,
            telefono: telefono,
            pais: pais
        };

        localStorage.setItem("user", JSON.stringify(user));
        console.log("Datos guardados en LocalStorage:");
        console.log(user);
        alert("Datos guardados exitosamente!");
    }
});

function validarFormulario(nombre, usuario, correo, contraseña, telefono) {
    var isValid = true;

    if (nombre === "") {
        document.getElementById("mensajeNombre").textContent = "Debe ingresar un nombre";
        isValid = false;
    } else {
        document.getElementById("mensajeNombre").textContent = "";
    }

    if (usuario === "") {
        document.getElementById("mensajeUsuario").textContent = "Debe ingresar un usuario";
        isValid = false;
    } else {
        document.getElementById("mensajeUsuario").textContent = "";
    }

    if (correo === "") {
        document.getElementById("mensajeCorreo").textContent = "Debe ingresar un correo";
        isValid = false;
    } else {
        document.getElementById("mensajeCorreo").textContent = "";
    }

    if (contraseña.length < 8) {
        document.getElementById("mensajeContra").textContent = "Debe ingresar una contraseña válida";
        isValid = false;
    } else {
        document.getElementById("mensajeContra").textContent = "";
    }

    if (telefono.length < 8) {
        document.getElementById("mensajeFono").textContent = "Ingrese un número de teléfono válido";
        isValid = false;
    } else {
        document.getElementById("mensajeFono").textContent = "";
    }

    return isValid;
}