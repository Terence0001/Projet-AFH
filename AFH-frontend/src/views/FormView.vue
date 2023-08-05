<script setup>
</script>

<template>
  <main>
    <div>
      <v-hover>
        <template v-slot:default="{ isHovering, props }">
          <v-card v-bind="props" :color="isHovering ? 'primary' : undefined" title="Formulaire de prédiction"
            text="..."></v-card>
        </template>
      </v-hover>
    </div>
    <v-file-input chips multiple label="Vos images"></v-file-input>
  </main>
</template>
