<script>
import * as api from "./api.js";

export default {
    data() {
        return {
            weather: null,
        }
    },
    async mounted() {
        this.weather = await api.get_weather();
    }
}
</script>

<template>
  <p class="title py-10">omnihans</p>
  <div class="text px-10" v-if="weather != null">
    <p>{{ weather.description }}</p>
    <p>{{ weather.temperature }}°C</p>
  </div>
</template>
