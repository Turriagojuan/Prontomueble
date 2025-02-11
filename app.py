from flask import Flask, render_template, request, redirect, url_for, session, flash
from persistencia.conexion import Conexion
from persistencia.proveedorDAO import ProveedorDAO
from persistencia.empleadoDAO import EmpleadoDAO
from persistencia.clienteDAO import ClienteDAO
from persistencia.muebleDAO import MuebleDAO
from persistencia.cargoDAO import CargoDAO
from persistencia.tipoDAO import TipoDAO
from persistencia.colorDAO import ColorDAO
from persistencia.materialDAO import MaterialDAO
from persistencia.suministraDAO import SuministraDAO
from persistencia.reporteDAO import ReporteDAO


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
    if request.method == 'POST':
        id = request.form['id']
        empleado = EmpleadoDAO.autenticar(id)
        if empleado:
            if empleado[0] == 1:
                session['empleado_id'] = id
                return redirect(url_for('admin_dashboard'))
            elif empleado[0] == 2:
                session['empleado_id'] = id
                return redirect(url_for('index'))
        return render_template('login.html', error='Credenciales incorrectas')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('empleado_id', None)
    return redirect(url_for('index'))

# Panel de administración
@app.route('/admin')
def admin_dashboard():
    if 'empleado_id' not in session:
        return redirect(url_for('login'))
    usuario = EmpleadoDAO.obtener_por_id(session['empleado_id'])
    return render_template('admin/dashboard.html', usuario=usuario)

# CRUD Proveedores
@app.route('/admin/proveedores')
def listar_proveedores():
    proveedores = ProveedorDAO.obtener_todos()
    return render_template('admin/proveedores/proveedores.html', proveedores=proveedores)

@app.route('/admin/proveedores/agregar', methods=['POST'])
def agregar_proveedor():
    id = request.form['id']
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    ProveedorDAO.agregar(id, nombre, direccion, telefono)
    flash('Proveedor agregado con éxito.')
    return redirect(url_for('listar_proveedores'))

