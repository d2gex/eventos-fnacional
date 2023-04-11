<template>
  <div class="row border border-primary">
    <div class="col-md-12" v-for="row in numRows" :key="row">
      <div class="card mt-2 mx-auto p-2 bg-light">
        <div class="card-body bg-light">
          <div class="container">
            <form id="contact-form" role="form">
              <div class="controls">
                <h3 class="text-center">Torero/Premio {{ row + 1 }}</h3>
                <div class="row">
                  <div class="col-md-6">
                    <div class="form-group">
                      <label :for="`toreroName_${row}`">Torero *</label>
                      <SearchBox type="text"
                                 :name="`toreroRow[${row}].toreroName`"
                                 :items="items"/>
                    </div>
                  </div>
                  <div class="col-md-6">
                    <PremiosTorero :torero-num-row="row"/>
                  </div>
                </div>
              </div>
            </form>
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
import SearchBox from "@/components/SearchBox.vue";
import PremiosTorero from "@/components/PremiosTorero.vue";

export default {
  name: "FestejoToreros",
  props: {
    items: {
      type: Array,
      required: true
    }
  },
  components: {
    SearchBox,
    PremiosTorero,
  },
  data() {
    const maxRows = 6;
    const numRows = 1
    const toreroRowFields = {
      toreroName: '',
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
