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
  {data: 'name'},
  {data: 'position'},
  {data: 'office'},
  {data: 'extn'},
  {data: 'start_date'},
  {data: 'salary'},
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
          <th>Name</th>
          <th>Position</th>
          <th>Office</th>
          <th>Extn.</th>
          <th>Start date</th>
          <th>Salary</th>
        </tr>
        </thead>
        <tfoot>
        <tr>
          <th>Name</th>
          <th>Position</th>
          <th>Office</th>
          <th>Extn.</th>
          <th>Start date</th>
          <th>Salary</th>
        </tr>
        </tfoot>
      </DataTable>
    </div>
  </fieldset>
</template>
