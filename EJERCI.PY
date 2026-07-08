def mostrarMenu():
    print("""
    ============== MENÚ PRINCIPAL =============
    1. Unidades por tipo de arreglo
    2. Búsqueda de arreglos por rango de precio
    3. Actualizar precio de arreglo
    4. Agregar arreglo
    5. Eliminar arreglo
    6. Salir
    ===========================================""")

def selecionareOpcion():
    try:
        opcion=int(input("Elige una opcion:"))
        if opcion>=1 and opcion <=6:
            return opcion
        else:
            return False
    except:
        False
#============================== OPCION 1 ===============================  
def unidades_tipo(tipoBuscador, diccionarioArreglos, diccionarioBodega):
    tipoBuscador = tipoBuscador.lower().strip()
    total_Stock=0
    for clave_arreglos, valor_arreglos  in diccionarioArreglos.items():

        if valor_arreglos[1] == tipoBuscador:
            for clave_bodega, valorBodega in diccionarioBodega.items():
                if clave_arreglos ==clave_bodega:
                    total_Stock+=valorBodega[1]
                    break
    print("Hay un total de: ",total_Stock, "de tipo de:", tipoBuscador)


#============================== OPCION 2 ===============================
def busqueda_precio(p_min, p_max,diccionarioBodega,diccionarioArreglos):

    lista_a=[]

    for clave_Bodega, valor_Bodega in diccionarioBodega.items():
        if valor_Bodega[0] >= p_min and valor_Bodega[0] >= p_max and valor_Bodega[1] > 0:

            for clave_Arreglos, valor_Arreglos in diccionarioArreglos.items():
                
                if clave_Bodega==clave_Arreglos:
                    lista_a.append(f"{valor_Arreglos[0]} -- {clave_Bodega}")
                    break

    if len(lista_a)==0:
        print("No hay arreglos")
    else:
        lista_a.sort()
        for arreglos in lista_a:
            print(arreglos)
#============================== OPCION 3 ===============================
def buscar_codigo(codigo, diccionario_bodega):
    for codigo_bodega in diccionario_bodega.keys():
        if codigo_bodega==codigo:
            return True
        
    return False

def actualizar_precio(codigo, nuevo_precio, diccionario_bodega):
        if buscar_codigo(codigo, diccionario_bodega)==True:
            valor_bodega=diccionario_bodega[codigo]
            valor_bodega[0]=nuevo_precio
            return True
        else:
            return False

#============================== OPCION 4 ===============================
def codigo_espacios(codigo, diccionario_bodega):
    codigo=codigo.upper().strip()
    for clave in diccionario_bodega.keys():
        if clave == codigo or codigo == "":
            return False
        else:
            return True
        
def nombre_espacio(nombre):
    if nombre.strip()=="":
        return False
    else:
        return True
    
def tipo_sin_espacios(tipo):
    if tipo.strip()=="":
        return False
    else:
        return True
    
def color_sin_espacio(color_principal):
    if color_principal.strip()=="":
        return False
    else: 
        return True

def tipo_tamaño(tamaño):
    tamaño=tamaño.upper()
    if tamaño=="S" or tamaño=="M" or tamaño=="L":
        return True
    else: 
        return False
    
def ver_tarjeta(incluye_tarjeta):
    incluye_tarjeta=incluye_tarjeta.lower()
    if incluye_tarjeta=="s":
        return True
    elif incluye_tarjeta == "n":
        return False
    
def temporada_sin_espacios(temporada):
    if temporada.strip()=="":
        return False
    else:
        return True
    
def precio_mayor_entero(precio):
    try:
        precio=int(precio)
        if precio>0:
            return True
        else:
            return False
    except:
        return False
    
def cantida_de_unidades(unidades):
    try: 
        unidades=int(unidades)
        if unidades>=0:
            return True
        else:
            return False
    except:
        return False

def agregar_arreglo(codigo, nombre, tipo, color_principal, tamaño, incluye_tarjeta, temporada, precio, unidades, diccicionario_arreglos, diccionario_bodega):
    for clave in diccicionario_arreglos.keys():
        if clave!=codigo:
            diccicionario_arreglos.update({codigo:[nombre, tipo, color_principal, tamaño, incluye_tarjeta, temporada]})
            diccionario_bodega.update({codigo:[precio,unidades]})
            return True
        else:
            return False
        
#============================== OPCION 5 ===============================
def eliminar_arreglo(diccionario_arreglo, diccionario_bodega):
    eliminar_codigo=input("Ingresa el codigo para eliminar: ").upper()
    validar_existencia=buscar_codigo(eliminar_codigo, bodega)
    if validar_existencia==True:
        del diccionario_arreglo[eliminar_codigo]
        del diccionario_bodega[eliminar_codigo]
        return True
    else:
        return False


