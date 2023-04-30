import {defineStore} from 'pinia'
import {CommonUtils} from "@/assets/common";
import {shallowReactive} from "vue";


export const usedataDepositStore = defineStore('dataDepositStore', {
    state: () => ({
        provincias: shallowReactive({data: []}),
        tipoToreros: shallowReactive({data: []}),
        tipoFestejos: [],
        toreroItems: shallowReactive({data: []}),
        ganaderiaItems: shallowReactive({data: []}),
        premioToreroItems: [],
        poblaciones: [],
        newDbData: shallowReactive({data: []}),
        oldDbData: shallowReactive({data: []}),
    }),
    actions: {
        async fetchAndStoreProvincias() {
            const response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_provincias')
            this.provincias.data = response.data
        },
        async fetchAndTipoToreros() {
            const response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_tipo_toreros')
            this.tipoToreros.data = response.data
        },
        async getTipoFestejos() {
            const response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_tipo_festejos')
            this.tipoFestejos = response.data
        },
        async fetchAndStoreToreros() {
            const response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_toreros')
            this.toreroItems.data = response.data
        },
        async fetchAndStoreGanaderias() {
            const response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_ganaderias')
            this.ganaderiaItems.data = response.data
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
            this.newDbData.data = response.data
        },
        async fetchAndStoreOldDbData() {
            const response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_old_db_all_records')
            this.oldDbData.data = response.data
        }
    }
})