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
                  :items="ganaderiasData"
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
    const numRows = 1;
    const ganaderiasData = [];
    return {
      ganaderiasData,
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
        },
        updateItems(newGanaderiaItems) {
          this.ganaderiasData = newGanaderiaItems
        }
      },
  watch: {
    // Update an instance of this component when fetching the  api data for the first time
    items(newItems) {
      this.updateItems(newItems)
    }
  },
  mounted() {
    // Update cloned copies of this component once the api data has been fetched.
    if (this.items.length) {
      this.updateItems(this.items)
    }
  }
}
</script>
