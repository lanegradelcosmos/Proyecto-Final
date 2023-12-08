def registrarMascota(
    nombre, sexo, edad, especie, rasgos, enfermedad, duenio, contacto, registroGeneralMascotas
):
    if len(registroGeneralMascotas) > 0:
       
        ids = list(registroGeneralMascotas.keys())
        ultimoId = ids[len(ids) - 1]
        idRegistro = ultimoId + 1
    else:
        idRegistro = 1

    registroGeneralMascotas[idRegistro] = {
        "nombre": nombre,
        "sexo": sexo,
        "edad": edad,
        "especie": especie,
        "rasgos": rasgos,
        "enfermedad": enfermedad,
        "duenio": duenio,
        "contacto": contacto,
    }


    print("\n¡¡¡Registro Exitoso!!!")


def verTodosLosRegistros(registroGeneralMascotas):
   
    for id, Registro in registroGeneralMascotas.items():
        print(
            f"""             
                ----ID REGISTRO: {id} ----
                Nombre de la Mascota: {Registro["nombre"]}
                Sexo: {Registro["sexo"]}
                Edad: {Registro["edad"]}
                Especie: {Registro["especie"]}
                Rasgos : {Registro["rasgos"]}
                Enfermedad: {Registro["enfermedad"]}
                Nombre del Dueño: {Registro["duenio"]}
                Numero de contacto: {Registro["contacto"]}
                
                  """
        )

def modificarRegistro(registroGeneralMascotas, idModificar, caractModificar, valorActualizar):
    
    registroGeneralMascotas[idModificar][caractModificar] = valorActualizar
    print("\nRegistro actualizado exitosamente")


def eliminarTarea(registroGeneralMascotas, idEliminar):
   
    registroGeneralMascotas.pop(idEliminar)
    print("Registro eliminado exitosamente")
