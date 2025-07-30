<template>
<div class="card bg-base-200 w-96 shadow-lg m-5" v-if="weather != null">
<div class="card-body">
    <p>{{ weather.description }}</p>
    <p>{{ weather.temperature }}°C</p>
</div>
</div>
</template>

<script>
import * as api from "@/api.js";

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
