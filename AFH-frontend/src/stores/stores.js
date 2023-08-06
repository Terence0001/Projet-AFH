// src/store.js
import { createStore } from 'vuex'

const store = createStore({
  state: {
    predictions: [] // Initial state for predictions
  },
  mutations: {
    setPredictions(state, predictions) {
      state.predictions = predictions
    }
  },
  actions: {
    updatePredictions({ commit }, predictions) {
      commit('setPredictions', predictions)
    }
  },
  getters: {
    getPredictions(state) {
      return state.predictions
    }
  }
})

export default store
