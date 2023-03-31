<template>
  <fieldset class="form-group border p-3">
    <legend class="w-auto px-2">Ganaderias</legend>
    <Form
        @submit="onSubmit"
        :initial-values="initialData"
        :validation-schema="schema"
    >
      <FieldArray name="ganaderiaRow" v-slot="{ fields, push, remove }">
        <div class="row border border-primary">
          <div class="col-lg-12" v-for="(field, row) in fields" :key="field.key">
            <div class="card mt-2 mx-auto p-2 bg-light">
              <div class="card-body bg-light">
                <div class="container">
                  <form id="contact-form" role="form">
                    <div class="controls">
                      <h3 class="text-center">Ganadería {{ row + 1 }}</h3>
                      <div class="row">
                        <div class="col-md-12">
                          <div class="form-group">
                            <label :for="`ganaderiaName_${row}`">Nombre *</label>
                            <Field :id="`ganaderiaName_${row}`" type="text" :name="`ganaderiaRow[${row}].ganaderiaName`"
                                   class="form-control"
                                   placeholder="Entra el nombre *"/>
                            <div class="field-error">
                              <ErrorMessage as="div" :name="`ganaderiaRow[${row}].ganaderiaName`"/>
                            </div>

                          </div>
                        </div>
                        <div class="col-md-6">
                          <div class="form-group">
                            <label :for="'provincia_' + row">Provincia *</label>
                            <Field :id="'provincia_' + row" :name="`ganaderiaRow[${row}].provincia`"
                                   v-model="selected_provincia" as="select" class="form-control">
                              <option v-for="(prov, prov_index) in provincias" :key="prov_index" :value="prov">
                                {{ prov }}
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
          <div class="col-lg-12 mx-auto my-3 border border-danger text-center">
            <button type="button"
                    @click="addGanaderiaRow(push, fields.length)"
                    class="btn btn-success">Añadir +
            </button>
            <button type="button" @click="removeGanaderiaRow(remove, row, fields.length) " class="btn btn-danger mx-2">
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
import * as yup from "yup";
import customErrorMessages from "@/assets/common";

export default {
  name: 'GanaderiaForm',
  components: {
    Form,
    Field,
    FieldArray,
    ErrorMessage
  },
  data() {
    const provincias = ['Toledo', 'Granada', 'Sevilla']
    const selected_provincia = 'Toledo'
    const ganaderiaRowFields = {
      ganaderiaName: '',
      provincia: ''
    };
    const initialData = {
      ganaderiaRow: [ganaderiaRowFields]
    }
    const schema = yup.object().shape({
      ganaderiaRow: yup
          .array()
          .of(
              yup.object().shape({
                ganaderiaName: yup.string().required("El nombre es obligatorio").min(2, customErrorMessages.min_2)
              })
          )
          .strict(),
    });
    const maxRows = 6;
    return {
      schema,
      maxRows,
      ganaderiaRowFields,
      initialData,
      provincias,
      selected_provincia
    }
  },
  methods:
      {
        addGanaderiaRow(func, numRows) {
          if (numRows < this.maxRows) {
            func(this.ganaderiaRowFields)
          }
        },
        removeGanaderiaRow(func, index, numRows) {
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
