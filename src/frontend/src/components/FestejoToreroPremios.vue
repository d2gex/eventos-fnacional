<template>
  <div class="row">
    <div class="col-md-4" v-for="row in numRows" :key="buildUniqueKey(row)">
      <div class="form-group">
        <label :for="`premioRow[${buildUniqueKey(row)}]`">Premio</label>
        <Field :id="`premio_id_${buildUniqueKey(row)}`" :name="`premioRow[${buildUniqueKey(row)}]`"
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
  name: "PremiosTorero",
  props: {
    toreroNumRow: Number
  },
  components: {
    Field
  },
  data() {
    const maxRows = 6;
    const numRows = 1
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
        },
        buildUniqueKey(key) {
          return this.toreroNumRow + '_' + key
        }
      }
}
</script>
