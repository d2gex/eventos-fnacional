<template>
  <div class="row">
    <TabView>
      <TabPanel header="Toreros Y Ganaderías">
        <div class="row">
          <div class="col-md-8">
            <ToreroForm :tipo-toreros="tipoToreros"/>
          </div>
          <div class="col-md-4">
            <GanaderiaForm/>
          </div>
        </div>
      </TabPanel>
      <TabPanel header="Festejos">
        <div class="row">
          <div class="col-md-12">
<!--            <FestejosForm-->
<!--                :selected-festejo="selectedFestejo"-->
<!--                :tipo-festejos="tipoFestejos"-->
<!--                :selected-toreros="selectedTorero"-->
<!--                :toreros-data="toreroItems"-->
<!--                :selected-ganaderias="selectedGanaderia"-->
<!--                :ganaderias-data="ganaderiaItems"-->
<!--                :selected-torero-premio="selectedToreroPremio"-->
<!--                :torero-premios-data="premioToreroItems"-->
<!--                :selected-poblacion="selectedPoblacion"-->
<!--                :poblaciones="poblaciones"-->
<!--            />-->
          </div>
        </div>
      </TabPanel>
    </TabView>
  </div>
  <div class="row">
    <TabView>
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
    </TabView>
  </div>


</template>

<script>
import {CommonUtils} from "@/assets/common";
import ToreroForm from '@/components/ToreroForm.vue'
import GanaderiaForm from '@/components/GanaderiaForm.vue'
// import FestejosForm from "@/components/FestejosForm.vue";
import TabView from 'primevue/tabview';
import TabPanel from 'primevue/tabpanel';
import OldDbTable from "@/components/OldDbTable.vue";
import NewDbTable from "@/components/NewDbTable.vue";
import {usedataDepositStore} from "@/stores/dataDepositStore";

export default {
  name: 'HomeView',
  components: {
    ToreroForm,
    GanaderiaForm,
    // FestejosForm,
    TabView,
    TabPanel,
    OldDbTable,
    NewDbTable
  },
  data() {
    const dataDeposit = usedataDepositStore()
    const selectedFestejo = 1;
    const tipoFestejos = [];
    const selectedTorero = 0;
    const toreroItems = [];
    const selectedGanaderia = 0;
    const ganaderiaItems = [];
    const selectedToreroPremio = 0;
    const premioToreroItems = [];
    const selectedPoblacion = 0;
    const poblaciones = [];
    const tipoToreros = [];

    return {
      dataDeposit,
      selectedFestejo,
      tipoFestejos,
      selectedTorero,
      toreroItems,
      selectedGanaderia,
      ganaderiaItems,
      selectedToreroPremio,
      premioToreroItems,
      selectedPoblacion,
      poblaciones,
      tipoToreros,
    }
  },
  async created() {

    await this.dataDeposit.fetchAndStoreProvincias()

    // Get details for tipo toreros
    let response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_tipo_toreros')
    this.tipoToreros = response.data

    // Get details for tipo toreros
    response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_tipo_festejos')
    this.tipoFestejos = response.data

    // Get details for toreros
    response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_toreros')
    this.toreroItems = response.data

    // Get details for ganaderias
    response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_ganaderias')
    this.ganaderiaItems = response.data

    // Get details for premios
    response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_tipo_premios')
    this.premioToreroItems = response.data

    // Get details for poblaciones
    response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_poblaciones')
    this.poblaciones = response.data
  }
}
</script>
