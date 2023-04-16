<template>
  <div class="row border border-primary">
    <div class="col-md-12" v-for="(_, row) in numRows" :key="row">
      <div class="card mt-2 mx-auto p-2 bg-light">
        <div class="card-body bg-light">
          <div class="container">
            <div class="controls">
              <h3 class="text-center">Torero y Premios {{ row }}</h3>
              <div class="row">
                <div class="col-md-6">
                  <div class="form-group">
                    <label :for="`toreroName_${row}`">Torero *</label>
                    <SearchDropdownBox
                                       :selected="selected"
                                       :items="items"
                                       :field-name="`toreroRow[${row}].toreroName`"/>
                  </div>
                </div>
                <div class="col-md-6">
                  <PremiosTorero :torero-num-row="row" :field-name="`toreroRow[${row}].toreroPremios`"/>
                </div>
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
    <div class="col-lg-8 mx-auto my-3 border border-danger text-center">
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
import PremiosTorero from "@/components/FestejoToreroPremios.vue";

export default {
  name: "FestejoToreros",
  props: {
    items: {
      type: Array,
      required: true
    },
    selected: {
      type: Object,
      required: true
    }
  },
  components: {
    SearchDropdownBox,
    PremiosTorero,
  },
  data() {
    const maxRows = 6;
    const numRows = 1;
    const toreroRowFields = {
      toreroName: '',
      toreroPremios: Array
    };
    const initialData = {
      toreroRow: [toreroRowFields]
    };
    return {
      maxRows,
      numRows,
      toreroRowFields,
      initialData
    }
  },
  methods:
      {
        addToreroPremioRow() {
          if (this.numRows < this.maxRows) {
            this.numRows++
          }
        },
        removeToreroPremioRow() {
          if (this.numRows > 1) {
            this.numRows--
          }
        },
      }
}
</script>
