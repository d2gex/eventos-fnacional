import {defineStore} from 'pinia'
import {CommonUtils} from "@/assets/common";

export const ganaderiaRowFields = {
    id: null,
    nombre_ganaderia: '',
    provincia_id: CommonUtils.selectedProvincia
}

export const useGanaderiaStore = defineStore('ganaderiaStore', {
    state: () => ({
        rows: new Array(CommonUtils.maxNumInstances).fill(0).map(() => ({...ganaderiaRowFields})),
        initialData: {
            ganaderiaRow: [{...ganaderiaRowFields}]
        }
    }),
    actions: {
        resetGanaderiaRowFields() {
            this.rows = new Array(CommonUtils.maxNumInstances).fill(0).map(() => ({...ganaderiaRowFields}))
            this.initialData.ganaderiaRow = {...ganaderiaRowFields}
        }
    }
})