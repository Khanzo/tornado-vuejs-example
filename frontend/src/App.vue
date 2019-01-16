
<template>
  <div id="app">
    <div class="header">
        <div class="menu-links">
          <img src="./assets/logo.png" class="logo">
          <router-link to="/">Сотрудники</router-link>
          <router-link to="/about">О проекте</router-link>
          <router-link to="/random">Случайное число</router-link>
        </div>
    </div>
  <div class="page">
    <router-view/>
  </div>
  </div>
</template>

<script>
import Vue from 'vue';
import BootstrapVue from 'bootstrap-vue';
Vue.use(BootstrapVue);
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


export default {
  name: 'app',
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  display: flex;
  flex-direction: column;
  width: 100%;
}
.logo {
  width: 30px;
  height: 30px;
}

.menu-links a {
  display: inline-block;
  text-decoration: none;
  color: #555;
  margin-right: 30px;
}

.header {
  border-bottom: 1px solid #b3b3b3;
  padding: 30px;
}
.page {
  width: 100%;
}

</style>
