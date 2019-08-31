import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Login from '@/components/Login'
import Register from '@/components/Register'
import RegisterFav from '@/components/RegisterFav'
import DefaultLayout from '../layouts/Default'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/tab',
      component: DefaultLayout,
      children: [
        {
          path: 'index',
          name: 'index',
          component: Index
        }
      ]
    },
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/register_fav',
      name: 'RegisterFav',
      component: RegisterFav
    }
  ]
})
