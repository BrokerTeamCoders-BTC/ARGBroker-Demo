from Programacion.database.database import ConexionBaseDeDatos
from Programacion.services.usuario_service import UsuarioService
from Programacion.services.portafolio_service import PortafolioService
from Programacion.utils.validacion_inversor import validar_datos

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
                print(f"\n\n¡Bienvenido, {inversor.get_nombre()}!\n\n")
                
                
                while True:
                    mostrar_menu_principal()
                    opcion_menu = input("\nSeleccione una opción: ")
                    
                    if opcion_menu == "1":
                        datos_cuenta = usuario_service.obtener_datos_cuenta()
                        print(f"\nLos datos de su cuenta son: {datos_cuenta}")
                        pass

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
                            print(f"ID Acción: {activo['id_accion']}")
                            print(f"Nombre Empresa: {activo['nombre_empresa']}")
                            print(f"Símbolo: {activo['simbolo']}")
                            print(f"Cantidad: {activo['cantidad']}")
                            print(f"Precio Compra: {activo['precio_compra']}")
                            print(f"Precio Actual: {activo['precio_actual']}")
                            print(f"Valor Total: {activo['valor_total']}")
                            print(f"Rendimiento: {activo['rendimiento']}%\n")
                        else:
                            print("No se encontraron activos en el portafolio.")
                        pass
                    
                    elif opcion_menu == "3":
                        pass
                    
                    elif opcion_menu == "4":
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