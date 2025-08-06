import axios from "axios";

export async function get_weather() {
    const response = await axios.get(`http://192.168.178.100:5000/weather`, {});
    return response.data;
}

export async function get_todos_today() {
    const response = await axios.get(`http://192.168.178.100:5000/todos/today`, {});
    return response.data;
}

export async function get_todos_not_today() {
    const response = await axios.get(`http://192.168.178.100:5000/todos/not-today`, {});
    return response.data;
}

export async function save_todo(text, date) {
    const response = await axios.post(`http://192.168.178.100:5000/todos`, {text: text, date: date});
    return response.data;
}

export async function update_todo(todo) {
    todo.checked = !todo.checked
    const response = await axios.put(`http://192.168.178.100:5000/todos`, todo);
    return response.data;
}
