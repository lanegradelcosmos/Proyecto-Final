
from rsc.Modules import Registros


def app():
    registroseliminados = 0

    agenda = {
        
    }
    while True:
        opcionIngresada = int(
            input(
                """
              𓃡 𓃡 𓃡 𓃡 𓃡 𓃡 𓃡 𓃡 𓃡 𓃡 𓃡 𓃡 𓃡 𓃡                   
              𓃡 𓃡 𓃡  VETERINARIA APP  𓃡 𓃡  
              𓃡 𓃡 𓃡 𓃡 𓃡 𓃡 𓃡 𓃡 𓃡 𓃡 𓃡 𓃡 𓃡 𓃡


            Menú:
            1- Registrar nueva Mascota
            2- Consultar Registro
            3- Modificar un Registro
            4- Eliminar un Registro
            5- Salir
            
            Opción elegida: """
            )
        )

        match opcionIngresada:
            case 1:
                
                print("\n  REGISTRAR    ")
                nombre = input("Ingrese el nombre de la mascota: ")
                sexo = input("Ingrese sexo: ")
                edad = input("Ingrese edad aproximada: ")
                especie = input("Ingrese especie(canino/felino): ")
                rasgos = input("Ingrese rasgos de la mascota:")
                enfermedad = input("Ingrese enfermedad: ")
                duenio = input("Ingrese nombre del dueño: ")
                contacto = input("Ingrese número de contacto: ")

                Registros.registrarMascota(
                    nombre,
                    sexo,
                    edad,
                    especie,
                    rasgos,
                    enfermedad,
                    duenio,
                    contacto,
                    agenda,
                )

            case 2:
               

                if len(agenda) >= 1:
                    print("\n##### REGISTRO TOTAL ######")
                    Registros.verTodosLosRegistros(agenda)
                else:
                    
                    print("\n¡No hay Mascotas registradas!")

            case 3:
                
                if len(agenda) >= 1:
                    
                    Registros.verTodosLosRegistros(agenda)

                    print("\n ♦♦♦♦ MODIFICAR REGISTRO ♦♦♦♦")

                    id = int(input("Ingrese el id del registro a modificar: "))

                    if id in agenda:
                        caractAModificar = input(
                            "\nQue desea actualizar (nombre / sexo / edad / especie / rasgos / enfermedad / duenio / contacto)?: "
                        ).lower()

                        if (
                         caractAModificar == "nombre"
                         or caractAModificar == "sexo"
                         or caractAModificar == "edad" 
                         or caractAModificar == "especie" 
                         or caractAModificar == "rasgos" 
                         or caractAModificar == "enfermedad" 
                         or caractAModificar == "duenio" 
                         or caractAModificar == "contacto" 
                         ):
                            valorActualizar = input(f"Nuevo/a {caractAModificar}: ")
                            Registros.modificarRegistro(
                                agenda, id, caractAModificar, valorActualizar
                            )

                        else:
                            print("\nCaracteristica Invalida")
                    else:
                        print("ID INCORRECTO")
                else:
                    print("\n¡No hay Mascotas registradas!")

            case 4:
                if len(agenda) >= 0:
                    
                    print("\n##### BORRAR TAREA ######")
                    id = int(input("¿Cuál ID desea eliminar?: "))

                
                    if id in agenda.keys():
                        Registros.eliminarTarea(agenda, id)
                        registroseliminados += (
                            1
                        )
                    else:
                        print("ID INCORRECTO")

                else:
                    print("\n¡No hay Mascotas registradas!")
            case 5:
                
                print(
                    f"""    REPORTE FINAL: 
                       Nuevos registros({len(agenda)})
                       Registros eliminados:({registroseliminados})
                      ¡Gracias por utilizar nuestros servicios! 
                      """
                )
                break


if __name__ == "__main__":
    app()
