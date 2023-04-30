<template>
  <div class="card">
    <DataTable :value="dataDeposit.ganaderiaItems.data"
               paginator
               :rows="50"
               :rowsPerPageOptions="[50, 100, 500]"
               v-model:filters="filters"
               v-model:selection="selectedRow"
               selectionMode="single"
               sortMode="multiple"
               dataKey="id"
               tableStyle="min-width: 60rem">
      <template #header>
         <div class="flex justify-content-start">
          <Button label="Copiar Fila"
                  icon="pi pi-copy"
                  severity="success"
                  :disabled="!Object.keys(selectedRow).length"
                  @click="copyRow"
                  class="mr-5"/>
          <span class="p-input-icon-right">
                <i class="pi pi-search"/>
                <InputText v-model="filters['global'].value" placeholder="Busca la clave"/>
            </span>
        </div>
      </template>
      <Column field="id" header="Ganaderia ID"></Column>
      <Column field="nombre_ganaderia" sortable header="Ganaderia"></Column>
      <Column field="provincia" sortable header="Provincia"></Column>
      <Column field="provincia_id" sortable header="Provincia ID"></Column>
    </DataTable>
    <Toast/>
  </div>
</template>

<script>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Toast from "primevue/toast";
import Button from "primevue/button";
import {FilterMatchMode} from "primevue/api";
import {useToast} from 'primevue/usetoast';
import InputText from "primevue/inputtext";
import {markRaw} from "vue";
import {useGanaderiaStore} from "@/stores/ganaderiaFormStore";
import {usedataDepositStore} from "@/stores/dataDepositStore";

export default {
  name: "GanaderiasTable",
  components: {
    DataTable,
    Column,
    Toast,
    Button,
    InputText
  },
  data() {
    const dataDeposit = usedataDepositStore()
    const ganaderiaStore = useGanaderiaStore()
    const toast = markRaw(useToast());
    const selectedRow = {};
    const filters = {
      global: {value: null, matchMode: FilterMatchMode.CONTAINS}
    };
    return {
      dataDeposit,
      ganaderiaStore,
      toast,
      selectedRow,
      filters
    }
  },
  methods: {
    async copyRow() {
      this.ganaderiaStore.rows[0].id = this.selectedRow.id
      this.ganaderiaStore.rows[0].nombre_ganaderia = this.selectedRow.nombre_ganaderia
      this.ganaderiaStore.rows[0].provincia_id = this.selectedRow.provincia_id
      await this.$vueAlert.alert("La ganadería '" + this.selectedRow.nombre_ganaderia + "' ha sido copiada", 'success')
    }
  }
}
</script>