<template>
  <div class="row">
    <div class="col-md-4" v-for="(_, row) in numRows" :key="toreroNumRow.toString() + '_' + row">
      <div class="form-group">
        <label :for="`${fieldName}[${row}]_id`">Premio</label>
        <Field :id="`${fieldName}[${row}]_id`"
               :name="`${fieldName}[${row}]`"
               v-model="tipoPremioSelected[row]"
               as="select"
               class="form-select">
          <option v-for="option in tipoPremios" :key="option.id" :value="option.id">
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
    selectedToreroPremio: {
      type: Number,
      required: true
    },
    toreroPremiosData: {
      type: Array,
      required: true
    }
  },
  components: {
    Field
  },
  data() {
    const maxRows = 6;
    const numRows = 1;
    const tipoPremios = []
    const tipoPremioSelected = []
    return {
      maxRows,
      numRows,
      tipoPremios,
      tipoPremioSelected,
    }
  },
  methods:
      {
        addPremioRow() {
          if (this.numRows < this.maxRows) {
            this.numRows++
          }
        },
        removePremioRow() {
          if (this.numRows > 1) {
            this.numRows--
          }
        },
        updatetoreroPremiosData(newTipoPremio) {
          this.tipoPremios = newTipoPremio
          this.tipoPremioSelected = Array(this.maxRows).fill(this.tipoPremios[this.selectedToreroPremio].id)
        }
      },
  watch: {
    toreroPremiosData(newTipoPremio) {
      // Update an instance of this component when fetching the  api data for the first time
      this.updatetoreroPremiosData(newTipoPremio)
    }
  },
  mounted() {
    // Update cloned copies of this component once the api data has been fetched.
    if (this.toreroPremiosData.length) {
      this.updatetoreroPremiosData(this.toreroPremiosData)
    }

  }
}
</script>
