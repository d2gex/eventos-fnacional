<template>
  <div class="card mt-2 mx-auto p-2 bg-light">
    <h4 class="text-center">Ganaderías del Festejo</h4>
    <div class="card-body bg-light">
      <div class="container">
        <div class="row">
          <div class="col-md-12" v-for="(_, row) in numRows" :key="row">
            <div class="form-group">
              <label :for="`ganaderiaName_${row}`">Ganaderia <span class="field_required">*</span></label>
              <SearchDropdownBox
                  :items="dataDeposit.ganaderiaItems"
                  :input-value="festejoSstore.ganaderias.rows[row]"
                  :field-name="`ganaderiaRow[${row}].ganaderiaName`"
                  place-holder="Selecciona una ganaderia"
                  option-label="nombre_ganaderia"/>

            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-12">
            <div class="form-group">
              <button type="button"
                      @click="addGanaderiaRow"
                      class="btn btn-success">Añadir Ganadería +
              </button>
              <button type="button" @click="removeGanaderiaRow" class="btn btn-danger mx-2">Borar Ganadería -
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import SearchDropdownBox from "@/components/SearchDropdownBox.vue";
import {CommonUtils} from "@/assets/common";
import {usedataDepositStore} from "@/stores/dataDepositStore";
import {useFestejoStore} from "@/stores/festejoStore";

export default {
  name: "FestejoGanaderias",
  components: {
    SearchDropdownBox
  },
  data() {
    const dataDeposit = usedataDepositStore()
    const festejoSstore = useFestejoStore()
    const numRows = 1;

    return {
      dataDeposit,
      festejoSstore,
      numRows
    }
  },
  methods:
      {
        addGanaderiaRow() {
          if (this.numRows < CommonUtils.maxNumInstances) {
            this.numRows++
          }
        },
        removeGanaderiaRow() {
          if (this.numRows > 1) {
            this.numRows--
          }
        }
      }
}
</script>
