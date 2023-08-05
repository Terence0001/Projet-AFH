import { createRouter, createWebHistory } from 'vue-router'
import FormViewVue from '../views/FormView.vue'
import HistoView from '../views/HistoView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: FormViewVue
    },
    {
      path: '/about',
      name: 'about',
      component: HistoView
    }
  ]
})

export default router
