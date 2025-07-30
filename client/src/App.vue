<script setup>
import AgendaWidget from "./components/AgendaWidget.vue";
import ToDoWidget from "./components/ToDoWidget.vue";
import WeatherWidget from "./components/WeatherWidget.vue";
</script>

<template>
  <div class="text text-base-content">
    <p class="title my-10">omnihans</p>

    <div class="flex flex-row mx-10">
      <div class="flex flex-col">
        <WeatherWidget />
        <AgendaWidget />
      </div>
      <ToDoWidget />
    </div>
  </div>
</template>
