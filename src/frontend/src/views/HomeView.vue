<template>
  <div class="row">
    <div class="col-md-8">
      <ToreroForm/>
    </div>
    <div class="col-md-4">
      <GanaderiaForm/>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import ToreroForm from '@/components/ToreroForm.vue'
import GanaderiaForm from '@/components/GanaderiaForm.vue'

export default {
  name: 'HomeView',
  components: {
    ToreroForm,
    GanaderiaForm
  }
}
</script>
