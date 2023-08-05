<template>
  <main>
    <div>
      <v-hover>
        <template v-slot:default="{ isHovering, props }">
          <v-card v-bind="props" :color="isHovering ? 'primary' : undefined" title="Formulaire de prédiction"
            text="Importer vos images et lancez la prédiction"></v-card>
        </template>
      </v-hover>
    </div>
    <form @submit.prevent="submitForm">
      <v-file-input ref="fileInput" chips multiple label="Vos images ici"></v-file-input>
      <v-btn type="submit" color="primary">Envoyer</v-btn>
    </form>
  </main>
</template>

<script>
import axios from 'axios';
export default {
  methods: {
    async submitForm() {
      const formData = new FormData();
      const files = this.$refs.fileInput.files;
      for (let i = 0; i < files.length; i++) {
        formData.append('images', files[i]);
      }
      try {
        const response = await axios.post(`http://127.0.0.1:8000/api/predict/`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        console.log('Formulaire soumis', response.data);
      } catch (error) {
        console.error('Erreur lors de l\'envoi du formulaire :', error);
      }
    }
  }
}
</script>