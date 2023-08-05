import './assets/main.css'

import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
    components,
    directives,
  })

// Créez une instance d'application Vue
const app = createApp(App)
// Utilisez les plugins
app.use(router);
app.use(vuetify);
// Montez l'application
app.mount('#app');