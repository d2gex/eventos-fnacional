<template>
  <div class="card mt-2 mx-auto p-2 bg-light">
    <h3 class="text-center">Ganaderías del Festejo</h3>
    <div class="card-body bg-light">
      <div class="container">
        <div class="row">
          <div class="col-md-12" v-for="(_, row) in numRows" :key="row">
            <div class="form-group">
              <label :for="`ganaderiaName_${row}`">Ganaderia *</label>
              <SearchDropdownBox
                  :selectedItem="selected"
                  :items="items"
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

export default {
  name: "FestejoGanaderias",
  components: {
    SearchDropdownBox
  },
  props: {
    items: {
      type: Array,
      required: true
    },
    selected: {
      type: Number,
      required: true
    }
  },
  data() {
    const maxRows = 6;
    const numRows = 1
    return {
      maxRows,
      numRows
    }
  },
  methods:
      {
        addGanaderiaRow() {
          if (this.numRows < this.maxRows) {
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
