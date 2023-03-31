import "bootstrap/dist/css/bootstrap.css"
import "bootstrap/dist/js/bootstrap"
import { configure } from 'vee-validate'
import {createApp} from 'vue'
import App from './App.vue'
import router from './router'

configure({
  classes: {
    valid: 'is-valid',
    invalid: ['is-invalid', 'invalid-feedback']
  }
})
let app = createApp(App)
app.use(router)
app.mount('#app')

