<template>
  <div v-if="fetchingData" class="container h-100">
    <div class="d-flex justify-content-md-center align-items-center vh-100">
      <ProgressSpinner/>
    </div>
  </div>
  <div v-else class="container">
    <div class="row">
      <TabView>
        <TabPanel header="Toreros Y Ganaderías">
          <div class="row">
            <div class="col-md-8">
              <ToreroForm/>
            </div>
            <div class="col-md-4">
              <GanaderiaForm/>
            </div>
          </div>
        </TabPanel>
        <TabPanel header="Festejos">
          <div class="row">
            <div class="col-md-12">
              <FestejosForm
                  :selected-festejo="selectedFestejo"
                  :tipo-festejos="tipoFestejos"
                  :selected-poblacion="selectedPoblacion"
                  :poblaciones="poblaciones"
              />
            </div>
          </div>
        </TabPanel>
      </TabView>
    </div>
    <div class="row">
      <TabView class="mt-4">
        <TabPanel header="Datos Originales">
          <div class="row">
            <div class="col-md-12">
              <OldDbTable/>
            </div>
          </div>
        </TabPanel>
        <TabPanel header="Nueva Base de Datos">
          <div class="row">
            <div class="col-md-12">
              <NewDbTable/>
            </div>
          </div>
        </TabPanel>
        <TabPanel header="Ganaderías">
          <div class="row">
            <div class="col-md-12">
              <GanaderiasTable/>
            </div>
          </div>
        </TabPanel>
        <TabPanel header="Toreros">
          <div class="row">
            <div class="col-md-12">
              <TorerosTable/>
            </div>
          </div>
        </TabPanel>
      </TabView>
    </div>
  </div>
</template>

<script>
import {CommonUtils} from "@/assets/common";
import ToreroForm from '@/components/ToreroForm.vue'
import GanaderiaForm from '@/components/GanaderiaForm.vue'
import FestejosForm from "@/components/festejos/FestejosForm.vue";
import TabView from 'primevue/tabview';
import TabPanel from 'primevue/tabpanel';
import OldDbTable from "@/components/dataTables/OldDbTable.vue";
import NewDbTable from "@/components/dataTables/NewDbTable.vue";
import GanaderiasTable from "@/components/dataTables/GanaderiasTable.vue";
import TorerosTable from "@/components/dataTables/TorerosTable.vue";
import {usedataDepositStore} from "@/stores/dataDepositStore";
import ProgressSpinner from 'primevue/progressspinner';

export default {
  name: 'HomeView',
  components: {
    ToreroForm,
    GanaderiaForm,
    FestejosForm,
    TabView,
    TabPanel,
    OldDbTable,
    NewDbTable,
    GanaderiasTable,
    TorerosTable,
    ProgressSpinner
  },
  data() {
    const dataDeposit = usedataDepositStore()
    const selectedFestejo = 1;
    const tipoFestejos = [];
    const selectedPoblacion = 0;
    const poblaciones = [];
    const fetchingData = false

    return {
      dataDeposit,
      selectedFestejo,
      tipoFestejos,
      selectedPoblacion,
      poblaciones,
      fetchingData
    }
  },
  async created() {
    this.fetchingData = true
    // Get Provincias details
    await this.dataDeposit.fetchAndStoreProvincias()
    // Get details for tipo toreros
    await this.dataDeposit.fetchAndTipoToreros()

    // Get details for tipo toreros
    let response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_tipo_festejos')
    this.tipoFestejos = response.data

    // Get details for toreros
    await this.dataDeposit.fetchAndStoreToreros()

    // Get details for ganaderias
    await this.dataDeposit.fetchAndStoreGanaderias()

    // Get details for premios
    await this.dataDeposit.fetchAndStoreTipoPremios()

    // Get details for poblaciones
    response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_poblaciones')
    this.poblaciones = response.data

    // get data from new db
    await this.dataDeposit.fetchAndStoreNewDbData()

    // get data from old db
    await this.dataDeposit.fetchAndStoreOldDbData()
    this.fetchingData = false
  }
}
</script>
<style>
.p-component, .p-component * {
  /* box-sizing: border-box; */
}

.p-tabview .p-tabview-panels {
  border: 2px #3B82F6 solid;

}

.p-tabview .p-tabview-nav {
  background-color: #999999;
  padding-top: 3px;
  border: None;
}

.p-tabview .p-tabview-nav li.p-tabview-header .p-tabview-nav-link {
  border-top-left-radius: 30%;
  border-top-right-radius: 30%;
  border-bottom: None;
  border-color: #6c757d;
  border-width: 3px;
}

.p-tabview .p-tabview-nav li.p-highlight .p-tabview-nav-link {
  border-top-left-radius: 30%;
  border-top-right-radius: 30%;
  border-color: #3B82F6;
  border-width: 3px;
}

</style>

