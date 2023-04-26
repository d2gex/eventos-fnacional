import {defineStore} from 'pinia'
import {CommonUtils} from "@/assets/common";

const ganaderiaRowFields = {
    nombre_ganaderia: '',
    provincia_id: ''
}

export const useGanaderiaStore = defineStore('ganaderiaStore', {
    state: () => ({
        selected: Array(CommonUtils.maxNumInstances).fill(CommonUtils.selectedProvincia),
        ganaderiaRowFields: ganaderiaRowFields,
        initialData: {
            ganaderiaRow: [ganaderiaRowFields]
        }
    }),
})