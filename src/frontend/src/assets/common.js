const customErrorMessages = {
    min_2: "Mínima longitud: 2 caracteres",
    required_with_name: function (name) {
        return name + " es obligatorio"
    }
}

const CommonUtils = {
    capitalizeWords: function (str) {
        return str
            .toLowerCase()
            .split(' ')
            .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
            .join(' ');
    },
    apiServerUrl : "http://127.0.0.1:5000/api"

}

export {customErrorMessages, CommonUtils}