<template>
  <div class="row mt-4">
    <div class="col-md-4" v-for="(_, row) in numRows" :key="toreroNumRow.toString() + '_' + row">
      <div class="form-group">
        <label :for="`${fieldName}[${row}]_id`">Estado Faena {{ row + 1 }}<span class="field_required">*</span></label>
        <MultiSelect v-model="storeData.estados[row]"
                     :options="items"
                     :maxSelectedLabels="2"
                     :option-label="optionLabel"
                     class="form-control"/>
        <small class="p-error" id="dd-error">{{ errorMessage || '&nbsp;' }}</small>
      </div>
    </div>
  </div>
  <div class="row">
    <div class="col-md-12">
        <button type="button"
                @click="addPremioRow()"
                class="btn btn-success">+
        </button>
        <button type="button" @click="removePremioRow() " class="btn btn-danger mx-2">-
        </button>
    </div>
  </div>

</template>

<script>
import {CommonUtils} from "@/assets/common";
import MultiSelect from "primevue/multiselect";
import {useField} from 'vee-validate';

export default {
  name: "FestejoToreroEstados",
  props: {
    toreroNumRow: {
      type: Number,
      required: true
    },
    fieldName: {
      type: String,
      required: true
    },
    items: {
      type: Array,
      required: true
    },
    placeHolder: {
      type: String,
      required: true
    },
    optionLabel: {
      type: String,
      required: true
    },
    inputObject: {
      type: Object,
      required: true
    },
    resetFormFlag: {
      type: Boolean,
    }
  },
  components: {
    MultiSelect
  },
  data() {
    const numRows = 1
    const {value, errorMessage} = useField(this.fieldName);
    const storeData = {}
    return {
      numRows,
      value,
      errorMessage,
      storeData
    }
  },
  methods: {
    addPremioRow() {
      if (this.numRows < CommonUtils.maxNumInstances) {
        this.numRows++
        this.storeData.estados.push([this.items[CommonUtils.selectedToreroEstado]])
      }
    },
    removePremioRow() {
      if (this.numRows > 1) {
        this.numRows--
        this.storeData.estados.pop()

      }
    },
    resetForm() {
      this.numRows = 1
    },
    initSelectedEstadoForRowZero(estados, row) {
      if (estados[row] === null) {
        return [[this.items[CommonUtils.selectedToreroEstado]]]
      }
      return estados
    }
  },
  watch: {
    // eslint-disable-next-line no-unused-vars
    'inputObject.estados': function (newEstados) {
      // Ensure that storeData is up to date with inputObject and does not lose its reference
      this.storeData = this.inputObject
      if (this.storeData.estados.length === 1) {
        this.storeData.estados = this.initSelectedEstadoForRowZero(this.storeData.estados, 0)
      }

    },
    'storeData.estados': {
      deep: true,
      handler (newEstados) {
        this.value = newEstados
      }
    },
    resetFormFlag(newValue) {
      if (newValue === true) {
        this.resetForm()
      }
    }
  },
  beforeMount() {
    this.storeData = this.inputObject;
    if (this.storeData.estados.length === 1) {
      this.storeData.estados = this.initSelectedEstadoForRowZero(this.storeData.estados, 0)
    }
  }
}
</script>
<style>
.p-multiselect .p-multiselect-label {
  padding: 0;
}
.p-multiselect .p-multiselect-trigger {
  width: 0;
}
</style>