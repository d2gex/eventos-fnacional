import {defineStore} from 'pinia'
import {CommonUtils} from "@/assets/common";

const ganaderiaRowFields = {
    id: null,
    nombre_ganaderia: '',
    provincia_id: CommonUtils.selectedProvincia
}

export const useGanaderiaStore = defineStore('ganaderiaStore', {
    state: () => ({
        selected: Array(CommonUtils.maxNumInstances).fill(CommonUtils.selectedProvincia),
        ganaderiaRowFields: ganaderiaRowFields,
        initialData: {
            ganaderiaRow: [ganaderiaRowFields]
        }
    }),
    actions: {
        resetGanaderiaRowFields() {
            this.ganaderiaRowFields = ganaderiaRowFields
            this.initialData.ganaderiaRow = ganaderiaRowFields
        }
    }
})