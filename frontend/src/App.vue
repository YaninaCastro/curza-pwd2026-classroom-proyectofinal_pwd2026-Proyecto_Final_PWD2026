<!--contenedor principal de la aplicación.-->

<template>
  <div id="app">
    <RouterView/>
  </div>
</template>

 <!--<RouterView /> Es el componente de Vue Router que funciona como espacio dinámico 
donde se renderiza la vista correspondiente a la URL.
Por ejemplo:
- Al ingresar a /login, muestra el componente de login.
- Al ingresar a /home, muestra HomeView.vue.
- Al ingresar a /duenos, muestra la vista correspondiente a dueños.
No se necesita importar manualmente cada vista en App.vue, porque Vue Router
se encarga de mostrarla según la configuración de las rutas..-->
