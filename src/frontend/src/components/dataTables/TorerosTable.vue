<template>
  <div class="card">
    <DataTable :value="dataDeposit.toreroItems"
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
      <Column field="id" header="Toero ID"></Column>
      <Column field="nombre" sortable header="Nombre"></Column>
      <Column field="apellidos" sortable header="Apellidos"></Column>
      <Column field="apodo" sortable header="Apodo"></Column>
      <Column field="nombre_profesional" sortable header="Nombre Profesional"></Column>
      <Column field="tipo_torero" sortable header="Tipo Torero"></Column>
      <Column field="tipo_torero_id" sortable header="Tipo ID"></Column>
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
import {useToreroStore} from "@/stores/toreroFormStore";
import {usedataDepositStore} from "@/stores/dataDepositStore";

export default {
  name: "TorerosTable",
  components: {
    DataTable,
    Column,
    Toast,
    Button,
    InputText
  },
  data() {
    const dataDeposit = usedataDepositStore()
    const toreroStore = useToreroStore()
    const toast = markRaw(useToast());
    const selectedRow = {};
    const filters = {
      global: {value: null, matchMode: FilterMatchMode.CONTAINS}
    };
    return {
      dataDeposit,
      toreroStore,
      toast,
      selectedRow,
      filters
    }
  },
  methods: {
    async copyRow() {
      this.toreroStore.rows[0].id = this.selectedRow.id
      this.toreroStore.rows[0].nombre = this.selectedRow.nombre
      this.toreroStore.rows[0].apellidos = this.selectedRow.apellidos
      this.toreroStore.rows[0].apodo = this.selectedRow.apodo
      this.toreroStore.rows[0].nombre_profesional = this.selectedRow.nombre_profesional
      this.toreroStore.rows[0].tipo_torero_id = this.selectedRow.tipo_torero_id
      await this.$vueAlert.alert("El torero '" + this.selectedRow.nombre_profesional + "' ha sido copiado", 'success')
    }
  }
}
</script>