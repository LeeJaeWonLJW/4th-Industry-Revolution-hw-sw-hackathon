import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Login from '@/components/Login'
import RegisterSex from '@/components/RegisterSex'
import RegisterFav from '@/components/RegisterFav'
import CreateBodyInfo from '@/components/CreateBodyInfo'
import Diary from '@/components/Diary'
import DietList from '@/components/DietList'
import DietListInfo from '@/components/DietListInfo'
import AddUser from '@/components/AddUser'
import AddMeal from '@/components/AddMeal'
import DiaryDetail from '@/components/DiaryDetail'
import MealDetail from '@/components/MealDetail'
import BarcodeView from '@/components/BarcodeView'
import BarcodeInputView from '@/components/BarcodeInputView'
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
        },
        {
          path: 'diary',
          name: 'diary',
          component: Diary
        },
        {
          path: 'diarydetail',
          name: 'diarydetail',
          component: DiaryDetail
        },
        {
          path: 'dietlist',
          name: 'dietlist',
          component: DietList
        },
        {
          path: 'dietlist/1',
          name: 'dietlistinfo',
          component: DietListInfo
        },
        {
          path: 'adduser',
          name: 'adduser',
          component: AddUser
        },
        {
          path: 'addmeal/:type',
          name: 'addmeal',
          component: AddMeal
        },
        {
          path: 'mealdetail/:id',
          name: 'mealdetail',
          component: MealDetail
        },
        {
          path: 'barcode',
          name: 'barcode-view',
          component: BarcodeView
				},
				{
          path: 'barcode/input',
          name: 'barcode-input-view',
          component: BarcodeInputView
        }
      ]
    },
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/register/favorite',
      name: 'RegisterFav',
      component: RegisterFav
    },
    {
      path: '/register/sex',
      name: 'RegisterSex',
      component: RegisterSex
    },
    {
      path: '/register/info',
      name: 'CreateBodyInfo',
      component: CreateBodyInfo
    }
  ]
})
