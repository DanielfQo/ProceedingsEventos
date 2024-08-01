from flask import Blueprint, render_template, session, redirect, url_for, request
from models.entidades.Usuario import Usuario, db

perfil = Blueprint('perfil', __name__)

@perfil.route('/')
def mostrar_perfil():
    if 'usuario_id' not in session:
        return redirect(url_for('inicio_sesion.login'))
    
    usuario_id = session['usuario_id']
    usuario = Usuario.query.get(usuario_id)
    
    if usuario:
        return render_template('vista/assets/HTML/perfil.html', usuario=usuario)
    else:
        return "Usuario no encontrado", 404

@perfil.route('/actualizar', methods=['POST'])
def actualizar_perfil():
    if 'usuario_id' not in session:
        return redirect(url_for('inicio_sesion.login'))
    
    usuario_id = session['usuario_id']
    usuario = Usuario.query.get(usuario_id)
    
    if usuario:
        # Actualiza la información del usuario con los datos del formulario
        usuario.nombres = request.form.get('nombres')
        usuario.apellidos = request.form.get('apellidos')
        usuario.fecha_nacimiento = request.form.get('fecha_nacimiento')
        usuario.nacionalidad = request.form.get('nacionalidad')
        # Añadir código aquí para actualizar otros campos si es necesario
        db.session.commit()
        
        return redirect(url_for('perfil.mostrar_perfil'))
    else:
        return "Usuario no encontrado", 404
