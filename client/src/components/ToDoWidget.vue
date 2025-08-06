<script setup>
import ToDoModal from "./ToDoModal.vue";
</script>

<template>
<div class="card bg-base-200 w-96 shadow-lg m-5">
<div class="card-body">
    <p>{{ title }}</p>
    <ul class="list bg-base-100 rounded-box shadow-md mx-3">
        <li v-for="t in todos" class="list-row">
            <div>{{  }}</div>
            <div class="list-col-grow">{{ t.text }}</div>
            <p>{{ t.date }}</p>
            <input v-model="t.checked" type="checkbox" class="checkbox" @click="checked(t)" />
        </li>
    </ul>
    <button class="btn btn-sm bg-base-300 text-lg my-2 mx-8 rounded-full" @click="open_modal()">+</button>

    <ToDoModal v-if="today" id="agendaModal"/>
    <ToDoModal v-if="!today" id="todoModal" date-field />
</div>
</div>
</template>

<script>
import * as api from "@/api.js";

export default {
    props: {
        today: Boolean,
        title: String
    },
    data() {
        return {
            todos: null
        }
    },
    async mounted() {
        if (this.today) {
            this.todos = await api.get_todos_today();
        } else {
            this.todos = await api.get_todos_not_today();
        }
        console.log(this.todos);
    },
    methods: {
        open_modal() {
            if (this.today) {
                agendaModal.showModal();
            } else {
                todoModal.showModal();
            }
        },
        checked(t) {
            api.update_todo(t);
        }
    }
}
</script>