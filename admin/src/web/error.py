from flask import render_template


def not_found_error(e):
    kwargs = {
        "error_name": "404 Not Found Error",
        "error_description": "La URL a la que quiere acceder no existe"
    }

    return render_template("error.html", **kwargs), 404


def unauthorized(e):
    kwargs = {
        "error_name": "401 Unauthorized",
        "error_description": """
            Usted no posee los permisos necesarios para
            ingresar a esta URL.
        """
    }

    return render_template("error.html", **kwargs), 401


def forbidden(e):
    kwargs = {
        "error_name": "503 Forbidden",
        "error_description": """
            El sitio se encuentra en mantenimiento.
            Por favor, intente más tarde.
        """
    }

    return render_template("error.html", **kwargs), 503



def maintenance(e):
    kwargs = {
        "error_name": "503 Forbidden",
        "error_description": """
            El sitio se encuentra en mantenimiento.
            Por favor, intente más tarde.
        """
    }

    return render_template("error.html", **kwargs), 503