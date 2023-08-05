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
            Pécision
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in data_pred" :key="item.date">
          <td>{{ item.date }}</td>
          <td>{{ item.précision }}</td>
        </tr>
      </tbody>
    </v-table>
  </div>
</template>
<script>
export default {
  data() {
    return {
      data_pred: [
      ],
    }
  },
  methods() {
    axios.get(`http://127.0.0.1:8000/api/predictions/`)
    console.log("test")
  }
}
</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
