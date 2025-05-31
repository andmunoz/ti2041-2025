# Aplicación Blog con Usuarios
Este ejemplo cumple con las características de seguridad solicitadas para la segunda evaluación. Se compone de los siguientes elementos: 

- blog: Es el proyecto Django.
- catblog: Es la app asociada al proyecto.

Para acceder a la app, se utiliza la url raíz directamente del proyecto, es decir: http://127.0.0.1:8000. Para entrar al administrador de Django, deben hacerlo a través de http://127.0.0.1:8000/admin.

## Consideraciones Generales
Esta aplicación utiliza tres contenidos vistos en clase: 

### Autenticación de Usuarios
A través de la autenticación de usuario, cada uno de los creadores de contenidos podrán ver sus propios artículos publicados y gestionarlos. Esto permite mantener separada la gestión dependiendo de cada usuario.

### Autorización de Usuarios
Utilizando los privilegios entregados en el administrador de Django, cada usuario va a poder realizar diferentes acciones sobre el modelo asignado (Post). Estos privilegios se estructuran como: 

- Ver Post (view_post)
- Crear Post (add_post)
- Modificar Post (change_post)
- Eliminar Post (delete_post)

Si bien es cierto, el visualizar tiene un permiso, no lo consideramos ya que por lógica cualquier usuario puede ver un post.

### Plantillas Heredables
Como se utilizó un framework de HTML (Materialize.CSS), crear templates para cada acción iba a repetir muchos elementos que, si queríamos gestionarlos, sería demasiado engorroso. Así que se creó una estructura general *base.html* que divide la página en secciones: 

- Un encabezado (head) que es único para todas los contenidos.
- Un contenido (main) que va variando dependiendo de lo que está realizando el usuario.
- Un pie de página (footer) que es estático.

## Usuarios de Pruebas
Para realizar las pruebas de uso, se crearon diferentes usuarios con permisos variados, de manera de que se pudiesen probar todas las combinaciones posibles. Los usuarios disponibles para las pruebas son:

- admin/admin: Usuario administrador. Solo utilizado para entrar a Django-Admin
- jperez/inacap2025: Usuario de pruebas publicador de post. Puede ver, publicar, modificar y eliminar.
- pgonzalez/inacap2025: Usuario de pruebas publicador de post. Puede ver, publicar y modificar.
- mdiaz/inacap2025: Usuario de pruebas publicador de post. Solo puede ver y publicar.