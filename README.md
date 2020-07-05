# Tic-Tac-Toe
Tic-Tac-Toe based on AI. Some algorithms that I pretend to implement are Minimax, Alpha-Beta prudding and  MCTS

# Intelligent_Tic-Tac-Toe
[Adrián Carretero Canut](https://github.com/acarreteroc99) \


## Content
- [Project Description](#project-description)
- [Dataset](#dataset)
- [Conclusion](#conclusion)
- [Future Work](#future-work)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
Dada la situación actual del coronavirus y las recomendaciones de seguridad dadas por el Gobierno, queríamos crear una App para ayudar a controlar los aforos, pudiendo reservar en tus lugares de ocio favoritos y saber la congestión del mismo antes de acudir.
Actualmente la App está pensada para locales más en el ámbito privado y centrada en piscinas, pero nuestra intención es ampliarla a cualquier espacio público. Es por ello que ya en fase de desarrollo hayamos añadido ciertas funcionalidades o requisitos que la harán que sea fácilmente escalable.
Además damos la posibilidad de crear incompatibilidades de edad, por ejemplo, actualmente es recomendable que mayores de 70 años y menores de 14 no compartan lugares como la piscina, es por ello que cuando se intenta realizar la reserva, antes se comprueba si existe alguien de la franja contraria para avisarte de ello y cambiar la reserva.

## Dataset
- Actualmente todos los datos están siendo hospedados en una base de datos de un hosting gratuito y utilizamos phpmyadmin como interfaz web para acceder a ella.
- Tenemos concretamente tres tablas: "Users" en la que tenemos la información de los usuarios; "Pool" en la que tenemos la información de la piscina; y, por último, "Booking" en la que tenemos información de las reservas.

## Conclusion
 - Tenemos un primer modelo con todas las características funcionales el cual creemos que ya es capaz de tener mucho éxito y ayudar a mucha gente.

## Future Work
- Añadir geolocalización para confirmar/cancelar automáticamente reservas.
- Añadir notificaciones via mail.
- Añadir recordatorios/pop-ups en el dispositivo móvil.
- Ampliar locales posibles y capacidad de usuarios.
- Comprar un hosting privado.
- Escalar a todo tipo de Sistemas Operativos.

## Workflow
- La app primero enseña una interfaz en la que un usuario registrado podrá hacer el log in para acceder a la App y un usuario nuevo podrá acceder al registro para crearse su usuario único.
- A partir de ahí la App nos enseña un menú con tres opciones.
- En la primera opción el usuario tiene la capacidad de sabiendo el código de su piscina, pueda consultar el aforo máximo así como otras normas.
- En la segunda opción el usuario accede a realizar la reserva en el día y horario que él elija, siempre cumpliendo las condiciones de aforo, opertura y franjas de edades.
- En la última opción el usuario puede cancelar su reserva por si quiere modificar el horario de la misma o por si no puede ir.

## Organization
En el repositorio puedes encontrar:
- La carpeta py dónde está todo el código de todas las pantallas y la Lógica que engloba todo.
- La carpeta ui dónde se encuentran los archivos de diseño que pueden editarse con la herramienta Qt Designer.
- La carpeta Others en la que se guardan todas las imagenes usadas y el fichero de recursos.
- Las carpetas dist y build + el archivo Logica.spec que son generados por pyinstaller que engloban el proyecto una vez compilado
- El archivo PisciGO.zip que es un comprimido del punto anterior. Cabe remarcar que dentro de la carpeta dist se encuentra el ejecutable.
