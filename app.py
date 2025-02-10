from flask import Flask, render_template, request, redirect, url_for, session
from persistencia.conexion import Conexion
from persistencia.proveedorDAO import ProveedorDAO
from persistencia.empleadoDAO import EmpleadoDAO
from persistencia.clienteDAO import ClienteDAO
from persistencia.muebleDAO import MuebleDAO
from persistencia.cargoDAO import CargoDAO

app = Flask(__name__, template_folder="presentacion/templates")
app.secret_key = 'clave_secreta'

# Página principal
@app.route('/')
def index():
    muebles = MuebleDAO.obtener_todos()
    return render_template('index.html', muebles=muebles)

# Inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    roles = CargoDAO.obtener_todos()
    if request.method == 'POST':
        id = request.form['id']
        rol = request.form['rol']
        empleado = EmpleadoDAO.autenticar(id, rol)
        if empleado:
            session['empleado_id'] = empleado.id_empleado
            return redirect(url_for('admin_dashboard'))
        return render_template('login.html', error='Credenciales incorrectas', roles=roles)
    return render_template('login.html', roles=roles)

@app.route('/logout')
def logout():
    session.pop('empleado_id', None)
    return redirect(url_for('index'))

# Panel de administración
@app.route('/admin')
def admin_dashboard():
    if 'empleado_id' not in session:
        return redirect(url_for('login'))
    return render_template('admin/dashboard.html')

# CRUD Proveedores
@app.route('/admin/proveedores')
def listar_proveedores():
    proveedores = ProveedorDAO.obtener_todos()
    return render_template('admin/proveedores.html', proveedores=proveedores)

@app.route('/admin/proveedores/agregar', methods=['POST'])
def agregar_proveedor():
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    ProveedorDAO.agregar(nombre, direccion, telefono)
    return redirect(url_for('listar_proveedores'))

@app.route('/admin/proveedores/eliminar/<int:id>')
def eliminar_proveedor(id):
    ProveedorDAO.eliminar(id)
    return redirect(url_for('listar_proveedores'))

# CRUD Empleados
@app.route('/admin/empleados')
def listar_empleados():
    empleados = EmpleadoDAO.obtener_todos()
    return render_template('admin/empleados.html', empleados=empleados)

@app.route('/admin/empleados/agregar', methods=['POST'])
def agregar_empleado():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['correo']
    cargo = request.form['cargo']
    EmpleadoDAO.agregar(nombre, apellido, correo, cargo)
    return redirect(url_for('listar_empleados'))

# CRUD Clientes
@app.route('/admin/clientes')
def listar_clientes():
    clientes = ClienteDAO.obtener_todos()
    return render_template('admin/clientes.html', clientes=clientes)

@app.route('/admin/clientes/agregar', methods=['POST'])
def agregar_cliente():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    correo = request.form['correo']
    ClienteDAO.agregar(nombre, telefono, direccion, correo)
    return redirect(url_for('listar_clientes'))

# CRUD Muebles
@app.route('/admin/muebles')
def listar_muebles():
    muebles = MuebleDAO.obtener_todos()
    return render_template('admin/muebles.html', muebles=muebles)

@app.route('/admin/muebles/agregar', methods=['POST'])
def agregar_mueble():
    tipo = request.form['tipo']
    material = request.form['material']
    dimensiones = request.form['dimensiones']
    color = request.form['color']
    precio = request.form['precio']
    MuebleDAO.agregar(tipo, material, dimensiones, color, precio)
    return redirect(url_for('listar_muebles'))

# Reportes y Gráficos
@app.route('/admin/reportes')
def reportes():
    return render_template('admin/reportes.html')

@app.route('/admin/graficas')
def graficas():
    return render_template('admin/graficas.html')

if __name__ == '__main__':
    app.run(debug=True)
