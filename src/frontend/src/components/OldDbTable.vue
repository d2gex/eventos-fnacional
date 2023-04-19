<!--  {data: 'Lugar'},-->
<!--  {data: 'Fecha'},-->
<!--  {data: 'Dia Semana'},-->
<!--  {data: 'Tipo'},-->
<!--  {data: 'Ganaderia'},-->
<!--  {data: 'Toreros'},-->
<!--  {data: 'Notas'},-->
<!--  {data: 'Foto'},-->
<!--  {data: 'Cartel'},-->
<!--  {data: 'Fecha Real'},-->
<!--  {data: 'Fuente'}

,-->
<template>
  <div class="card">
    <DataTable :value="products.value"
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
            <Button text icon="pi pi-plus" label="Expand All" @click="expandAll"/>
            <Button text icon="pi pi-minus" label="Collapse All" @click="collapseAll"/>
          </div>
          <div class="flex justify-content-end">
            <span class="p-input-icon-right">
                <i class="pi pi-search"/>
                <InputText v-model="filters['global'].value" placeholder="Busca la clave"/>
            </span>
          </div>
      </template>
      <Column expander style="width: 5rem"/>
      <Column field="id" header="ID"></Column>
      <Column field="Lugar" sortable header="Lugar"></Column>
      <Column field="Fecha" sortable header="Fecha"></Column>
      <Column field="Tipo" sortable header="Tipo"></Column>
      <Column field="Ganaderia" header="Ganaderia"></Column>
      <Column field="Toreros" header="Toreros"></Column>
            <template #expansion="slotProps">
              <div class="p-3">
                <h5>Mas información {{ slotProps.data.Tipo }}</h5>
                <DataTable :value="[slotProps.data]">
                  <Column field="Dia Semana" header="Dia Semana"></Column>
                  <Column field="Notas" header="Notas"></Column>
                  <Column field="Fotos" header="Fotos"></Column>
                  <Column field="Cartel" header="Cartel"></Column>
                  <Column field="Fecha Real" header="Fecha Real"></Column>
                  <Column field="Fuente" header="Fuente"></Column>
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
import {CommonUtils} from "@/assets/common";
import InputText from "primevue/inputtext";
import {markRaw} from "vue";

export default {
  name: "OldDbTable",
  components: {
    DataTable,
    Column,
    Toast,
    Button,
    InputText
  },
  data() {
    const products = {};
    const expandedRows = [];
    const toast = markRaw(useToast());
    const selectedRow = {};
    const filters = {
      global: {value: null, matchMode: FilterMatchMode.CONTAINS}
    };
    return {
      products,
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
    },
    expandAll() {
      this.expandedRows.value = this.products.value.filter((p) => p.id);
    },
    collapseAll() {
      this.expandedRows.value = null;
    }
  },
  async mounted() {
    const response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_old_db_all_records')
    this.products.value = response.data
  },
}
</script>