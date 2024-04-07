<script setup>
import ToDoModal from "./ToDoModal.vue";
</script>

<template>
<div class="mx-10 mb-5">
    <p>Heute steht folgendes an:</p>
    <div class="join join-vertical mx-3">
        <p v-for="t in todos" class="join-item">• {{ t }}</p>
    </div>
    <br>
    <button class="btn btn-sm text-lg my-2 mx-8 rounded-full" onclick="todoModal.showModal()">+</button>

    <to-do-modal />
</div>
</template>

<script>
import * as api from "../api.js";

export default {
    data() {
        return {
            todos: null
        }
    },
    async mounted() {
      this.todos = await api.get_todos_today();
    }
}
</script>