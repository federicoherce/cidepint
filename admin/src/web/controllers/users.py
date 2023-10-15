from flask import Blueprint, render_template, abort, request
from flask import redirect, url_for, flash
from src.core import auth
from src.forms.users_form import CreateUserForm, UpdateUserForm
from src.web.helpers.auth import login_required, has_permissions, user_is_superadmin

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.get("/")
@login_required
def index():
    if not has_permissions(['user_index']):
        abort(401)

    if request.args:
        email = request.args.get('email')
        estado = request.args.get('estado')
    else:
        email = ""
        estado = "todos"

    users = get_users(email, estado)

    return render_template("users/index.html", users=users)


def get_users(email, estado):
    """
    Este método se encarga de traer los usuarios (se haga o no una búsqueda)
    - Si no se realizó una búsqueda:
      - Me traigo a todos
    - Si se realizó una búsqueda por email y estado:
      - Me traigo a los que contengan el email cuyo estado sea
      igual al recibido
    - Si solo se busca por un criterio, se aplicará solo ese al listado.
    """
    if email == "" and estado == "todos":
        return auth.list_users()

    users = []

    if email != "":
        users.extend(auth.find_user_contains_mail(email))

    if estado != "todos":
        aux = auth.find_user_by_state(estado)  # Menos lecturas
        if email != "":
            users = [u for u in users if u in aux]
        else:
            users.extend(aux)

    return users


@users_bp.get("/profile/<int:user_id>")
@login_required
def user_profile(user_id):
    if not has_permissions(['user_show']):
        abort(401)

    user = auth.get_user_by_id(user_id)
    is_superadmin = user_is_superadmin(user=user)

    return render_template("users/profile.html",
                           user=user,
                           user_is_superadmin=is_superadmin)


@users_bp.route("/update_user/<int:user_id>", methods=['GET', 'POST'])
@login_required
def update_user(user_id):
    if not has_permissions(['user_update']):
        abort(401)

    user = auth.get_user_by_id(user_id)
    form = UpdateUserForm()

    if form.validate_on_submit():
        if user.email != form.email.data:
            existe = auth.find_user_by_mail(form.email.data)
            if existe:
                flash('Este correo electrónico ya está en uso. Por favor, elige otro.', 'error')
                return redirect(url_for("users.update_user", user_id=user.id))

        user.nombre = form.nombre.data
        user.apellido = form.apellido.data
        user.email = form.email.data
        auth.update_user()
        flash("Usuario actualizado con éxito!", "success")
        return redirect(url_for("users.user_profile", user_id=user.id))

    elif request.method == "GET":
        form.nombre.data = user.nombre
        form.apellido.data = user.apellido
        form.email.data = user.email

    return render_template("users/update_user.html", user_id=user.id, form=form)


@users_bp.post("/update_state/<int:user_id>")
@login_required
def update_state(user_id):
    if not has_permissions(['user_update']):
        abort(401)

    user = auth.get_user_by_id(user_id)
    auth.update_state(user)

    return redirect(url_for("users.user_profile", user_id=user_id))


@users_bp.post("/destroy_user/<int:user_id>")
@login_required
def destroy_user(user_id):
    if not has_permissions(['user_destroy']):
        abort(401)

    user = auth.get_user_by_id(user_id)
    auth.delete_user(user)

    flash("Usuario eliminado con éxito", "success")
    return redirect(url_for("users.index"))


@users_bp.route("/create_user", methods=['GET', 'POST'])
@login_required
def create_user():
    if not has_permissions(['user_new']):
        abort(401)

    if request.method == "GET":
        form = CreateUserForm()
        return render_template("users/create_user.html", form=form)

    form = CreateUserForm()
    if form.validate_on_submit():
        existe = auth.find_user_by_mail(form.email.data)
        if existe:
            flash('Este correo electrónico ya está en uso. Por favor, elige otro.', 'error')
            return redirect(url_for("users.create_user"))

        user = auth.create_User(
            email=form.email.data,
            nombre=form.nombre.data,
            apellido=form.apellido.data,
            password=form.contraseña.data,
            token=None,
            activo=True
        )
        flash("Usuario creado con éxito!", "success")
        return redirect(url_for("users.user_profile", user_id=user.id))

    return render_template("users/create_user.html", form=form)
