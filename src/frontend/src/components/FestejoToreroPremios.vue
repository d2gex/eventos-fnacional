<template>
  <div class="row">
    <div class="col-md-4" v-for="row in numRows" :key="toreroNumRow.toString() + '_' + row">
      <div class="form-group">
        <label :for="`${fieldName}[${row}]_id`">Premio</label>
        <Field :id="`${fieldName}[${row}]_id`" :name="`${fieldName}[${row}]`"
               v-model="tipoPremioSelected[row]" as="select" class="form-control">
          <option v-for="(tipo, tipo_index) in tipoPremios" :key="tipo_index" :value="tipo">
            {{ tipo }}
          </option>
        </Field>
      </div>
    </div>
  </div>
  <div class="row">
    <div class="col-md-12">
      <div class="form-group">
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
    }
  },
  components: {
    Field
  },
  data() {
    const maxRows = 6;
    const numRows = 1;
    const tipoPremios = ['N', 'O', 'OO', 'OOR'];
    const tipoPremioSelected = Array(maxRows).fill(tipoPremios[0])
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
        }
      }
}
</script>
