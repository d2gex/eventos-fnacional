<template>
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
                :selected-toreros="selectedTorero"
                :toreros-data="toreroItems"
                :selected-torero-premio="selectedToreroPremio"
                :torero-premios-data="premioToreroItems"
                :selected-poblacion="selectedPoblacion"
                :poblaciones="poblaciones"
            />
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
      <TabPanel header="Ganaderías">
        <div class="row">
          <div class="col-md-12">
            <GanaderiasTable/>
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
import FestejosForm from "@/components/festejos/FestejosForm.vue";
import TabView from 'primevue/tabview';
import TabPanel from 'primevue/tabpanel';
import OldDbTable from "@/components/dataTables/OldDbTable.vue";
import NewDbTable from "@/components/dataTables/NewDbTable.vue";
import GanaderiasTable from "@/components/dataTables/GanaderiasTable.vue";
import {usedataDepositStore} from "@/stores/dataDepositStore";

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
    GanaderiasTable
  },
  data() {
    const dataDeposit = usedataDepositStore()
    const selectedFestejo = 1;
    const tipoFestejos = [];
    const selectedTorero = 0;
    const toreroItems = [];
    const selectedToreroPremio = 0;
    const premioToreroItems = [];
    const selectedPoblacion = 0;
    const poblaciones = [];

    return {
      dataDeposit,
      selectedFestejo,
      tipoFestejos,
      selectedTorero,
      toreroItems,
      selectedToreroPremio,
      premioToreroItems,
      selectedPoblacion,
      poblaciones
    }
  },
  async created() {

    await this.dataDeposit.fetchAndStoreProvincias()

    // Get details for tipo toreros
    await this.dataDeposit.fetchAndTipoToreros()

    // Get details for tipo toreros
    let response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_tipo_festejos')
    this.tipoFestejos = response.data

    // Get details for toreros
    response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_toreros')
    this.toreroItems = response.data

    // Get details for ganaderias
    await this.dataDeposit.fetchAndStoreGanaderias()

    // Get details for premios
    response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_tipo_premios')
    this.premioToreroItems = response.data

    // Get details for poblaciones
    response = await CommonUtils.getDataFromTable(CommonUtils.apiServerUrl + '/get_poblaciones')
    this.poblaciones = response.data
  }
}
</script>
