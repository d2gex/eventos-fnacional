<template>
  <div class="row">
    <div class="col-md-8">
      <ToreroForm :tipo-toreros="tipoToreros"/>
    </div>
    <div class="col-md-4">
      <GanaderiaForm :provincias="provincias"/>
    </div>
  </div>
  <div class="row">
    <div class="col-md-12">
      <FestejosForm
          :selected-provincia="selectedProvincia"
          :provincias="provincias"
          :selected-festejo="selectedFestejo"
          :tipo-festejos="tipoFestejos"/>
    </div>
  </div>
  <div class="row">
    <div class="col-md-12">
      <OldDbDatatable :data_url="oldDbDataUrl"/>
    </div>
  </div>

</template>

<script>
import axios from "axios";
import {CommonUtils} from "@/assets/common";
import ToreroForm from '@/components/ToreroForm.vue'
import GanaderiaForm from '@/components/GanaderiaForm.vue'
import FestejosForm from "@/components/FestejosForm.vue";
import OldDbDatatable from "@/components/OldDbDatatable.vue";

export default {
  name: 'HomeView',
  components: {
    ToreroForm,
    GanaderiaForm,
    FestejosForm,
    OldDbDatatable
  },
  data() {
    const selectedFestejo = 1;
    const tipoFestejos = [];
    const selectedProvincia = 45;
    const provincias = [];
    const tipoToreros = [];
    const oldDbDataUrl = CommonUtils.apiServerUrl + '/get_old_db_all_records';
    return {
      selectedFestejo,
      tipoFestejos,
      selectedProvincia,
      provincias,
      tipoToreros,
      oldDbDataUrl
    }
  },
  methods: {

    async getDataFromTable(end_point) {
      try {
        const response = await axios.get(end_point);
        return response
      } catch (error) {
        console.error(error);
      }
    }

  },
  async mounted() {
    // Get details for provinces
    let response = await this.getDataFromTable(CommonUtils.apiServerUrl + '/get_provincias')
    this.provincias = response.data

    // Get details for tipo toreros
    response = await this.getDataFromTable(CommonUtils.apiServerUrl + '/get_tipo_toreros')
    this.tipoToreros = response.data

     // Get details for tipo toreros
    response = await this.getDataFromTable(CommonUtils.apiServerUrl + '/get_tipo_festejos')
    this.tipoFestejos = response.data
  }
}
</script>
