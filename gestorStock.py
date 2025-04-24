from conexion import os,crear_conexion,insertar_producto, borrar_productos, listar_productos, modificar_stock, modificar_precio, limpiar_pantalla
conexion = crear_conexion()

if conexion:
    while True:
        try:
            limpiar_pantalla()
            print("\n📦 GESTOR DE PRODUCTOS - SUPERMERCADO")
            print("1. Insertar producto")
            print("2. Mostrar productos")
            print("3. Modificar precio")
            print("4. Modificar stock")
            print("5. Borrar producto")
            print("6. Salir")
            
            opcion = input('Ingrese una opcion: ')
            
            if opcion == '1':
                nombre = input('Porfavor ingrese Nombre del producto: ')
                try:
                    precio = float(input('Precio del producto: '))
                    stock = int(input('Stock del producto: '))
                except ValueError:
                    print('❌ Error: el precio debe ser un número decimal y el stock un entero.')
                    continue
                insertar_producto(conexion, nombre, precio, stock)
            
            elif opcion == '2':
                listar_productos(conexion)
                input('\nPresione Enter para continuar...')
            
            elif opcion == '3':
                try:
                    producto_id = int(input('Ingrese el id del producto: '))
                    cantidad = float(input('Ingresá cuánto querés **sumar o restar** al precio actual del producto: '))
                except ValueError:
                    print('Error: debe ingresar un id valido o un numero para el precio. ')
                modificar_precio(conexion, producto_id, cantidad)
                
            elif opcion == '4':
                try:
                    producto_id = int(input('Ingrese el id del producto: '))
                    cantidad = float(input('Ingresá cuánto querés **sumar o restar** al stock actual del producto: '))
                except ValueError:
                    print('Error: debe ingresar un id valido o un numero para el stock. ')
                modificar_stock(conexion, producto_id,cantidad)
                
            elif opcion == '5':
                try:
                    producto_id = int(input('Ingrese el id del producto que desea borrar: '))
                    borrar_productos(conexion, producto_id)
                except ValueError:
                    print('Ingrese un ID valido...')
                    
            elif opcion == '6':
                print('Gracias por usar el gestor. ¡Hasta luego!')
                break
            else:
                input('Ingrese una opcion valida...')
                
        except ValueError as error:
            print(f'Hubo un error: {error}')
    
    conexion.close()
