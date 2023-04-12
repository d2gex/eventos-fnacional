<script setup>
import DataTable from 'datatables.net-vue3';
import DataTablesCore from 'datatables.net-bs5';

DataTable.use(DataTablesCore);

const columns = [
  { data: 'name' },
  { data: 'position' },
  { data: 'office' },
  { data: 'extn' },
  { data: 'start_date' },
  { data: 'salary' },
];
</script>

<template>
  <div class="container">
    <h1>Bootstrap 5 styled DataTable</h1>
    <h2>DataTables + Vue3 example</h2>
    <p>
      In this example we show a DataTable in a Vue3 application being styled by
      Bootstrap 5. DataTables supports a number of other styling libraries as
      well, such as Bulma, Foundation, Boostrap 3, 4 and others.
    </p>

    <DataTable
      :columns="columns"
      ajax="http://localhost:5000/api/get_old_db_all_records"
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
</template>
