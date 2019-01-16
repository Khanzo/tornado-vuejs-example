import Vue from 'vue'
import Router from 'vue-router'
import App from './App.vue'
import Home from './components/Home.vue'
import About from './components/About.vue'
import Random from './components/Random.vue'
import Error from './components/NotFound.vue'
import Sotrud from './components/Sotrud.vue'
import AddSotrud from './components/AddSotrud.vue'
import Zarplat from './components/Zarplat.vue'
import titleMixin from './mixins/titleMixin'

Vue.use(Router)
Vue.mixin(titleMixin)

const router = new Router({
 mode: 'history',
 routes: [
   {
     path: '/',
     name:'home',
     meta:{title:'Сотрудники'},
     component: Home,
   },
   {
     path: '/about',
     name:'about',
     meta:{title:'О проекте'},
     component: About,
   },
   {
     path: '/add',
     name:'add',
     meta:{title:'Новый сотрудник'},
     component: AddSotrud,
   },
   {
     path: '/sotrud/:id',
     name:'sotrud',
     meta:{title:'Сотрудник'},
     component: Sotrud,
     props: true,
   },
   {
     path: '/zarplati/:id',
     name:'zarplat',
     meta:{title:'Зарплаты'},
     component: Zarplat,
     props: true,
   },
   {
     path: '/random',
     name:'random',
     component: Random,
   },
   {
     path: '*',
     name:'NotFound',
     component: Error,
   },
 ]
})

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
