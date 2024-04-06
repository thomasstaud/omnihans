import axios from "axios";

export async function get_weather() {
    const response = await axios.get(`http://localhost:5000/weather`, {});
    return response.data;
}