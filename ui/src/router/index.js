import Vue from 'vue'
import VueRouter from 'vue-router'
import BoardList from '../views/BoardList.vue'
import Board from '../views/Board.vue'
import About from '../views/About.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'BoardList',
    component: BoardList
  },
  {
    path: '/about',
    name: 'About',
    component: About 
  }, 
  {
    path: '/board/:id',
    name: 'Board',
    component: Board
  }
]

const router = new VueRouter({
  routes
})

export default router
