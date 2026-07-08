juegos = {
    'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
    'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
    'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
    'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
    'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
    'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate']
}

inventario = {
    'G001': [9990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2]
}

def stock_plataforma(plataforma):
    total_stock = 0
    for codigo, datos in juegos.items():
        if datos[1].lower() == plataforma.lower():
            total_stock += inventario[codigo][1]
    print(f"El total de stock disponibles es: {total_stock}")

def busqueda_precio(p_min, p_max):
    resultados = []
    for codigo, datos_inv in inventario.items():
        precio = datos_inv[0]
        stock = datos_inv[1]
        if p_min <= precio <= p_max and stock > 0:
            titulo = juegos[codigo][0]
            resultados.append(f"{titulo}--{codigo}")
            
    if len(resultados) == 0:
        print("No hay juegos en ese rango de precios.")
    else:
        resultados.sort()
        print(f"Los juegos encontrados son: {resultados}")

def actualizar_precio(codigo, nuevo_precio):
    cod_upper = codigo.upper()
    if cod_upper in inventario:
        inventario[cod_upper][0] = nuevo_precio
        return True
    return False

def validar_codigo(codigo):
    return codigo.strip() != "" and codigo.upper() not in juegos

def validar_texto(texto):
    return texto.strip() != ""

def validar_clasificacion(clasificacion):
    return clasificacion.upper() in ['E', 'T', 'M']

def validar_multiplayer(opcion):
    return opcion.lower() in ['s', 'n']

def validar_precio(precio):
    return precio > 0

def validar_stock(stock):
    return stock >= 0

def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock):
    cod_upper = codigo.upper()
    if cod_upper in juegos:
        return False
    es_multiplayer = True if multiplayer.lower() == 's' else False
    juegos[cod_upper] = [titulo, plataforma, genero, clasificacion.upper(), es_multiplayer, editor]
    inventario[cod_upper] = [precio, stock]
    return True

def eliminar_juego(codigo):
    cod_upper = codigo.upper()
    if cod_upper in juegos:
        del juegos[cod_upper]
        del inventario[cod_upper]
        return True
    return False

def menu_principal():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Stock por plataforma")
        print("2. Búsqueda de juegos por rango de precio")
        print("3. Actualizar precio de juego")
        print("4. Agregar juego")
        print("5. Eliminar juego")
        print("6. Salir")
        print("=====================================")
        
        opcion = input("Ingrese opción: ")
        
        if opcion == "1":
            plat = input("Ingrese plataforma a consultar: ")
            stock_plataforma(plat)
            
        elif opcion == "2":
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        busqueda_precio(p_min, p_max)
                        break
                    else:
                        print("Debe ingresar valores enteros válidos (mínimo menor que máximo).")
                except ValueError:
                    print("Debe ingresar valores enteros")
                    
        elif opcion == "3":
            while True:
                cod = input("Ingrese código del juego: ")
                try:
                    _precio = int(input("Ingrese nuevo precio: "))
                    if _precio > 0:
                        if actualizar_precio(cod, _precio):
                            print("Precio actualizado")
                        else:
                            print("El código no existe")
                    else:
                        print("El precio debe ser un entero positivo.")
                except ValueError:
                    print("Debe ingresar un valor entero para el precio.")
                
                otra = input("¿Desea actualizar otro precio (s/n)?: ").lower()
                if otra == 'n':
                    break
                    
        elif opcion == "4":
            print("--- Registrar Nuevo Juego ---")
            cod = input("Ingrese código del juego: ")
            tit = input("Ingrese título: ")
            plat = input("Ingrese plataforma: ")
            gen = input("Ingrese género: ")
            clas = input("Ingrese clasificación: ")
            mult = input("¿Es multiplayer? (s/n): ")
            edit = input("Ingrese editor: ")
            
            try:
                prec = int(input("Ingrese precio: "))
                stk = int(input("Ingrese stock: "))
            except ValueError:
                print("Error: Precio y Stock deben ser números enteros.")
                continue

            if not validar_codigo(cod):
                print("Error: Código inválido o ya existente.")
            elif not validar_texto(tit):
                print("Error: El título no puede estar vacío.")
            elif not validar_texto(plat):
                print("Error: La plataforma no puede estar vacía.")
            elif not validar_texto(gen):
                print("Error: El género no puede estar vacío.")
            elif not validar_clasificacion(clas):
                print("Error: La clasificación debe ser 'E', 'T' o 'M'.")
            elif not validar_multiplayer(mult):
                print("Error: En multiplayer debe ingresar 's' o 'n'.")
            elif not validar_texto(edit):
                print("Error: El editor no puede estar vacío.")
            elif not validar_precio(prec):
                print("Error: El precio debe ser mayor a cero.")
            elif not validar_stock(stk):
                print("Error: El stock debe ser mayor o igual a cero.")
            else:
                if agregar_juego(cod, tit, plat, gen, clas, mult, edit, prec, stk):
                    print("Juego agregado")
                else:
                    print("El código ya existe")
                    
        elif opcion == "5":
            cod = input("Ingrese código del juego que desea eliminar: ")
            if eliminar_juego(cod):
                print("Juego eliminado")
            else:
                print("El código no existe")
                
        elif opcion == "6":
            print("Programa finalizado.")
            break
        else:
            print("Debe seleccionar una opción válida")

if __name__ == "__main__":
    menu_principal()
