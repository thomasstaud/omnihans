<script setup>
import ToDoWidget from "./components/ToDoWidget.vue";
import WeatherWidget from "./components/WeatherWidget.vue";
</script>

<template>
  <div class="text text-base-content">
    <p class="title my-10">omnihans</p>

    <div class="flex flex-row mx-10">
      <div class="flex flex-col">
        <WeatherWidget />
      <ToDoWidget today title="Heute steht folgendes an:"/>
      </div>
      <ToDoWidget title="Das wär auch noch zu tun:"/>
    </div>
  </div>
</template>
