import Vue from 'vue'
import VueRouter from 'vue-router'
import store from "@/store";

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('../views/Register.vue')
  },
    {
    path: '/home',
    name: 'Home2',
    component: () => import('../views/Home2.vue')
  },
  {
    path: '/404',
    name: '404',
    component: () => import('../views/404.vue')
  },
  {
    path: '/changepassword',
    name: 'ChangePassword',
    component: () => import('../views/ChangePassword.vue')
  },
  {
    path: '/property',
    name: 'Property',
    component: () => import('../views/Property.vue')
  },
  {
    path: '/today',
    name: 'Today',
    component: () => import('../views/Today.vue')
  },
  {
    path: '/stock1',
    name: 'Stock1',
    component: () => import('../views/Stock1.vue')
  },
  {
    path: '/stock2',
    name: 'Stock2',
    component: () => import('../views/Stock2.vue')
  },
  {
    path: '/trade1',
    name: 'Trade1',
    component: () => import('../views/Trade1.vue')
  },
  {
    path: '/trade2',
    name: 'Trade2',
    component: () => import('../views/Trade2.vue')
  },
  
  {
    path: '/trade11',
    name: 'Trade11',
    component: () => import('../views/Trade11.vue')
  },
  {
    path: '/trade22',
    name: 'Trade22',
    component: () => import('../views/Trade22.vue')
  },
  {
    path: '/strategy1',
    name: 'Strategy1',
    component: () => import('../views/Strategy1.vue')
  },
  {
    path: '/strategy2',
    name: 'Strategy2',
    component: () => import('../views/Strategy2.vue')
  },
  {
    path: '/strategy_show1',
    name: 'Strategy_show1',
    component: () => import('../views/Strategy_show1.vue')
  },
  {
    path: '/kline1',
    name: 'Kline1',
    component: () => import('../views/Kline1.vue')
  },
  {
    path: '/kline2',
    name: 'Kline2',
    component: () => import('../views/Kline2.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

// 重置路由
export const resetRouter = () => {
  router.matcher = new VueRouter({
    mode: 'history',
    routes
  })
}

router.beforeEach((to, from, next) => {
  localStorage.setItem("currentPathName", to.name)  // 设置当前的路由名称
  store.commit("setPath")
  if (!to.matched.length) {
    const menus = localStorage.getItem("menus")
    if (!menus) {
      next("/login")
    } else {
      next("/404")
    }
  } else {
    next()
  }
})

export default router
