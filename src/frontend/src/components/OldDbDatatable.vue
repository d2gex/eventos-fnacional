<script setup>
import DataTable from 'datatables.net-vue3';
import DataTablesCore from 'datatables.net-bs5';
import {defineProps} from "vue";

defineProps({
  data_url: {
    type: String,
    required: true
  }
})

DataTable.use(DataTablesCore);

const columns = [
  {data: 'Lugar'},
  {data: 'Fecha'},
  {data: 'Dia Semana'},
  {data: 'Tipo'},
  {data: 'Ganaderia'},
  {data: 'Toreros'},
  {data: 'Notas'},
  {data: 'Foto'},
  {data: 'Cartel'},
  {data: 'Fecha Real'},
  {data: 'Fuente'},
];
</script>

<template>
  <fieldset class="form-group border p-3">
    <legend class="w-auto px-2">Registros de la base de datos antigua</legend>
    <div class="container">
      <DataTable
          :columns="columns"
          :ajax="data_url"
          class="table table-hover table-striped"
          width="100%"
      >
        <thead>
        <tr>
          <th>Lugar</th>
          <th>Fecha</th>
          <th>Dis s.</th>
          <th>Tipo</th>
          <th>Ganaderia</th>
          <th>Toreros</th>
          <th>Notas</th>
          <th>Foto</th>
          <th>Cartel</th>
          <th>Fecha real</th>
          <th>Fuente</th>
        </tr>
        </thead>
        <tfoot>
        <tr>
          <th>Lugar</th>
          <th>Fecha</th>
          <th>Dis s.</th>
          <th>Tipo</th>
          <th>Ganaderia</th>
          <th>Toreros</th>
          <th>Notas</th>
          <th>Foto</th>
          <th>Cartel</th>
          <th>Fecha real</th>
          <th>Fuente</th>
        </tr>
        </tfoot>
      </DataTable>
    </div>
  </fieldset>
</template>
