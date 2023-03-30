<template>
  <div class="container">
    <div class="row " v-for="row in numRows" :key="row">
      <div class="col-lg-6 mx-auto">
        <div class="card mt-2 mx-auto p-2 bg-light">
          <div class="card-body bg-light">
            <div class="container">
              <form id="contact-form" role="form">
                <div class="controls">
                  <div class="row">
                    <div class="col-md-6">
                      <div class="form-group">
                        <label :for="'torero_name_' + row">Nombre *</label>
                        <input :id="'torero_name_' + row" type="text" :name="'torero_name_' + row" class="form-control"
                               placeholder="Entra el nombre *" required="required"
                               data-error="Nombre es requerido.">

                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="form-group">
                        <label :for="'torero_surname_' + row">Apellidos *</label>
                        <input :id="'torero_surname_' + row" type="text" :name="'torero_surname_' + row"
                               class="form-control"
                               placeholder="Entra los apellidos *" required="required"
                               data-error="Nombre es requerido.">
                      </div>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-md-6">
                      <div class="form-group">
                        <label :for="'torero_nickname_' + row">Apodo *</label>
                        <input :id="'torero_nickname_' + row" type="text" :name="'torero_nickname_' + row"
                               class="form-control"
                               placeholder="Entra el apodo *">
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="form-group">
                        <label :for="'tipo_torero_' + row">Tipo de Torero *</label>
                        <select :id="'tipo_torero_' + row" :name="'tipo_torero_' + row" class="form-control">
                          <option selected value="Torero">Torero</option>
                          <option value="Rejoneador">Rejoneador</option>
                          <option value="Novillero">Novillero</option>
                        </select>

                      </div>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-md-6">
                      <div class="form-group">
                        <label :for="'nombre_profesional' + row">Nombre Profesional *</label>
                        <input :id="'nombre_profesional' + row" type="text" :name="'nombre_profesional' + row"
                               class="form-control"
                               placeholder="Entra el nombre profesional *" required="required"
                               data-error="Nombre profesional es requerido.">
                      </div>
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
      <div class="col-lg-6 mx-auto my-3">
        <button type="button" @click="addToreroRow" class="btn btn-success">Añadir Torero</button>
        <button type="button" @click="deleteToreroRow" class="btn btn-danger">Borrar Torero</button>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: 'BullFighterRow',
  data() {
    return {
      numRows: 1,
      maxRows: 6
    }
  },
  methods:
      {
        addToreroRow() {
          if (this.numRows < this.maxRows) {
            this.numRows++
          }
        },
        deleteToreroRow() {
          if (this.numRows > 1) {
            this.numRows--
          }
        }
      }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
body {
  font-family: 'Lato', sans-serif;
}

h1 {
  margin-bottom: 40px;
}

label {
  color: #333;
}

.help-block.with-errors {
  color: #ff5050;
  margin-top: 5px;

}

.card {
  margin-left: 10px;
  margin-right: 10px;
}

</style>
