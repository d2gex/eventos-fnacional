<template>
  <!--  <div class="row">-->
  <!--    <div class="col-md-8">-->
  <!--      <ToreroForm/>-->
  <!--    </div>-->
  <!--    <div class="col-md-4">-->
  <!--      <GanaderiaForm/>-->
  <!--    </div>-->
  <!--  </div>-->
  <!--  <div class="row">-->
  <!--    <div class="col-md-12">-->
  <!--      <FestejosForm/>-->
  <!--    </div>-->
  <!--  </div>-->
    <div class="row">
      <div class="col-md-12">
        <FestejoToreros :items="items"/>
      </div>
    </div>

</template>

<script>

// import ToreroForm from '@/components/ToreroForm.vue'
// import GanaderiaForm from '@/components/GanaderiaForm.vue'
// import FestejosForm from "@/components/FestejosForm.vue";
import FestejoToreros from "@/components/FestejoToreros.vue";

export default {
  name: 'HomeView',
  components: {
    FestejoToreros
    // FestejosForm,
    // ToreroForm,
    // GanaderiaForm,
  },
  data() {
    return {
      items: ["Jose Antonio", "Daniel Garcia", "David 'El Litri'", "Sonia Espartaca", "Laura Fogar 'La Cute'"].map(v => v.toLowerCase()),
    }
  }
}
</script>
