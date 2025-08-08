<template>
<div class="card bg-base-200 w-96 shadow-lg m-5" v-if="weather != null">
<div class="card-body">
    <p>{{ weather.description }}</p>
    <div class="collapse bg-base-100 border-base-300 border">
        <input type="checkbox" @click="find_running_time()" />
        <div class="collapse-title font-semibold">
            {{ weather.temperature }}°C
        </div>
        <div class="collapse-content text-sm">
            Laufen geht ab {{ running_time }} ({{ running_temp }}°C)
        </div>
    </div>
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
            running_time: null,
            running_temp: null,
        }
    },
    async mounted() {
      this.weather = await api.get_weather();
    },
    methods: {
        // returns the time and temperature at which running seems doable
        async find_running_time() {
            console.log("hans");

            if (this.running_time != null) {
                return;
            }

            const max_temp = 30;
            const weather = await api.get_weather_detailed();
            console.log(weather);

            for (const x of weather) {
                console.log(x);
                if (x.temperature <= max_temp) {
                    const date = new Date(x.timestamp * 1000);
                    const hours = date.getHours();
                    const minutes = "0" + date.getMinutes();
                    this.running_time = hours + ':' + minutes.slice(-2);
                    this.running_temp = x.temperature;
                    break;
                }
            }
        }
    }
}
</script>
