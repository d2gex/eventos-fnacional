import {defineStore} from 'pinia'
import {CommonUtils} from "@/assets/common";
import {shallowReactive} from "vue";

export const toreroFestejoRowFields = {
    id: null,
    data: null,
    premios: []
}
export const ganaderiaRowFields = {
    data: undefined
}

export const useFestejoStore = defineStore('festejoStore', {
    state: () => ({
        toreros: {
            rows: new Array(CommonUtils.maxNumInstances).fill(0).map(() => ({...toreroFestejoRowFields})),
        },
        ganaderias: {
            rows: new Array(CommonUtils.maxNumInstances).fill(0).map(() => ({...ganaderiaRowFields})),
        }
    }),
    actions: {
        resetToreros() {
            this.toreros.rows = new Array(CommonUtils.maxNumInstances).fill(0).map(() => ({...toreroFestejoRowFields}))
        },
        resetGanaderias() {
            this.ganaderias.rows = new Array(CommonUtils.maxNumInstances).fill(0).map(() => ({...ganaderiaRowFields}))
        }
    }
})