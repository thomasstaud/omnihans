<template>
    <dialog :id="id" class="modal">
    <div class="modal-box text-center shadow-lg rounded-lg">
        <textarea v-model="text" class="textarea textarea-bordered m-2" placeholder="TODO" @click="sent=false"></textarea> <br>
        <input v-if="dateField" v-model="date" class="input m-2" type="date" @click="sent=false">
        <form class="text-center m-2" method="dialog">
            <button class="btn btn-ghost fa fa-save w-15 mx-1" @click="save_todo()"></button>
            <button class="btn btn-ghost fa fa-times w-15 mx-1"></button>
        </form>
    </div>
    </dialog>
</template>

<script>
import * as api from "../api.js";

export default {
    props: {
        id: String,
        dateField: Boolean
    },
    data() {
        return {
            text: null,
            date: this.getDefaultDate(),
            // what is this for?
            sent: false
        }
    },
    methods: {
        getDefaultDate() {
            // default date is today
            var defaultDate = new Date();
            if (this.dateField) {
                // if there is a date field, default date is tomorrow
                defaultDate.setDate(defaultDate.getDate() + 1);
            }
            return defaultDate.toISOString().slice(0, 10);
        },
        async save_todo() {
            await api.save_todo(this.text, this.date);
            this.sent = true;

            this.text = null;
            this.date = this.getDefaultDate();
        }
    }
    
}
</script>