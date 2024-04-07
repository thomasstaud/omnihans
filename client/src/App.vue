<script setup>
import ToDoWidget from "./components/ToDoWidget.vue";
</script>

<template>
  <div class="text">
    <p class="title my-10">omnihans</p>

    <div class="mx-10 mb-5" v-if="weather != null">
      <p>{{ weather.description }}</p>
      <p>{{ weather.temperature }}°C</p>
    </div>

    <to-do-widget />
  </div>
</template>

<script>
import * as api from "./api.js";

export default {
    data() {
        return {
            // weather
            weather: null,
        }
    },
    async mounted() {
      this.weather = await api.get_weather();
    }
}
</script>
