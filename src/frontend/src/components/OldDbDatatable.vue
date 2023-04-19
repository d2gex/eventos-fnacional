<template>
  <div class="container">
    <DataTable
        :columns="columns"
        :ajax="data_url"
        :options="options"
        class="table table-hover table-striped"
        width="100%"
    >
      <thead>
      <tr>
        <th>Lugar</th>
        <th>Fecha</th>
        <th>Dia s.</th>
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
</template>

<script setup>
import DataTable from 'datatables.net-vue3';
import DataTablesCore from 'datatables.net-bs5';
import 'datatables.net-select';
import 'datatables.net-responsive';
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
const options = {
  pageLength: 50,
  select: true,
  responsive: true
}

</script>

<style>
@import 'datatables.net-dt';
@import 'datatables.net-select-dt';
@import 'datatables.net-responsive-dt';
</style>
