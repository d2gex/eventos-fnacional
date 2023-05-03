<template>
  <div class="row ">
    <div class="col-md-12" v-for="(_, row) in numRows" :key="row">
      <div class="card mt-2 mx-auto p-2 bg-light">
        <h4 class="text-center">Torero y Premios {{ row + 1 }}</h4>
        <div class="card-body bg-light">
          <div class="container">
            <div class="controls">
              <div class="row">
                <div class="col-md-6">
                  <div class="form-group">
                    <label :for="`toreroName_${row}`">Torero <span class="field_required">*</span></label>
                    <SearchDropdownBox
                        :input-object="festejoStore.toreros.rows[row]"
                        :items="dataDeposit.toreroItems.data"
                        :field-name="`toreroRow[${row}].toreroName`"
                        place-holder="Selecciona un torero"
                        option-label="nombre_profesional"/>
                  </div>
                </div>
                <div class="col-md-6">
                  here the extra data
                </div>
              </div>
              <div class="row">
                <PremiosTorero :torero-num-row="row"
                               :field-name="`toreroRow[${row}].premios`"
                               :reset-form-flag="resetFormFlag"/>
              </div>
              <div class="row">
                <FestejoToreroEstados
                    :items="dataDeposit.estadoToreroItems.data"
                    :torero-num-row="row"
                    :field-name="`toreroRow[${row}].estados`"
                    :reset-form-flag="resetFormFlag "
                    :input-object="festejoStore.toreros.rows[row]"
                    place-holder="Selecciona un estado"
                    option-label="tipo_estado"/>
              </div>

            </div>
          </div>
        </div>
      </div>
      <!-- /.8 -->
    </div>
    <!-- /.row-->
  </div>
  <div class="row ">
    <div class="col-lg-8 mx-auto my-3  text-center">
      <button type="button"
              @click="addToreroPremioRow"
              class="btn btn-success">Añadir Torero +
      </button>
      <button type="button" @click="removeToreroPremioRow" class="btn btn-danger mx-2">
        Borrar Torero -
      </button>
    </div>
  </div>
</template>

<script>
import SearchDropdownBox from "@/components/SearchDropdownBox.vue";
import PremiosTorero from "@/components/festejos/FestejoToreroPremios.vue";
import FestejoToreroEstados from "@/components/festejos/FestejoToreroEstados.vue";
import {CommonUtils} from "@/assets/common";
import {useFestejoStore} from "@/stores/festejoStore";
import {usedataDepositStore} from "@/stores/dataDepositStore";

export default {
  name: "FestejoToreros",
  props: {
    resetFormFlag: {
      type: Boolean,
    }
  },
  components: {
    SearchDropdownBox,
    PremiosTorero,
    FestejoToreroEstados
  },
  data() {
    const dataDeposit = usedataDepositStore()
    const festejoStore = useFestejoStore()
    const numRows = 1;
    return {
      dataDeposit,
      festejoStore,
      numRows,
    }
  },
  methods:
      {
        addToreroPremioRow() {
          if (this.numRows < CommonUtils.maxNumInstances) {
            this.numRows++
          }
        },
        removeToreroPremioRow() {
          if (this.numRows > 1) {
            this.numRows--
          }
        },
        resetForm() {
          this.festejoStore.resetToreros()
          this.numRows = 1
        }
      },
  watch: {
    resetFormFlag(newValue) {
      if (newValue === true) {
        this.resetForm()
      }
    }
  }
}
</script>
