<template>
  <div class="row">
    <div class="col-md-4" v-for="(_, row) in numRows" :key="toreroNumRow.toString() + '_' + row">
      <div class="form-group">
        <label :for="`${fieldName}[${row}]_id`">Premio Faena {{row + 1}}<span class="field_required">*</span></label>
        <Field :id="`${fieldName}[${row}]_id`"
               :name="`${fieldName}[${row}]`"
               v-model="festejoStore.toreros.rows[toreroNumRow].premios[row]"
               as="select"
               class="form-select">
          <option v-for="option in dataDeposit.premioToreroItems.data" :key="option.id" :value="option.id">
            {{ option.tipo_premio }}
          </option>
        </Field>
      </div>
    </div>
  </div>
  <div class="row">
    <div class="col-md-12">
      <div class="form-group mt-4">
        <button type="button"
                @click="addPremioRow()"
                class="btn btn-success">+
        </button>
        <button type="button" @click="removePremioRow() " class="btn btn-danger mx-2">-
        </button>
      </div>
    </div>
  </div>

</template>

<script>
import {Field} from "vee-validate";
import {CommonUtils} from "@/assets/common";
import {useFestejoStore} from "@/stores/festejoStore";
import {usedataDepositStore} from "@/stores/dataDepositStore";

export default {
  name: "FestejoToreroPremios",
  props: {
    toreroNumRow: {
      type: Number,
      required: true
    },
    fieldName: {
      type: String,
      required: true
    },
    resetFormFlag: {
      type: Boolean,
    }
  },
  components: {
    Field
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
        addPremioRow() {
          if (this.numRows < CommonUtils.maxNumInstances) {
            this.numRows++
            this.festejoStore.toreros.rows[this.toreroNumRow].premios.push(CommonUtils.selectedToreroPremio)
          }
        },
        removePremioRow() {
          if (this.numRows > 1) {
            this.numRows--
            this.festejoStore.toreros.rows[this.toreroNumRow].premios.pop()

          }
        },
        resetForm() {
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
