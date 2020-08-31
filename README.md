# SimpleQL

(Manual de Usuario)

## Descripci�n

_SimpleQL es una aplicaci�n desarrollada en python con el fin de facilitar la gesti�n de archivos que est�n en formato .json, la aplicaci�n tiene la capacidad de cargar uno o varios archivos .json para realizar una tabla de los registros ingresados para poderlos gestionar de mejor manera._
_El manejo de la aplicaci�n es como el de una consola cualquiera, en este caso estamos hablando de un "lenguaje" tipo declarativo, el cual consiste en ingresar el comando y presionar la tecla ENTER para ejecutarlo._

### Funcionamiento

_SimpleQL posee 8 comandos diferentes los cuales ayudan al usuario a interactuar con la interfaz de programaci�n, adem�s de que los c�digos ingresados son insensibles a las may�sculas, estos c�digos se especifican a continuaci�n:_

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

_El comando CARGAR se encarga de cargar los datos de uno o m�s archivos .json a la memoria del dispositivo, los archivos deben ir separados por coma y espacio uno del otro._

_Nota: No existe un l�mite para subir archivos, por lo que la �nica limitante es el hardware del usuario._

```
CARGAR seccionA.json, seccionB.json, seccionC.json
```

### Comando SELECCIONAR

_El comando SELECCIONAR se encarga de mostrar los datos que se han cargado a memoria, adem�s que se pueden seleccionar todos (*) o solo algunos campos indicando el nombre de la columna que se desea mostrar, adicionalmente, con la extensi�n DONDE es posible a�adir una restricci�n que se limita �nicamente a igualaci�n de un campo con un valor espec�fico._

_Nota: Si alguno de los campos es mal ingresado la aplicaci�n se cerrar� inmediatamente._

```
SELECCIONAR * DONDE Activo=True
```

### Comando MAXIMO

_El comando MAXIMO se encarga de buscar el valor m�ximo de un campo dentro de toda la tabla con los datos ingresados anteriormente._

_Nota: Solo es posible ingresar dos campos en este comando, en este caso solo se admiten los campos Edad y Promedio (valores num�ricos)._

```
MAXIMO promedio
```

### Comando MINIMO

_El comando MINIMO se encarga de buscar el valor m�nimo de un campo dentro de toda la tabla con los datos ingresados anteriormente._

_Nota: Solo es posible ingresar dos campos en este comando, en este caso solo se admiten los campos Edad y Promedio (valores num�ricos)._

```
MINIMO edad
```

### Comando SUMA

_El comando SUMA se encarga de calcular el valor num�rico total de un campo dentro de la tabla con los datos ingresados anteriormente._

_Nota: Solo es posible ingresar dos campos en este comando, en este caso solo se admiten los campos Edad y Promedio (valores num�ricos)._

```
SUMA promedio
```

### Comando CUENTA

_El comando CUENTA se encarga de calcular el n�mero de registros actuales que hay dentro de la tabla con los datos ingresados anteriormente._

_Nota: Este comando no admite ning�n par�metro para su uso._

```
CUENTA
```

### Comando REPORTAR n

_El comando REPORTAR se encarga de realizar un reporte HTML estilizado con CSS utilizando el n�mero de registros ingresados, los cuales son los n primeros registros que hay dentro de la tabla con los datos ingresados anteriormente._

_Nota: Este comando no admite 0 registros, ni tampoco m�s registros que el n�mero de datos actuales en la tabla._

```
REPORTAR 20
```

### Comando CERRAR

_El comando CERRAR se encarga de salir del programa y cerrar la ventana de la consola._
_Nota: Este comando hace que la consola se cierre de inmediato, por lo que no se podr�n recuperar registros una vez utilizado._

```
CERRAR
```

## Recomendaciones para el usuario

_Para una mejor experiencia con el uso de la aplicaci�n por favor siga las siguientes indicaciones:_

### Aprovechando case-insensitive

_El programador recomienda utilizar la ventaja que ofrece la insensibilidad a las may�sculas a su favor, por lo que si se est� escribiendo en min�sculas, ejecute los comandos tambi�n en min�sculas:_

```
seleccionar nombre, edad, activo donde edad=25
```

### Corroborar el n�mero de datos antes de reportar

_Para evitar que el programa detecte un error y se cierre autom�ticamente, es preferible que antes de reportar cierto n�mero de datos, se verifique con el comando CUENTA cu�ntos datos posee la tabla actualmente y no cometer un error (y por ende eliminar todos los registros)._

```
CUENTA
N�mero de datos = 5

REPORTAR 4
```

## Informaci�n adicional

_Algunos datos que podr�an servir al usuario_

* Versi�n de Python utilizada: Python 3.8.5
* Fecha de creaci�n: 30/08/2020
* Desarrollador: Meoer8Marsan
* Sistema de versionamiento utilizado: GitHub

---
Todos los derechos reservados por Romeo Ernesto Marroqu�n S�nchez (Meoer8Marsan)