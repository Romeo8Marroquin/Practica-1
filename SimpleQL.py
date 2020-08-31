import json
import webbrowser
comando = ["Hola"]
dato = ["Nombre", "Edad", "Activo", "Promedio"]
datos = [dato]
restriccion = ""
validador = 0
print(" ")
print("Ingrese comando...")
while comando[0].lower() != "cerrar" and comando[0].lower() != "salir":
    salida = ""
    print(" ")
    cmd = input()
    comando = cmd.split()





    # Si el comando es cargar:
    if comando[0].lower() == "cargar":
        archivos = [""]
        for i in comando:
            if i.lower() != "cargar":
                archivos.append(i.split(",")[0])
        archivos.pop(0)
        for i in archivos:
            with open(i) as arch:
                data = json.load(arch)
                for registro in data:
                    nuevoReg = [registro["nombre"], registro["edad"], registro["activo"], registro["promedio"]]
                    datos.append(nuevoReg)





    # Si el comando es seleccionar:
    elif comando[0].lower() == "seleccionar":
        # Si es un seleccionar todo:
        if comando[1] == "*":
            # Si es un seleccionar todo con condición:
            if len(comando) >= 4:
                res1 = cmd.lower().split(" donde ")
                res2 = res1[1].split("=")
                restriccion = res2[0].split()
                res3 = res2[1].split('"')
                if len(res3) > 1:
                    restriccion.append(res3[1])
                else:
                    restriccion.append(res3[0])
                r1 = len(datos)
                for i in range(r1):
                    if i == 0:
                        r2 = len(datos[i])
                        for j in range(r2):
                            esp = 20 - len(str(datos[i][j]))
                            salida += str(datos[i][j])
                            r3 = esp
                            for var in range(r3):
                                salida += " "
                        salida += "\n"
                    else:
                        indice = -1
                        r2 = len(datos[i])
                        if restriccion[0].lower() == "nombre":
                            if str(restriccion[1].lower()) == str(datos[i][0]):
                                indice = 1
                        elif str(restriccion[0].lower()) == "edad":
                            if restriccion[1].lower() == str(datos[i][1]):
                                indice = 1
                        elif str(restriccion[0].lower()) == "activo":
                            if restriccion[1].lower() == str(datos[i][2]).lower():
                                indice = 1
                        elif str(restriccion[0].lower()) == "promedio":
                            if restriccion[1].lower() == str(datos[i][3]):
                                indice = 1
                        if indice == 1:
                            for j in range(r2):
                                esp = 20 - len(str(datos[i][j]))
                                salida += str(datos[i][j])
                                r3 = esp
                                for var in range(r3):
                                    salida += " "
                            salida += "\n"
                print(salida)
            # Si es un seleccionar todo sin condición:
            elif len(comando) == 2:
                r1 = len(datos)
                for i in range(r1):
                    r2 = len(datos[i])
                    for j in range(r2):
                        esp = 20 - len(str(datos[i][j]))
                        salida += str(datos[i][j])
                        r3 = esp
                        for var in range(r3):
                            salida += " "
                    salida += "\n"
                print(salida)
        # Si el comando es Seleccionar por campos:
        else:
            columnas = [0]
            res1 = cmd.lower().split(" donde ")
            # Si el comando es Seleccionar por campos con restricción:
            if len(res1) > 1:
                campos = [""]
                temp = res1[0].split(" ")
                for i in temp:
                    campos.append(i.split(",")[0])
                campos.pop(0)
                campos.pop(0)
                for k in range(len(campos)):
                    if campos[k].lower() == "nombre":
                        columnas.append(0)
                    elif campos[k].lower() == "edad":
                        columnas.append(1)
                    elif campos[k].lower() == "activo":
                        columnas.append(2)
                    elif campos[k].lower() == "promedio":
                        columnas.append(3)
                columnas.pop(0)
                res1 = cmd.lower().split(" donde ")
                res2 = res1[1].split("=")
                restriccion = res2[0].split()
                res3 = res2[1].split('"')
                if len(res3) > 1:
                    restriccion.append(res3[1])
                else:
                    restriccion.append(res3[0])
                r1 = len(datos)
                for i in range(r1):
                    if i == 0:
                        r2 = len(columnas)
                        for j in range(r2):
                            esp = 20 - len(str(datos[i][columnas[j]]))
                            salida += str(datos[i][columnas[j]])
                            r3 = esp
                            for var in range(r3):
                                salida += " "
                        salida += "\n"
                    else:
                        indice = -1
                        r2 = len(columnas)
                        if restriccion[0].lower() == "nombre":
                            if str(restriccion[1].lower()) == str(datos[i][0]):
                                indice = 1
                        elif str(restriccion[0].lower()) == "edad":
                            if restriccion[1].lower() == str(datos[i][1]):
                                indice = 1
                        elif str(restriccion[0].lower()) == "activo":
                            if restriccion[1].lower() == str(datos[i][2]).lower():
                                indice = 1
                        elif str(restriccion[0].lower()) == "promedio":
                            if restriccion[1].lower() == str(datos[i][3]):
                                indice = 1
                        if indice == 1:
                            for j in range(r2):
                                esp = 20 - len(str(datos[i][columnas[j]]))
                                salida += str(datos[i][columnas[j]])
                                r3 = esp
                                for var in range(r3):
                                    salida += " "
                            salida += "\n"
                print(salida)
            # Si el comando es Seleccionar sin restricción:
            else:
                campos = [""]
                temp = res1[0].split(" ")
                for i in temp:
                    campos.append(i.split(",")[0])
                campos.pop(0)
                campos.pop(0)
                for k in range(len(campos)):
                    if campos[k].lower() == "nombre":
                        columnas.append(0)
                    elif campos[k].lower() == "edad":
                        columnas.append(1)
                    elif campos[k].lower() == "activo":
                        columnas.append(2)
                    elif campos[k].lower() == "promedio":
                        columnas.append(3)
                columnas.pop(0)
                r1 = len(datos)
                for i in range(r1):
                    r2 = len(columnas)
                    for j in range(r2):
                        esp = 20 - len(str(datos[i][columnas[j]]))
                        salida += str(datos[i][columnas[j]])
                        r3 = esp
                        for var in range(r3):
                            salida += " "
                    salida += "\n"
                print(salida)





    # Si el comando es Maximo:
    elif comando[0].lower() == "maximo":
        # Si el comando es Máximo por edad:
        if comando[1].lower() == "edad":
            indice = len(datos) - 1
            for i in range(len(datos)):
                reg = len(datos) - 1 - i
                if reg != 0 and indice != 0:
                    if int(datos[reg][1]) > int(datos[indice][1]):
                        indice = reg
            r2 = len(datos[i])
            for j in range(len(datos[0])):
                esp = 20 - len(str(datos[0][j]))
                salida += str(datos[0][j])
                r3 = esp
                for var in range(r3):
                    salida += " "
            salida += "\n"
            for j in range(len(datos[indice])):
                esp = 20 - len(str(datos[indice][j]))
                salida += str(datos[indice][j])
                r3 = esp
                for var in range(r3):
                    salida += " "
            salida += "\n"
            print(salida)
        # Si el comando es máximo por promedio:
        elif comando[1].lower() == "promedio":
            indice = len(datos) - 1
            for i in range(len(datos)):
                reg = len(datos) - 1 - i
                if reg != 0 and indice != 0:
                    if float(datos[reg][3]) > float(datos[indice][3]):
                        indice = reg
            r2 = len(datos[i])
            for j in range(len(datos[0])):
                esp = 20 - len(str(datos[0][j]))
                salida += str(datos[0][j])
                r3 = esp
                for var in range(r3):
                    salida += " "
            salida += "\n"
            for j in range(len(datos[indice])):
                esp = 20 - len(str(datos[indice][j]))
                salida += str(datos[indice][j])
                r3 = esp
                for var in range(r3):
                    salida += " "
            salida += "\n"
            print(salida)





    # Si el comando es Minimo:
    elif comando[0].lower() == "minimo":
        # Si el comando es minimo por edad:
        if comando[1].lower() == "edad":
            indice = len(datos) - 1
            for i in range(len(datos)):
                reg = len(datos) - 1 - i
                if reg != 0 and indice != 0:
                    if int(datos[reg][1]) < int(datos[indice][1]):
                        indice = reg
            r2 = len(datos[i])
            for j in range(len(datos[0])):
                esp = 20 - len(str(datos[0][j]))
                salida += str(datos[0][j])
                r3 = esp
                for var in range(r3):
                    salida += " "
            salida += "\n"
            for j in range(len(datos[indice])):
                esp = 20 - len(str(datos[indice][j]))
                salida += str(datos[indice][j])
                r3 = esp
                for var in range(r3):
                    salida += " "
            salida += "\n"
            print(salida)
        # Si el comando es mínimo por promedio:
        elif comando[1].lower() == "promedio":
            indice = len(datos) - 1
            for i in range(len(datos)):
                reg = len(datos) - 1 - i
                if reg != 0 and indice != 0:
                    if float(datos[reg][3]) < float(datos[indice][3]):
                        indice = reg
            r2 = len(datos[i])
            for j in range(len(datos[0])):
                esp = 20 - len(str(datos[0][j]))
                salida += str(datos[0][j])
                r3 = esp
                for var in range(r3):
                    salida += " "
            salida += "\n"
            for j in range(len(datos[indice])):
                esp = 20 - len(str(datos[indice][j]))
                salida += str(datos[indice][j])
                r3 = esp
                for var in range(r3):
                    salida += " "
            salida += "\n"
            print(salida)
    





    # Si el comando es Suma:
    elif comando[0].lower() == "suma":
        # Si el comando es Suma de edad:
        if comando[1].lower() == "edad":
            acum = 0
            for i in range(len(datos)):
                if i != 0:
                    acum += int(datos[i][1])
            print("Sumatoria de edades = ", acum)
        # Si el comando es Suma de promedio:
        if comando[1].lower() == "promedio":
            acum = 0
            for i in range(len(datos)):
                if i != 0:
                    acum += float(datos[i][3])
            print("Sumatoria de promedios = ", acum)





    # Si el comando es Cuenta:
    elif comando[0].lower() == "cuenta":
        # Si el comando es Suma de edad:
        acum = 0
        for i in range(len(datos)):
            if i != 0:
                acum += 1
        print("Número de datos = ", acum)





    # Si el comando es Reportar N:
    elif comando[0].lower() == "reportar":
        n = int(comando[1])
        if n > 0 and n <= (len(datos) - 1):
            tabla = ""
            for i in range(n+1):
                tabla += "<tr>"
                if i == 0:
                    tabla += "<td class='celda'>No.</td>"
                else:
                    tabla += "<td class='celda'>" + str(i) + "</td>"
                for j in range(len(datos[0])):
                    nuevoR = "<td class='celda'>" + str(datos[i][j]) + "</td>"
                    tabla += nuevoR
                tabla += "</tr>"
            pagina = """
            <html>
            <head>
            <title></title>
            <style>
                body{
                    background-color:black;
                    font-size:100%;
                    font-family:Time New Roman;
                }
                #tab{
                    width:60%;
                    background-color:black;
                    border:3px solid white;
                    color:white;
                    border-radius:10px;
                    font-family: "Times New Roman";
                    text-align:center;
                }
                h1{
                    text-align:center;
                    font-family: "Times New Roman";
                    color:white;
                }
                .celda{
                    background-color:rgb(20,20,20);
                    text-align:center;
                    font-family: "Times New Roman";
                    padding:5px 10px;
                    border:1px solid white;
                    border-radius:3px;
                }
                footer{
                    position:fixed;
                    top:96%;
                    left:1%;
                    color:white;
                    font-size:90%;
                    font-family: "Times New Roman";

                }
            </style>
            </head>
            <body><br><h1>Reporte de """ + str(n) + """ datos</h1><br>
            <center>
                <table id="tab">
                    """ + tabla + """
                </table><br><br><br>
            </center>
            <footer>Todos los derechos reservados por Romeo Ernesto Marroquín Sánchez (Meoer8Marsan)</footer>
            </body>
            </html>"""
            reporte = open('Reporte.html', 'w')
            reporte.write(pagina)
            reporte.close()
            webbrowser.open_new_tab('Reporte.html')
        else:
            print("Ingreso no válido")
exit()