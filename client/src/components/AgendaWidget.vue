<script setup>
import ToDoModal from "./ToDoModal.vue";
</script>

<template>
<div class="card bg-base-200 w-96 shadow-lg m-5">
<div class="card-body">
    <p>Heute steht folgendes an:</p>
    <ul class="list bg-base-100 rounded-box shadow-md mx-3">
        <li v-for="t in todos" class="list-row">
            <div>{{ t }}</div>
            <input type="checkbox" checked="checked" class="checkbox" />
        </li>
    </ul>
    <br>
    <button class="btn btn-sm bg-base-300 text-lg my-2 mx-8 rounded-full" onclick="agendaModal.showModal()">+</button>

    <ToDoModal id="agendaModal"/>
</div>
</div>
</template>

<script>
import * as api from "@/api.js";

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