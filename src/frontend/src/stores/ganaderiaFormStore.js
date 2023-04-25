import {defineStore} from 'pinia'

const ganaderiaRowFields = {
    nombre_ganaderia: '',
    provincia_id: ''
}

export const useGanaderiaStore = defineStore('ganaderiaStore', {
    state: () => ({
        selected: Array(6).fill(45),
        ganaderiaRowFields: ganaderiaRowFields,
        initialData: {
            ganaderiaRow: [ganaderiaRowFields]
        }
    }),
})