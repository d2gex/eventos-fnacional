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
                            <label :for="`toreroRow[${row}].nombre` + '_id'">Nombre *</label>
                            <Field :id="`toreroRow[${row}].nombre` + '_id'" type="text" :name="`toreroRow[${row}].nombre`"
                                   class="form-control"
                                   placeholder="Entra el nombre *"/>
                            <div class="field-error">
                              <ErrorMessage as="div" :name="`toreroRow[${row}].nombre`"/>
                            </div>

                          </div>
                        </div>
                        <div class="col-md-6">
                          <div class="form-group">
                            <label :for="`toreroRow[${row}].apellidos` + '_id'">Apellidos *</label>
                            <Field :id="`toreroRow[${row}].apellidos` + '_id'" type="text"
                                   :name="`toreroRow[${row}].apellidos`"
                                   class="form-control"
                                   placeholder="Entra los apellidos *"/>
                            <div class="field-error">
                              <ErrorMessage :name="`toreroRow[${row}].apellidos`"/>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="row">
                        <div class="col-md-6">
                          <div class="form-group">
                            <label :for="`toreroRow[${row}].apodo` + '_id'">Apodo </label>
                            <Field :id="`toreroRow[${row}].apodo` + '_id'" type="text"
                                   :name="`toreroRow[${row}].apodo`"
                                   class="form-control"
                                   placeholder="Entra el apodo"/>
                            <div class="field-error">
                              <ErrorMessage :name="`toreroRow[${row}].apodo`"/>
                            </div>
                          </div>
                        </div>
                        <div class="col-md-6">
                          <div class="form-group">
                            <label :for="`toreroRow[${row}].tipo_torero_id` + '_id'">Tipo de Torero *</label>
                            <Field :id="`toreroRow[${row}].tipo_torero_id` + '_id'" :name="`toreroRow[${row}].tipo_torero_id`"
                                   v-model="selected[row]" as="select" class="form-control">
                              <option v-for="option in tipoToreros" :key="option.id" :value="option.id">
                                {{ option.tipo }}
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
import {customErrorMessages, CommonUtils} from "@/assets/common";

export default {
  name: 'ToreroForm',
  components: {
    Form,
    Field,
    FieldArray,
    ErrorMessage,
  },
  data() {
    const tipoToreros = [
        {id: 1, tipo: 'Torero'},
        {id: 2, tipo: 'Rejoneador'},
    ];
    const selected = Array(6).fill(1);
    const toreroRowFields = {
      nombre: '',
      apellidos: '',
      apodo: '',
      tipo_torero_id: ''
    };
    const initialData = {
      toreroRow: [toreroRowFields]
    };
    const schema = markRaw(y_object().shape({
      toreroRow: y_array()
          .of(
              y_object().shape({
                nombre: y_string().required(customErrorMessages.required_with_name("El nombre")).min(2, customErrorMessages.min_2),
                apellidos: y_string().required(customErrorMessages.required_with_name("Los apellidos")).min(2, customErrorMessages.min_2),
                apodo: y_string().min(2, customErrorMessages.min_2),
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
          const {data} = CommonUtils.sendDataToBackend(values, '/save_torero_details')
          console.log(JSON.stringify(data, null, 2));
        }
      }
}
</script>
