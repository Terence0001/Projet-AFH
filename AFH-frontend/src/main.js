// import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import stores from './stores/stores' // Importer le store Vuex

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives
})

// Créez une instance d'application Vue
const app = createApp(App)
// Utilisez les plugins
app.use(stores)
app.use(router)
app.use(vuetify)
// Montez l'application
app.mount('#app')
