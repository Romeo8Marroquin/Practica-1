# SimpleQL

(Manual de Usuario)

## Descripción

_SimpleQL es una aplicación desarrollada en python con el fin de facilitar la gestión de archivos que estén en formato .json, la aplicación tiene la capacidad de cargar uno o varios archivos .json para realizar una tabla de los registros ingresados para poderlos gestionar de mejor manera._
_El manejo de la aplicación es como el de una consola cualquiera, en este caso estamos hablando de un "lenguaje" tipo declarativo, el cual consiste en ingresar el comando y presionar la tecla ENTER para ejecutarlo._

### Funcionamiento

_SimpleQL posee 8 comandos diferentes los cuales ayudan al usuario a interactuar con la interfaz de programación, además de que los códigos ingresados son insensibles a las mayúsculas, estos códigos se especifican a continuación:_

```
CARGAR archivo1.json, archivo2.json, ..., archivoN.json
SELECCIONAR Promedio, Edad, Nombre DONDE promedio=12.84
MAXIMO promedio
MINIMO edad
SUMA promedio
CUENTA
REPORTAR n
CERRAR
```

### Comando CARGAR

_El comando CARGAR se encarga de cargar los datos de uno o más archivos .json a la memoria del dispositivo, los archivos deben ir separados por coma y espacio uno del otro._

_Nota: No existe un límite para subir archivos, por lo que la única limitante es el hardware del usuario._

```
CARGAR seccionA.json, seccionB.json, seccionC.json
```

### Comando SELECCIONAR

_El comando SELECCIONAR se encarga de mostrar los datos que se han cargado a memoria, además que se pueden seleccionar todos (*) o solo algunos campos indicando el nombre de la columna que se desea mostrar, adicionalmente, con la extensión DONDE es posible añadir una restricción que se limita únicamente a igualación de un campo con un valor específico._

_Nota: Si alguno de los campos es mal ingresado la aplicación se cerrará inmediatamente._

```
SELECCIONAR * DONDE Activo=True
```

### Comando MAXIMO

_El comando MAXIMO se encarga de buscar el valor máximo de un campo dentro de toda la tabla con los datos ingresados anteriormente._

_Nota: Solo es posible ingresar dos campos en este comando, en este caso solo se admiten los campos Edad y Promedio (valores numéricos)._

```
MAXIMO promedio
```

### Comando MINIMO

_El comando MINIMO se encarga de buscar el valor mínimo de un campo dentro de toda la tabla con los datos ingresados anteriormente._

_Nota: Solo es posible ingresar dos campos en este comando, en este caso solo se admiten los campos Edad y Promedio (valores numéricos)._

```
MINIMO edad
```

### Comando SUMA

_El comando SUMA se encarga de calcular el valor numérico total de un campo dentro de la tabla con los datos ingresados anteriormente._

_Nota: Solo es posible ingresar dos campos en este comando, en este caso solo se admiten los campos Edad y Promedio (valores numéricos)._

```
SUMA promedio
```

### Comando CUENTA

_El comando CUENTA se encarga de calcular el número de registros actuales que hay dentro de la tabla con los datos ingresados anteriormente._

_Nota: Este comando no admite ningún parámetro para su uso._

```
CUENTA
```

### Comando REPORTAR n

_El comando REPORTAR se encarga de realizar un reporte HTML estilizado con CSS utilizando el número de registros ingresados, los cuales son los n primeros registros que hay dentro de la tabla con los datos ingresados anteriormente._

_Nota: Este comando no admite 0 registros, ni tampoco más registros que el número de datos actuales en la tabla._

```
REPORTAR 20
```

### Comando CERRAR

_El comando CERRAR se encarga de salir del programa y cerrar la ventana de la consola._
_Nota: Este comando hace que la consola se cierre de inmediato, por lo que no se podrán recuperar registros una vez utilizado._

```
CERRAR
```

## Recomendaciones para el usuario

_Para una mejor experiencia con el uso de la aplicación por favor siga las siguientes indicaciones:_

### Aprovechando case-insensitive

_El programador recomienda utilizar la ventaja que ofrece la insensibilidad a las mayúsculas a su favor, por lo que si se está escribiendo en minúsculas, ejecute los comandos también en minúsculas:_

```
seleccionar nombre, edad, activo donde edad=25
```

### Corroborar el número de datos antes de reportar

_Para evitar que el programa detecte un error y se cierre automáticamente, es preferible que antes de reportar cierto número de datos, se verifique con el comando CUENTA cuántos datos posee la tabla actualmente y no cometer un error (y por ende eliminar todos los registros)._

```
CUENTA
Número de datos = 5

REPORTAR 4
```

## Información adicional

_Algunos datos que podrían servir al usuario_

* Versión de Python utilizada: Python 3.8.5
* Fecha de creación: 30/08/2020
* Desarrollador: Meoer8Marsan
* Sistema de versionamiento utilizado: GitHub

---
Todos los derechos reservados por Romeo Ernesto Marroquín Sánchez (Meoer8Marsan)