import mysql.connector
import os
import config

def crear_conexion():
    try:
        conexion = mysql.connector.connect (
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        )
        print('✅ Conexión exitosa a la base de datos.')
        return conexion
    except mysql.connector.Error as error:
        print(f'❌ Error al conectar a la base de datos: {error}')
        return None
    
def insertar_producto(conexion, nombre, precio, stock):
        cursor = conexion.cursor()
        try:
            consulta = 'INSERT  INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)'
            datos = (nombre, precio, stock)
            cursor.execute(consulta, datos)
            conexion.commit()
            print('✅ Producto insertado correctamente.') 
        except mysql.connector.Error as error:
            print(f"❌ Error al insertar el producto: {error}")
        finally:
            cursor.close()

def borrar_productos(conexion, producto_id):
    cursor = conexion.cursor()
    try:
        consulta = 'delete from productos where id = %s'
        cursor.execute(consulta, (producto_id,))
        conexion.commit()
        if cursor.rowcount > 0:
            print('✅ Producto eliminado correctamente.')
        else:
            print('⚠️ No se encontró un producto con ese ID.')
    except mysql.connector.Error as error:
        print(f'❌ Error al borrar el producto: {error}')
    finally:
        cursor.close()

def listar_productos(conexion):
    cursor = conexion.cursor()
    try:
        consulta = 'Select * from productos'
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        if resultados:
            print("📦 Productos disponibles:")
            for producto in resultados:
                print(f'ID: {producto[0]} | Nombre: {producto[1]} | Precio: {producto[2]} | Stock: {producto[3]}')
            else:
                print('No hay productos en la base de datos..')
    except mysql.connector.Error as error:
        print(f"❌ Error al listar productos: {error}")
        return []
    finally:
        cursor.close()

def modificar_stock(conexion, producto_id, cantidad):
    cursor = conexion.cursor()
    try:
        consulta = 'update productos set stock = stock + %s where id = %s'
        datos = (cantidad, producto_id)
        cursor.execute(consulta, datos)
        conexion.commit()
        
        if cursor.rowcount > 0:
            print(f'✅ Stock actualizado. Se cambió en {cursor.rowcount} producto(s).')
        else:
            print('❌ No se encontró el producto con ese ID.')
    except mysql.connector.Error as error:
        print(f'❌ Error al modificar el stock: {error}')
    finally:
        cursor.close()

def modificar_precio(conexion, producto_id, cantidad):
    cursor = conexion.cursor()
    try:
        consulta = 'update productos set precio = precio + %s where id = %s'
        datos = (cantidad, producto_id)
        cursor.execute(consulta, datos)
        conexion.commit()
        
        if cursor.rowcount > 0:
            print(f'✅ Precio actualizado. Se cambió en {cursor.rowcount} producto(s).')
        else:
            print('❌ No se encontró el producto con ese ID.')
    except mysql.connector.Error as error:
        print(f'❌ Error al modificar el precio: {error}')
    finally:
        cursor.close()
        
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    
