<template>
  <div class="card">
    <DataTable :value="dataDeposit.newDbData"
               paginator
               :rows="50"
               :rowsPerPageOptions="[50, 100, 500]"
               v-model:filters="filters"
               v-model:expandedRows="expandedRows"
               v-model:selection="selectedRow"
               selectionMode="single"
               sortMode="multiple"
               dataKey="id"
               @rowExpand="onRowExpand"
               @rowCollapse="onRowCollapse"
               tableStyle="min-width: 60rem">
      <template #header>
        <div class="flex justify-content-start">
          <Button label="Copiar Fila"
                  icon="pi pi-copy"
                  severity="success"
                  :disabled="!Object.keys(selectedRow).length"
                  class="mr-5"/>
          <span class="p-input-icon-right">
                <i class="pi pi-search"/>
                <InputText v-model="filters['global'].value" placeholder="Busca la clave"/>
            </span>
        </div>
      </template>
      <Column expander style="width: 5rem"/>
      <Column field="id" header="ID"></Column>
      <Column field="poblacion" sortable header="Poblacion"></Column>
      <Column field="fecha" sortable header="Fecha"></Column>
      <Column field="nombre" sortable header="Festejo"></Column>
      <Column field="ganaderias" header="Ganaderias"></Column>
      <Column field="toreros" header="Toreros"></Column>
      <template #expansion="slotProps">
        <div class="p-3">
          <h5>Mas información {{ slotProps.data.Tipo }}</h5>
          <DataTable :value="[slotProps.data]">
            <Column field="premios" header="Premios"></Column>
            <Column field="notas" header="Notas"></Column>
          </DataTable>
        </div>
      </template>
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
import {usedataDepositStore} from "@/stores/dataDepositStore";

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
    const dataDeposit = usedataDepositStore();
    const expandedRows = [];
    const toast = markRaw(useToast());
    const selectedRow = {};
    const filters = {
      global: {value: null, matchMode: FilterMatchMode.CONTAINS}
    };
    return {
      dataDeposit,
      expandedRows,
      toast,
      selectedRow,
      filters
    }
  },
  methods: {
    onRowExpand(event) {
      this.toast.add({severity: 'info', summary: 'Producto Expandido', detail: event.data.name, life: 3000});
    },
    onRowCollapse(event) {
      this.toast.add({severity: 'success', summary: 'Product Colapsado', detail: event.data.name, life: 3000});
    }
  }
}
</script>