@app.route('/admin/proveedores/editar/<int:id>', methods=['GET', 'POST'])
def editar_proveedor(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        ProveedorDAO.actualizar(id, nombre, direccion, telefono)
        flash('Proveedor actualizado con éxito.')
        return redirect(url_for('listar_proveedores'))
    proveedor = ProveedorDAO.obtener_por_id(id)
    return render_template('admin/proveedores/editar_proveedor.html', proveedor=proveedor)

@app.route('/admin/proveedores/eliminar/<int:id>')
def eliminar_proveedor(id):
    ProveedorDAO.eliminar(id)
    flash('Proveedor eliminado con éxito.')
    return redirect(url_for('listar_proveedores'))

# CRUD Empleados
@app.route('/admin/empleados')
def listar_empleados():
    empleados = EmpleadoDAO.obtener_todos_con_cargo()
    cargos = CargoDAO.obtener_todos()
    return render_template('admin/empleados/empleados.html', empleados=empleados, cargos=cargos)

@app.route('/admin/empleados/agregar', methods=['POST'])
def agregar_empleado():
    id = request.form['id']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['correo']
    cargo = request.form['cargo']
    EmpleadoDAO.agregar(id, nombre, apellido, correo, cargo)
    flash('Empleado agregado con éxito.')
    return redirect(url_for('listar_empleados'))

@app.route('/admin/empleados/editar/<int:id>', methods=['GET', 'POST'])
def editar_empleado(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        cargo = request.form['cargo']
        EmpleadoDAO.actualizar(id, nombre, apellido, correo, cargo)
        flash('Empleado actualizado con éxito.')
        return redirect(url_for('listar_empleados'))
    empleado = EmpleadoDAO.obtener_por_id(id)
    cargos = CargoDAO.obtener_todos()
    return render_template('admin/empleados/editar_empleados.html', empleado=empleado, cargos=cargos)

@app.route('/admin/empleados/eliminar/<int:id>')
def eliminar_empleado(id):
    EmpleadoDAO.eliminar(id)
    flash('Empleado eliminado con éxito.')
    return redirect(url_for('listar_empleados'))

# CRUD Clientes
@app.route('/admin/clientes')
def listar_clientes():
    clientes = ClienteDAO.obtener_todos()
    return render_template('admin/clientes/clientes.html', clientes=clientes)

@app.route('/admin/clientes/agregar', methods=['POST'])
def agregar_cliente():
    id = request.form['id']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    direccion = request.form['direccion']
    correo = request.form['correo']
    ClienteDAO.agregar(id, nombre, apellido, direccion, correo)
    flash('Cliente agregado con éxito.')
    return redirect(url_for('listar_clientes'))

@app.route('/admin/clientes/editar/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        direccion = request.form['direccion']
        correo = request.form['correo']
        ClienteDAO.actualizar( id,nombre,apellido, direccion, correo)
        flash('Cliente actualizado con éxito.')
        return redirect(url_for('listar_clientes'))
    cliente = ClienteDAO.obtener_por_id(id)
    return render_template('admin/clientes/editar_clientes.html', cliente=cliente)

@app.route('/admin/clientes/eliminar/<int:id>')
def eliminar_cliente(id):
    ClienteDAO.eliminar(id)
    flash('Cliente eliminado con éxito.')
    return redirect(url_for('listar_clientes'))

# CRUD Muebles
@app.route('/admin/muebles')
def listar_muebles():
    muebles = MuebleDAO.obtener_todos()
    tipos = TipoDAO.obtener_todos()
    colores = ColorDAO.obtener_todos()
    materiales = MaterialDAO.obtener_todos()
    proveedores = ProveedorDAO.obtener_todos()
    return render_template('admin/muebles/muebles.html', muebles=muebles, tipos=tipos, colores=colores, materiales=materiales, proveedores=proveedores)

@app.route('/admin/muebles/agregar', methods=['POST'])
def agregar_mueble():
    nombre = request.form['nombre']
    material = request.form['material']
    color = request.form['color']
    precio = request.form['precio']
    cantidad = request.form['cantidad']
    tipo = request.form['tipo']
    alto = request.form['alto']
    largo = request.form['largo']
    ancho = request.form['ancho']
    proveedor = request.form['proveedor']
    MuebleDAO.agregar(nombre, alto, largo, ancho, material, color, tipo)
    mueble_id = MuebleDAO.obtener_ultimo_id()  # Assuming this method exists to get the last inserted mueble ID
    SuministraDAO.agregar(proveedor, mueble_id, cantidad, precio)
    flash('Mueble agregado con éxito.')
    return redirect(url_for('listar_muebles'))

@app.route('/admin/muebles/eliminar/<int:id>')
def eliminar_mueble(id):
    MuebleDAO.eliminar(id)
    flash('Mueble eliminado con éxito.')
    return redirect(url_for('listar_muebles'))

@app.route('/admin/muebles/editar/<int:id>', methods=['GET', 'POST'])
def editar_mueble(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        material = request.form['material']
        color = request.form['color']
        tipo = request.form['tipo']
        alto = request.form['alto']
        largo = request.form['largo']
        ancho = request.form['ancho']
        MuebleDAO.actualizar(id, nombre,alto, largo, ancho, material, color,tipo)
        flash('Mueble actualizado con éxito.')
        return redirect(url_for('listar_muebles'))
    mueble = MuebleDAO.obtener_por_id(id)
    tipos = TipoDAO.obtener_todos()
    colores = ColorDAO.obtener_todos()
    materiales = MaterialDAO.obtener_todos()
    proveedores = ProveedorDAO.obtener_todos()
    return render_template('admin/muebles/editar_muebles.html', mueble=mueble, tipos=tipos, colores=colores, materiales=materiales, proveedores=proveedores)


# Reportes y Gráficos
@app.route('/reportes')
def reportes():
    mes = request.args.get('mes', default=1, type=int)
    anio = request.args.get('anio', default=2023, type=int)
    vendedores = ReporteDAO.vendedor_mas_ventas(mes, anio)
    clientes_nuevos = ReporteDAO.clientes_nuevos(mes, anio)
    clientes_top = ReporteDAO.clientes_mayores_compras(mes, anio)
    muebles_top = ReporteDAO.muebles_mas_vendidos(mes, anio)
    return render_template('admin/reportes.html', mes=mes, anio=anio, vendedores=vendedores, clientes_nuevos=clientes_nuevos, clientes_top=clientes_top, muebles_top=muebles_top)
@app.route('/graficas')
def graficas():
    mes = request.args.get('mes', default=1, type=int)
    anio = request.args.get('anio', default=2023, type=int)
    muebles_top = ReporteDAO.muebles_mas_vendidos(mes, anio)
    return render_template('admin/graficas.html', muebles_top=muebles_top)
if __name__ == '__main__':
    app.run(debug=True)

