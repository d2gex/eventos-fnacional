<template>
  <div class="row">
    <div class="col-md-8">
      <ToreroForm/>
    </div>
    <div class="col-md-4">
      <GanaderiaForm/>
    </div>
  </div>
  <div class="row">
    <div class="col-md-12">
      <FestejosForm/>
    </div>
  </div>


</template>

<script>

import ToreroForm from '@/components/ToreroForm.vue'
import GanaderiaForm from '@/components/GanaderiaForm.vue'
import FestejosForm from "@/components/FestejosForm.vue";


export default {
  name: 'HomeView',
  components: {
    ToreroForm,
    GanaderiaForm,
    FestejosForm,

  }
}
</script>
