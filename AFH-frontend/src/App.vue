<script setup>
import FormView from './views/FormView.vue';
import HistoView from './views/HistoView.vue';
</script>

<template>
  <v-container>
    <v-row class="align-center">
      <v-col cols="12" md="6" class="text-center">
        <!-- Contenu du formulaire -->
        <FormView />
      </v-col>
      <v-col cols="12" md="6" class="text-center">
        <!-- Contenu de l'historique -->
        <HistoView />
      </v-col>
    </v-row>
  </v-container>
</template>


