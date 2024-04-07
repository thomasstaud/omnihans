<template>
    <dialog id="todoModal" class="modal">
    <div class="modal-box text-center">
        <textarea v-model="text" class="textarea textarea-bordered" placeholder="TODO" @click="sent=false"></textarea> <br>
        <input v-model="date" class="input" type="date" @click="sent=false">
        <form class="text-center" method="dialog">
            <button class="btn btn-ghost fa fa-save w-15 mx-1" @click="save_todo()"></button>
            <button class="btn btn-ghost fa fa-times w-15 mx-1"></button>
        </form>
    </div>
    </dialog>
</template>

<script>
import * as api from "../api.js";

export default {
    data() {
        return {
            text: null,
            date: null,
            sent: false
        }
    },
    methods: {
      async save_todo() {
        await api.save_todo(this.text, this.date);
        this.sent = true;

        this.text = null;
        this.date = null;
      }
    }
}
</script>