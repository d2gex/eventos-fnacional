import {defineStore} from 'pinia'
import {CommonUtils} from "@/assets/common";


export const usedataDepositStore = defineStore('dataDepositStore', {
    state: () => ({
        provincias: [],
        tipoToreros: [],
        tipoFestejos: [],
        toreroItems: [],
        ganaderiaItems: [],
        premioToreroItems: [],
        poblaciones: [],
        newDbData: [],
    }),
    actions: {
        async fetchAndStoreProvincias() {
            const response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_provincias')
            this.provincias = response.data
        },
        async fetchAndTipoToreros() {
            const response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_tipo_toreros')
            this.tipoToreros = response.data
        },
        async getTipoFestejos() {
            const response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_tipo_festejos')
            this.tipoFestejos = response.data
        },
        async getToreros() {
            const response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_toreros')
            this.toreroItems = response.data
        },
        async fetchAndStoreGanaderias() {
            const response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_ganaderias')
            this.ganaderiaItems = response.data
        },
        async getTipoPremios() {
            const response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_tipo_premios')
            this.premioToreroItems = response.data
        },
        async getPoblaciones() {
            const response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_poblaciones')
            this.poblaciones = response.data
        },
        async fetchAndStoreNewDbData() {
            const response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_db_all_records')
            this.newDbData = response.data
        }
    }
})