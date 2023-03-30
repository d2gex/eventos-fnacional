import "bootstrap/dist/css/bootstrap.css"
import "bootstrap/dist/js/bootstrap"
import Vuelidate from 'vuelidate'
import {createApp} from 'vue'
import App from './App.vue'
import router from './router'

let app = createApp(App)
app.use(router)
app.use(Vuelidate)
app.mount('#app')

