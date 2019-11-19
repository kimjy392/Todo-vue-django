import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueSession from 'vue-session'

Vue.config.productionTip = false
// vue-session 서맃
// VueSession 추가
Vue.use(VueSession)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
