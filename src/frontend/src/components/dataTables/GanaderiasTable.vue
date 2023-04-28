<template>
  <div class="card">
    <DataTable :value="products.value"
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
          <Button label="Copiar Fila" icon="pi pi-copy" severity="success" @click="copyRow"
                  :disabled="!Object.keys(selectedRow).length"/>
        </div>
        <div class="flex justify-content-end">
            <span class="p-input-icon-right">
                <i class="pi pi-search"/>
                <InputText v-model="filters['global'].value" placeholder="Busca la clave"/>
            </span>
        </div>
      </template>
      <Column field="id" header="ID"></Column>
      <Column field="nombre_ganaderia" sortable header="Ganaderia"></Column>
      <Column field="provincia_id" sortable header="Provincia_ID"></Column>
      <Column field="provincia" sortable header="Provincia"></Column>
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
import {CommonUtils} from "@/assets/common";
import InputText from "primevue/inputtext";
import {markRaw} from "vue";
import {useGanaderiaStore} from "@/stores/ganaderiaFormStore";

export default {
  name: "NewDbTable",
  components: {
    DataTable,
    Column,
    Toast,
    Button,
    InputText
  },
  data() {
    const ganaderiaStore = useGanaderiaStore()
    const products = {};
    const toast = markRaw(useToast());
    const selectedRow = {};
    const filters = {
      global: {value: null, matchMode: FilterMatchMode.CONTAINS}
    };
    return {
      ganaderiaStore,
      products,
      toast,
      selectedRow,
      filters
    }
  },
  methods: {
    async copyRow() {
      this.ganaderiaStore.ganaderiaRowFields['nombre_ganaderia'] = this.selectedRow.nombre_ganaderia
      this.ganaderiaStore.ganaderiaRowFields['provincia_id'] = this.selectedRow.provincia_id
      this.ganaderiaStore.ganaderiaRowFields['id'] = this.selectedRow.id
      await this.$vueAlert.alert("La ganadería '" + this.selectedRow.nombre_ganaderia + "' ha sido copiada" , 'success')
    }
  },
  async mounted() {
    const response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_ganaderias')
    this.products.value = response.data
  },
}
</script>