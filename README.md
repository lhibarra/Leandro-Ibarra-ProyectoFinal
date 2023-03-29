
# Proyecto Final Leandro Ibarra
Requisitos para su funcionamiento:
- Tener instalado python 3.9 o superior

## Objetivo del sistema
- Permitir a los usuarios crearse una cuenta. Posteriormente logearse, y allí publicar su máquina para alquilar. El usuario también puede alquilar una en caso de que lo requiera. El sistema permite comunicarse entre los diversos usuarios registrados.

## Paquetes necesarios para la instalación
-Desde la terminal  que se se esté utilizando ejecutar el siguiente comando: pip install django

## Prueba del sistema

1- Ejecutar el comando python manage.py runserver desde la consola utilizada
2- Ingresar al navegador con la siguiente dirección: http://127.0.0.1:8000/
3- En la página de inicio encontraremos un menú con las siguientes opciones: Inicio, Ver, Registrate, Ingresar y Acerca de mi y un formulario que me permite buscar la herramienta deseada.En cada uno de ellos podemos acceder sin necesidad de estar logeados. 
4- En el menú Logearse nos va pedir nombre de usuario y contraseña e ingresa al sistema. En caso de no tener usuario creado, en la opción registrate se puede crear un usuario que luego te redirige a login.
5- Cuando el usuario se logea, entra a la página de inicio, la misma tiene otros menues: Mis máq., Ingresa tu Maq., Enviar Mensaje, Mje, editar o crear perfil, dependiendo si el usuario ya tiene creado un perfil o no, Salir
El menú Ingresa tu Maq. permite al usuario realizar una publicación de su maquina para alquilar. En Ver podemos ver todas las publicaciones de todos los usuarios. Y en el menú Mis Maq. el usuario podrá ver todas sus máquinas publicadas. Enviar Mensaje permite comunicarse con otro usuario por este medio. En Ver Mje, aquí el usuario recibirá la información sufiente para poder alquilar su máquina
6- Finalmente, en el menú salir el usuario sale del sistema 





## Video demostrativo
https://youtu.be/XQs6YaopQiQ

