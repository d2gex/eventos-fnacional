import "bootstrap/dist/css/bootstrap.css"
import "./assets/main.css"
import 'sweetalert2/dist/sweetalert2.min.css';
import '@vuepic/vue-datepicker/dist/main.css'
import "primevue/resources/themes/lara-light-blue/theme.css";
import "primevue/resources/primevue.min.css";
import "primeicons/primeicons.css";

import "bootstrap/dist/js/bootstrap"
import "./assets/common.js"

import VueSimpleAlert from "vue3-simple-alert";
import PrimeVue from 'primevue/config'
import ToastService from 'primevue/toastservice';
import {createApp} from 'vue'
import App from './App.vue'
import router from './router'

let app = createApp(App)
app.use(router)
app.use(VueSimpleAlert)
app.use(PrimeVue)
app.use(ToastService)
app.mount('#app')
app.config.globalProperties.$vueAlert = VueSimpleAlert;