#============================== PROGRAMA PRINCIPAL ===============================

arreglos = {
    'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True,'primavera'],
    'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todoaño'],
    'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
    'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
    'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
    'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno'],
    
   }

bodega = {
    'FLO1': [15990, 8],
    'FLO2': [29990, 3],
    'FLO3': [9990, 12],
    'FLO4': [24990, 5],
    'FLO5': [19990, 0],
    'FLO6': [22990, 6],
 }

while True:
    mostrarMenu()
    opcionValidada=selecionareOpcion()
    match opcionValidada:
        case 1:
            validarTipo=input("Ingresa tipo de ramo: ")
            unidades_tipo(validarTipo, arreglos, bodega)
        case 2:
            while True:
                try:
                    minimo=int(input("ingresa  el minomo de precio: "))
                    maximo=int(input("Ingrese el maximo del precio: "))
                    if minimo<=0 or minimo<maximo:
                       busqueda_precio(minimo, maximo, bodega, arreglos)
                       break
                    else:
                        print("Error...")
                except ValueError:
                    print("Solo se permite valores numericos. Intente de nuevo")     
        case 3:
            while True:
                codigo_arreglo=input("Ingrese el codigo para modificar precio: ").upper().strip()
                while True:
                    try:
                        precio_asignar=int(input("Ingrese un precio para modificarlo: "))
                        if precio_asignar>=0:
                            break
                        else:
                            print("Tiene que ser mayor a \"0\"")
                    except ValueError:
                        print("Solo se permite valores numericos. Intente de nuevo")
                actualizado=actualizar_precio(codigo_arreglo, precio_asignar, bodega)
                if actualizado==True:
                    print("Precio actualizado")
                else:
                    print("El código no existe")

                otro_precio=input("¿Desea ingresar otro precio? (s/n): ").lower()
                if otro_precio== "s":
                    continue
                else:
                    break
            
        case 4:
            codigo=input("Ingrese un codigo: ")
            nombre=input("Ingrese el nombre: ")
            tipo=input("Ingrese que tipo: ")
            color_principal=input("Ingresa el color: ")
            tamaño=input("Ingrese el tamaño \"S/L/M\": ")
            incluye_tarjeta=input("¿Incluira Tarjeta? (s/n): ")
            temporada=input("Ingrese de que termporada es: ")
            precio=input("Ingrese el precio del ramo: ")
            unidades=input("Ingrese cuanta unidades habra: ")

            validar_codigo=codigo_espacios(codigo, arreglos)
            validar_nombre=nombre_espacio(nombre)
            validar_tipo=tipo_sin_espacios(tipo)
            validar_color=color_sin_espacio(color_principal)
            validar_tamaño=tipo_tamaño(tamaño)
            validar_tarjeta=ver_tarjeta(incluye_tarjeta)
            validar_temporada=temporada_sin_espacios(temporada)
            validar_precio=precio_mayor_entero(precio)
            validar_unidades=cantida_de_unidades(unidades)

            if validar_codigo == True and validar_nombre== True and validar_tipo== True and validar_color== True and validar_tamaño == True and validar_temporada== True and validar_precio == True and validar_unidades==True:
                validar_arreglo=agregar_arreglo(codigo, nombre, tipo, color_principal, tamaño, incluye_tarjeta, temporada, precio, unidades, arreglos, bodega)
                if validar_arreglo==True:
                    print("Arreglo agregado")
                else:
                    print("El código ya existe")
            else:
                print("""
                    ====================CONDICIONES PARA AGREGAR=====================
                      ~ CODIGO: No vacío ni solo espacios en blanco, y que no exista ya en lo diccionarios
                      ~ NOMBRE: No vacío ni solo espacios en blanco
                      ~ COLOR: No vacío ni solo espacios en blanco
                      ~ TIPO: No vacío ni solo espacios en blanco
                      ~ TAMAÑO: Debe ser exactamente 'S', 'M' o 'L'
                      ~ TEMPORADA: No vacío ni solo espacios en blanco
                      ~ PRECIO: Número entero mayor que cero
                      ~ UNIDADES: Número entero mayor o igual a cero
                    """)
    
        case 5:
            elimniacion=eliminar_arreglo(arreglos, bodega)
            if elimniacion==True:
                print("Arreglo eliminado")
            else:
                print("El código no existe")

        case 6:
            print("Programa finalizado.....")
            break

