import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Login from '@/components/Login'
import Register from '@/components/Register'
import RegisterSex from '@/components/RegisterSex'
import RegisterFav from '@/components/RegisterFav'
import CreateBodyInfo from '@/components/CreateBodyInfo'
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
    },
    {
      path: '/register_sex',
      name: 'RegisterSex',
      component: RegisterSex
    },
    {
      path: '/create/bodyinfo',
      name: 'CreateBodyInfo',
      component: CreateBodyInfo
    }
  ]
})
