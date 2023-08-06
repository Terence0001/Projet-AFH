<template>
  <main>
    <div>
      <v-hover>
        <template v-slot:default="{ isHovering, props }">
          <v-card v-bind="props" :color="isHovering ? 'primary' : undefined" title="Formulaire de prédiction"
            text="Importer vos images et lancez la prédiction et pour voir le résultat recharger la page"></v-card>
        </template>
      </v-hover>
    </div>
    <form @submit.prevent="submitForm">
      <v-file-input ref="fileInput" chips multiple label="Vos images ici" id="fileInput"></v-file-input>
      <v-btn type="submit" color="primary">Envoyer</v-btn>
    </form>
  </main>
</template>


<script>
import axios from 'axios';
import { ref } from 'vue';

export default {
  setup() {
    // Crée une référence réactive pour stocker les prédictions
    const predictions = ref([]);
    // Fonction pour soumettre le formulaire
    const submitForm = async () => {
      // Crée un objet FormData pour les données du formulaire
      const formData = new FormData();
      // Récupère les fichiers sélectionnés dans le champ de fichier
      const files = document.querySelector('#fileInput').files;
      // Ajoute chaque fichier au FormData avec la clé 'images'
      for (let i = 0; i < files.length; i++) {
        formData.append('images', files[i]);
      }
      try {
        // Envoie une requête POST avec les données du formulaire
        const response = await axios.post(`http://127.0.0.1:8000/api/predict/`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        predictions.value = response.data;
        console.log('Formulaire soumis', response.data);
      } catch (error) {
        console.error('Erreur lors de l\'envoi du formulaire :', error);
      }
    };
    // Retourne les fonctions et données nécessaires pour le composant
    return {
      submitForm, // Fonction pour soumettre le formulaire
      predictions// Référence réactive pour stocker les prédictions
    };
  }
};

</script>
