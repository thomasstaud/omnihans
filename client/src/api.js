import axios from "axios";

export async function get_weather() {
    const response = await axios.get(`http://10.0.0.7:5000/weather`, {});
    return response.data;
}

export async function get_todos_today() {
    const response = await axios.get(`http://10.0.0.7:5000/todos/today`, {});
    return response.data;
}

export async function save_todo(text, date) {
    const response = await axios.post(`http://10.0.0.7:5000/todos`, {text: text, date: date});
    return response.data;
}