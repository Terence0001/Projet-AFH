<script setup>
import { RouterLink, RouterView } from 'vue-router'
import FormView from './views/FormView.vue';
import HistoView from './views/HistoView.vue';
</script>

<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="6">
        <!-- Contenu du formulaire -->
        <FormView />
      </v-col>
      <v-col cols="12" md="6">
        <!-- Contenu de l'historique -->
        <HistoView />
      </v-col>
    </v-row>
  </v-container>
</template>


