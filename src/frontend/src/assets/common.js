import axios from "axios";

const customErrorMessages = {
    min_2: "Mínima longitud: 2 caracteres",
    required_with_name: function (name) {
        return name + " es obligatorio"
    }
}

const CommonUtils = {
    apiServerUrl: "http://127.0.0.1:5000/api",
    capitalizeWords: function (str) {
        return str
            .toLowerCase()
            .split(' ')
            .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
            .join(' ');
    },
    sendDataToBackend: async function (data, end_point) {
        try {
            const url = this.apiServerUrl + end_point
            const response = await axios.post(url, data);
            console.log(response);
        } catch (error) {
            console.error(error);
        }
    }

}

export {customErrorMessages, CommonUtils}