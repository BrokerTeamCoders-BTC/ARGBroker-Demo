from database.database import ConexionBaseDeDatos
from services.usuario_service import UsuarioService
from services.portafolio_service import PortafolioService
from services.operacion_service import OperacionService
from services.accion_service import AccionService
from utils.validacion_inversor import validar_datos

def mostrar_menu_principal():
    print("\n1. Ver datos de la cuenta")
    print("2. Listar activos del portafolio")
    print("3. Comprar acciones")
    print("4. Vender acciones")
    print("5. Cerrar sesión")

def main():
    db = ConexionBaseDeDatos()
    db.conectar()

    usuario_service = UsuarioService(db)
    
    portafolio_service = PortafolioService(db)

    operacion_service = OperacionService(db)

    accion_service = AccionService(db)


    print("\n------------ BIENVENIDO A ARGBROKER ------------")

    while True:
        print("\n1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            datos = validar_datos()
            usuario_service.registrar_inversor(*datos)
            print("\nInversor creado correctamente. Inicie sesión para operar.")

        elif opcion == "2":
            correo = input("\nCorreo: ")
            contrasenia = input("Contraseña: ")
            inversor = usuario_service.iniciar_sesion(correo, contrasenia)
            
            if inversor:
                print(f"\n\n¡Bienvenido, {inversor.get_nombre()}!\n")
                
                
                while True:
                    mostrar_menu_principal()
                    opcion_menu = input("\nSeleccione una opción: ")
                    
                    if opcion_menu == "1":
                        datos_usuario = usuario_service.obtener_datos_cuenta()
                        datos_cuenta = portafolio_service.obtener_datos_cuenta(inversor.get_id_inversor())

                        print(f"\nLos datos de su cuenta son: \n\n {datos_usuario}")
                        print(f"\nSaldo: {datos_cuenta['saldo']}")
                        print(f"Total invertido: {datos_cuenta['total_invertido']}")
                        print(f"Valor actual: {datos_cuenta['valor_total_actual']}")
                        print(f"Rendimiento: {datos_cuenta['rendimiento_total']}")

                    elif opcion_menu == "2":
                         # Verifica si el usuario ha iniciado sesión
                        if not usuario_service.usuario:
                            print("Debe iniciar sesión primero.")
                        else:
                        # Utiliza el id del inversor logueado
                            id_inversor = usuario_service.usuario.get_id_inversor()
                            activos = portafolio_service.listar_activos(id_inversor)
                
                        # Mostrar activos del portafolio
                        if activos:
                            print("\nActivos en el portafolio:")
                            for activo in activos:
                                print(f"\nID Acción: {activo['id_accion']}")
                                print(f"Nombre Empresa: {activo['nombre_empresa']}")
                                print(f"Símbolo: {activo['simbolo']}")
                                print(f"Cantidad: {activo['cantidad']}")
                                print(f"Precio Compra: {activo['precio_compra']}")
                                print(f"Precio Actual: {activo['precio_actual']}")
                                print(f"Valor Total: {activo['valor_total']}")
                                print(f"Rendimiento: {activo['rendimiento']}%\n")
                                print("----------------------------------------------")
                        else:
                            print("No se encontraron activos en el portafolio.")
                        pass
                    
                    elif opcion_menu == "3":
                        # Listar las acciones disponibles para la compra
                        acciones = accion_service.armar_listado_acciones()
                        if acciones:
                            print("\nAcciones disponibles:")
                            for accion in acciones:
                                print(f"ID: {accion['id_accion']}, Nombre: {accion['nombre_empresa']}, Precio: {accion['precio_compra']}")

                            id_accion = input("\nIngrese el ID de la acción que desea comprar: ")
                            cantidad = int(input("Ingrese la cantidad de acciones a comprar: "))

                            try:
                                id_inversor = usuario_service.usuario.get_id_inversor()  # Obtener ID del inversor logueado
                                operacion_service.realizar_compra(id_inversor, id_accion, cantidad)  # Ejecutar la compra
                                print("Compra realizada con éxito.")
                            except ValueError as e:
                                print(f"Error en la compra: {e}")

                        else:
                            print("No hay acciones disponibles para comprar.")
                        pass
                    
                    elif opcion_menu == "4":
                        # Verifica si el usuario ha iniciado sesión
                        if not usuario_service.usuario:
                            print("Debe iniciar sesión primero.")
                        else:
                        # Utiliza el id del inversor logueado
                            id_inversor = usuario_service.usuario.get_id_inversor()
                            activos = portafolio_service.listar_activos(id_inversor)
                
                        # Mostrar activos del portafolio
                        if activos:
                            print("\nActivos en el portafolio:")
                            for accion in activos:
                                print(f"ID: {accion['id_accion']}, Nombre: {accion['nombre_empresa']}, Precio venta actual: {accion['precio_actual']}, Rendimiento: {accion['rendimiento']}%, Cantidad de acciones: {accion['cantidad']}, Total en cartera: {accion['valor_total']}")   
                        else:
                            print("No se encontraron activos en el portafolio.")
                        id_accion = input("\nIngrese el ID de la acción que desea vender: ")
                        cantidad = int(input("Ingrese la cantidad de acciones a vender: "))
                        try: 
                            operacion_service.realizar_venta(id_inversor, id_accion, cantidad)
                            print("Venta realizada con exito: ")
                        except Exception as e:
                            print(f"Error en la venta: {e}")
                        pass

                    elif opcion_menu == "5":
                        break

                    else: 
                        print("Seleccione una opción correcta.")
            else:
                print("\n¡El correo o contraseña incorrectos!.")

        elif opcion == "3":
            break

        else:
            print("Seleccione una opción correcta")

    db.desconectar()

if __name__ == "__main__":
    main()