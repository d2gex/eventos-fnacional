import {defineStore} from 'pinia'
import {CommonUtils} from "@/assets/common";


export const toreroFestejoRowFields = {
    id: null,
    data: null,
    premios: [CommonUtils.selectedToreroPremio]
}
export const ganaderiaRowFields = {
    data: undefined
}

export const useFestejoStore = defineStore('festejoStore', {
    state: () => ({
        toreros: {
            rows: new Array(CommonUtils.maxNumInstances).fill(0).map(() =>
                (CommonUtils.deepCloneObject(toreroFestejoRowFields))),
        },
        ganaderias: {
            rows: new Array(CommonUtils.maxNumInstances).fill(0).map(() =>
                ({...ganaderiaRowFields})),
        }
    }), actions: {
        resetToreros() {
            this.toreros.rows = new Array(CommonUtils.maxNumInstances).fill(0).map(() =>
                (CommonUtils.deepCloneObject(toreroFestejoRowFields)))
        }, resetGanaderias() {
            this.ganaderias.rows = new Array(CommonUtils.maxNumInstances).fill(0).map(() =>
                ({...ganaderiaRowFields}))
        }
    }
})