<script setup>
import ToDoModal from "./ToDoModal.vue";
</script>

<template>
<div class="card bg-base-200 w-96 shadow-lg m-5">
<div class="card-body">
    <p>{{ title }}</p>
    <ul class="list bg-base-100 rounded-box shadow-md my-5">
        <li v-for="t in todos" class="list-row">
            <div v-html="format_date(t.date)" class="text-base-content/30"></div>
            <div class="list-col-grow align-middle">{{ t.text }}</div>
            <input v-model="t.checked" type="checkbox" class="checkbox align-middle" @click="checked(t)" />
        </li>
    </ul>
    <button class="btn btn-sm bg-base-300 text-lg my-2 mx-8 rounded-full" @click="open_modal()">+</button>

    <ToDoModal v-if="today" id="agendaModal" @todo_added="refresh_todos()"/>
    <ToDoModal v-if="!today" id="todoModal" date-field @todo_added="refresh_todos()"/>
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
        this.refresh_todos();
    },
    methods: {
        async refresh_todos() {
            if (this.today) {
                this.todos = await api.get_todos_today();
            } else {
                this.todos = await api.get_todos_not_today();
            }
            console.log(this.todos);
        },
        open_modal() {
            if (this.today) {
                agendaModal.showModal();
            } else {
                todoModal.showModal();
            }
        },
        checked(t) {
            api.update_todo(t);
        },
        format_date(date) {
            // assumes date has YYYY-MM-DD format
            // returns date as DD\nMM
            
            return date.slice(5).split("-").reverse().join(" ");
        }
    }
}
</script>