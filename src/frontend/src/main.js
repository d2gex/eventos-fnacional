import "bootstrap/dist/css/bootstrap.css"
import "./assets/main.css"
import 'sweetalert2/dist/sweetalert2.min.css';
import "bootstrap/dist/js/bootstrap"
import "./assets/common.js"
import VueSimpleAlert from "vue3-simple-alert";
import {createApp} from 'vue'
import App from './App.vue'
import router from './router'

let app = createApp(App)
app.use(router)
app.use(VueSimpleAlert)
app.mount('#app')
app.config.globalProperties.$vueAlert = VueSimpleAlert;

