import {defineStore} from 'pinia'
import {CommonUtils} from "@/assets/common";

export const toreroFestejoRowFields = {
    id: null,
    torero: undefined,
    premios: []
}



export const useFestejoStore = defineStore('festejoStore', {
    state: () => ({
        toreros: {
            rows: new Array(CommonUtils.maxNumInstances).fill(0).map(() => ({...toreroFestejoRowFields})),
        },
        ganaderias: {
            rows: new Array(CommonUtils.maxNumInstances).fill(undefined),
        }
    }),
    actions: {}
})