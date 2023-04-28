import {defineStore} from 'pinia'
import {CommonUtils} from "@/assets/common";

export const toreroRowFields = {
    id: null,
    nombre_profesional: '',
    tipo_torero_id: CommonUtils.selectedTipoTorero
}

export const useToreroStore = defineStore('toreroStore', {
    state: () => ({
        rows: new Array(CommonUtils.maxNumInstances).fill(0).map(() => ({...toreroRowFields})),
        initialData: {
            ganaderiaRow: [{...toreroRowFields}]
        }
    }),
    actions: {
        resetGanaderiaRowFields() {
            this.rows = new Array(CommonUtils.maxNumInstances).fill(0).map(() => ({...toreroRowFields}))
            this.initialData.ganaderiaRow = {...toreroRowFields}
        }
    }
})