import Vue from 'vue'
import App from './App'
import axios from 'axios'

Vue.prototype.$http = axios

import Demon from "./components/Demo.vue"

/*아이유 노래 짱잘해*/


const app = new Vue({
    el:'#app',
    template : '<App/>',
    components: { App }
})