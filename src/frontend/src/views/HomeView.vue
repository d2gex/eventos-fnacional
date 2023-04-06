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
      <SearchBox type="text"
                 id="nombreProfesional_id"
                 name='nombreProfesional'
                 placeholder="Entra el nombre *"
                 :items="items"/>
    </div>
  </div>
</template>

<script>

// import ToreroForm from '@/components/ToreroForm.vue'
// import GanaderiaForm from '@/components/GanaderiaForm.vue'
// import FestejosForm from "@/components/FestejosForm.vue";
import SearchBox from "@/components/SearchBox.vue";

export default {
  name: 'HomeView',
  components: {
    // FestejosForm,
    // ToreroForm,
    // GanaderiaForm,
    SearchBox
  },
  data() {
    return {
      items: ["Jose Antonio", "Daniel Garcia", "David 'El Litri'", "Sonia Espartaca", "Laura Fogar 'La Cute'"].map(v => v.toLowerCase()),
    }
  }
}
</script>
