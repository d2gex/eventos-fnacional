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
                 placeholder="Entra el festejo *"/>
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
  }
}
</script>
