import Vue from 'vue'
import Router from 'vue-router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import HelloWorld from '@/components/HelloWorlds'
import Hello from '@/components/ApiData'
import News from '@/components/NewsData'
import Topmv from '@/components/Topmv'

Vue.use(Router)
Vue.use(ElementUI)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/xxb',
      name: 'Hello',
      component: Hello
    },
    {
      path: '/news',
      name: 'News',
      component: News
    },
    {
      path: '/topmv',
      name: 'Topmv',
      component: Topmv
    }
  ]
})
