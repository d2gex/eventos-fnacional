import "bootstrap/dist/css/bootstrap.css"
import "bootstrap/dist/js/bootstrap"
import "./assets/main.css"
import {createApp} from 'vue'
import App from './App.vue'
import router from './router'

let app = createApp(App)
app.use(router)
app.mount('#app')

