<template>
  <div class="row">
    <div class="col-md-8">
      <ToreroForm/>
    </div>
    <div class="col-md-4">
      <GanaderiaForm :provincias="provincias"/>
    </div>
  </div>
  <div class="row">
    <div class="col-md-12">
      <FestejosForm/>
    </div>
  </div>


</template>

<script>
import axios from "axios";
import {CommonUtils} from "@/assets/common";
import ToreroForm from '@/components/ToreroForm.vue'
import GanaderiaForm from '@/components/GanaderiaForm.vue'
import FestejosForm from "@/components/FestejosForm.vue";

export default {
  name: 'HomeView',
  components: {
    ToreroForm,
    GanaderiaForm,
    FestejosForm,
  },
  data() {
    const provincias = []
    return {
      provincias
    }
  },
  methods: {

    async getProvinces(end_point) {
      try {
        return await axios.get(end_point);
      } catch (error) {
        console.error(error);
      }
    }

  },
  async mounted() {
    const response = await this.getProvinces(CommonUtils.apiServerUrl + '/get_provincias')
    this.provincias = response.data
  }
}
</script>
