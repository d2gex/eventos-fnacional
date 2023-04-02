<template>
  <fieldset class="form-group border p-3">
    <legend class="w-auto px-2">Toreros</legend>
    <Form
        @submit="onSubmit"
        :initial-values="initialData"
        :validation-schema="schema"
    >
      <FieldArray name="toreroRow" v-slot="{ fields, push, remove }">
        <div class="row border border-primary">
          <div class="col-lg-6 float-left" v-for="(field, row) in fields" :key="field.key">
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
                            <Field :id="`toreroSurname_${row}`" type="text"
                                   :name="`toreroRow[${row}].toreroSurname`"
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
                            <Field :id="`toreroNickname_${row}`" type="text"
                                   :name="`toreroRow[${row}].toreroNickname`"
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
                            <Field :id="'tipoTorero_' + row" :name="`toreroRow[${row}].tipoTorero`"
                                   v-model="selected" as="select" class="form-control">
                              <option v-for="(tipo, tipo_index) in tipoToreros" :key="tipo_index" :value="tipo">
                                {{ tipo }}
                              </option>
                            </Field>
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
          <div class="col-lg-8 mx-auto my-3 border border-danger text-center">
            <button type="button"
                    @click="addToreroRow(push, fields.length)"
                    class="btn btn-success">Añadir +
            </button>
            <button type="button" @click="removeToreroRow(remove, row, fields.length) " class="btn btn-danger mx-2">
              Borrar -
            </button>
            <button type="submit" class="btn btn-secondary">Guardar</button>
          </div>
        </div>
      </FieldArray>
    </Form>
  </fieldset>
</template>

<script>
import {Field, Form, FieldArray, ErrorMessage} from 'vee-validate';
import {object as y_object, string as y_string, array as y_array} from "yup";
import {markRaw} from "vue";
import customErrorMessages from "@/assets/common";

export default {
  name: 'ToreroForm',
  components: {
    Form,
    Field,
    FieldArray,
    ErrorMessage,
  },
  data() {
    const tipoToreros = ['Torero', 'Rejoneador', 'Banderillero']
    const selected = 'Torero'
    const toreroRowFields = {
      toreroName: '',
      toreroSurname: '',
      toreroNickname: '',
      tipoTorero: ''
    };
    const initialData = {
      toreroRow: [toreroRowFields]
    }
    const schema = markRaw(y_object().shape({
      toreroRow: y_array()
          .of(
              y_object().shape({
                toreroName: y_string().required(customErrorMessages.required_with_name("El nombre")).min(2, customErrorMessages.min_2),
                toreroSurname: y_string().required(customErrorMessages.required_with_name("Los apellidos")).min(2, customErrorMessages.min_2),
                toreroNickname: y_string().min(2, customErrorMessages.min_2),
              })
          )
          .strict(),
    }));
    const maxRows = 6;
    return {
      tipoToreros,
      selected,
      toreroRowFields,
      initialData,
      schema,
      maxRows
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
