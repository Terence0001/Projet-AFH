<template>
  <div class="historique">
    <h1>Voici votre historique</h1>
    <v-table height="300px" :hover="true">
      <thead>
        <tr>
          <th class="text-left">
            Date
          </th>
          <th class="text-left">
            Résultat
          </th>
          <th class="text-left">
            Pécision
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in data_pred.reverse()" :key="item.date">
          <td>{{ item.date }}</td>
          <td>{{ item.results }}</td>
          <td>{{ item.precision }}</td>
        </tr>
      </tbody>
    </v-table>
  </div>
</template>
<script>
import axios from 'axios';
export default {
  data() {
    return {
      data_pred: []  // Initialise un tableau vide pour les données de prédiction
    };
  },
  methods: {
    // Fonction pour récupérer les prédictions depuis l'API
    async fetchPredictions() {
      try {
        // Effectue une requête GET pour obtenir les données de prédiction
        const response = await axios.get('http://127.0.0.1:8000/api/predictions/');
        this.data_pred = response.data; // Met à jour data_pred avec les données récupérées
      } catch (error) {
        console.error('Erreur lors de la récupération des données :', error);
      }
    },
  },
  mounted() {
    // Appelle fetchPredictions lors du montage du composant pour afficher les prédictions initiales
    this.fetchPredictions();
    // Écoute l'événement personnalisé pour mettre à jour les prédictions
    window.addEventListener('predictions-updated', (event) => {
      this.data_pred = event.detail; // Met à jour data_pred avec les nouvelles données
    });
  },
  beforeUnmount() {
    // Supprime l'écouteur d'événement lorsque le composant est démonté
    window.removeEventListener('predictions-updated', (event) => {
      this.data_pred = event.detail; // Met à jour data_pred avec les nouvelles données
    });
  }
};

</script>

