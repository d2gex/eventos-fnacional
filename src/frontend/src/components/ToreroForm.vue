<template>
  <div class="container">
    <Form
        @submit="onSubmit"
        :initial-values="initialData"
        :validation-schema="schema"
        novalidate
    >
      <FieldArray name="toreroRow" v-slot="{ fields, push, remove }">
        <div class="row border border-primary">
          <div class="col-lg-4 float-left" v-for="(field, row) in fields" :key="field.key">
            <div class="card mt-2 mx-auto p-2 bg-light">
              <div class="card-body bg-light">
                <div class="container">
                  <form id="contact-form" role="form">
                    <div class="controls">
                      <h3 class="text-center">Torero {{ row + 1 }}</h3>
                      <div class="row">
                        <div class="col-md-6">
                          <div class="form-group">
                            <label :for="`toreroName_${row}`">Nombre *</label>
                            <Field :id="`toreroName_${row}`" type="text" :name="`toreroRow[${row}].toreroName`"
                                   class="form-control"
                                   placeholder="Entra el nombre *"/>
                            <div class="field-error">
                              <ErrorMessage as="div" :name="`toreroRow[${row}].toreroName`"/>
                            </div>

                          </div>
                        </div>
                        <div class="col-md-6">
                          <div class="form-group">
                            <label :for="`toreroSurname_${row}`">Apellidos *</label>
                            <Field :id="`toreroSurname_${row}`" type="text" :name="`toreroRow[${row}].toreroSurname`"
                                   class="form-control"
                                   placeholder="Entra los apellidos *"/>
                            <div class="field-error">
                              <ErrorMessage :name="`toreroRow[${row}].toreroSurname`"/>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="row">
                        <div class="col-md-6">
                          <div class="form-group">
                            <label :for="`toreroNickname_${row}`">Apodo </label>
                            <Field :id="`toreroNickname_${row}`" type="text" :name="`toreroRow[${row}].toreroNickname`"
                                   class="form-control"
                                   placeholder="Entra el apodo"/>
                            <div class="field-error">
                              <ErrorMessage :name="`toreroRow[${row}].toreroNickname`"/>
                            </div>
                          </div>
                        </div>
                        <div class="col-md-6">
                          <div class="form-group">
                            <label :for="'tipo_torero_' + row">Tipo de Torero *</label>
                            <select :id="'_tipo_torero_' + row" :name="'tipo_torero_' + row" class="form-control">
                              <option selected value="Torero">Torero</option>
                              <option value="Rejoneador">Rejoneador</option>
                              <option value="Novillero">Novillero</option>
                            </select>

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
          <div class="col-lg-6 mx-auto my-3 border border-danger text-center">
            <button type="button"
                    @click="addToreroRow(push, fields.length)"
                    class="btn btn-success">Añadir Torero +
            </button>
            <button type="button" @click="removeToreroRow(remove, row, fields.length) " class="btn btn-danger mx-2">
              Borrar Torero -
            </button>
            <button type="submit" class="btn btn-secondary">Guardar Toreros</button>
          </div>
        </div>
      </FieldArray>
    </Form>
  </div>

</template>

<script>
import {Field, Form, FieldArray, ErrorMessage} from 'vee-validate';
import * as yup from "yup";

export default {
  name: 'ToreroForm',
  components: {
    Form,
    Field,
    FieldArray,
    ErrorMessage
  },
  data() {
    const customErrorMessages = {
      min_2: "Mínima longitud: 2 caracteres"
    }
    const toreroRowFields = {
      toreroName: '',
      toreroSurname: '',
      toreroNickname: ''
    };
    const initialData = {
      toreroRow: [toreroRowFields]
    }
    const schema = yup.object().shape({
      toreroRow: yup
          .array()
          .of(
              yup.object().shape({
                toreroName: yup.string().required("El nombre es obligatorio").min(2, customErrorMessages.min_2),
                toreroSurname: yup.string().required("Los apellidos son obligatorios").min(2, customErrorMessages.min_2),
                toreroNickname: yup.string().min(2, customErrorMessages.min_2),
              })
          )
          .strict(),
    });
    const maxRows = 6;
    return {
      schema,
      maxRows,
      toreroRowFields,
      initialData
    }
  },
  methods:
      {
        addToreroRow(func, numRows) {
          if (numRows < this.maxRows) {
            func(this.toreroRowFields)
          }
        },
        removeToreroRow(func, index, numRows) {
          if (numRows > 1) {
            func(index)
          }
        },
        onSubmit(values) {
          console.log(JSON.stringify(values, null, 2));
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

.error {
  color: red;
}

</style>
