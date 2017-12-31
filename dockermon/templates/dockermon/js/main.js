import Vue from 'vue'
import App from './App'
import axios from 'axios'

Vue.prototype.$http = axios


/*아이유 노래 짱잘해*/
new Vue({
    el:'#app',
    template : '<App/>',
    components: { App }
})