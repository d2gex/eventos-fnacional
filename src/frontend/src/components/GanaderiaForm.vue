<template>
  <fieldset class="form-group border p-3">
    <legend class="w-auto px-2">Ganaderias</legend>
    <Form
        @submit="onSubmit"
        :initial-values="this.ganaderiaStore.initialData"
        :validation-schema="schema"
    >
      <FieldArray name="ganaderiaRow" v-slot="{ fields, push, remove }">
        <div class="row border border-primary">
          <div class="col-lg-12" v-for="(field, row) in fields" :key="field.key">
            <div class="card mt-2 mx-auto p-2 bg-light">
              <div class="card-body bg-light">
                <div class="container">
                  <div class="controls">
                    <h3 class="text-center">Ganadería {{ row + 1 }}</h3>
                    <div class="row">
                      <div class="col-md-12">
                        <div class="form-group">
                          <label :for="`ganaderiaRow[${row}].nombre_ganaderia` + '_id'">Nombre *</label>
                          <Field :id="`ganaderiaRow[${row}].nombre_ganaderia` + '_id'" type="text"
                                 :name="`ganaderiaRow[${row}].nombre_ganaderia`"
                                 class="form-control"
                                 placeholder="Entra el nombre *"/>
                          <div class="field-error">
                            <ErrorMessage as="div" :name="`ganaderiaRow[${row}].nombre_ganaderia`"/>
                          </div>

                        </div>
                      </div>
                      <div class="col-md-6">
                        <div class="form-group">
                          <label :for="`ganaderiaRow[${row}].provincia_id` + '_id'">Provincia *</label>
                          <Field :id="`ganaderiaRow[${row}].provincia_id` + '_id'"
                                 :name="`ganaderiaRow[${row}].provincia_id`"
                                 v-model="ganaderiaStore.selected[row]" as="select" class="form-control">
                            <option v-for="option in provinciasData" :key="option.id" :value="option.id">
                              {{ option.provincia }}
                            </option>
                          </Field>
                        </div>
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
import {object as y_object, string as y_string, array as y_array} from "yup";
import {markRaw} from "vue";
import {customErrorMessages, CommonUtils} from "@/assets/common";
import {useGanaderiaStore} from "@/stores/ganaderiaFormStore";

export default {
  name: 'GanaderiaForm',
  props: {
    provincias: {
      type: Array,
      required: true
    }
  },
  components: {
    Form,
    Field,
    FieldArray,
    ErrorMessage
  },
  data() {
    const ganaderiaStore = useGanaderiaStore()
    const provinciasData = []
    const schema = markRaw(y_object().shape({
      ganaderiaRow: y_array()
          .of(
              y_object().shape({
                nombre_ganaderia: y_string().required(customErrorMessages.required_with_name("El nombre")).min(2, customErrorMessages.min_2)
              })
          )
          .strict(),
    }));
    const maxRows = 6;
    return {
      ganaderiaStore,
      provinciasData,
      schema,
      maxRows,
    }
  },
  methods:
      {
        addGanaderiaRow(func, numRows) {
          if (numRows < this.maxRows) {
            func(this.ganaderiaStore.ganaderiaRowFields)
          }
        },
        removeGanaderiaRow(func, index, numRows) {
          if (numRows > 1) {
            func(index)
          }
        },
        async onSubmit(values) {
          console.log(JSON.stringify(values, null, 2));
          const {data} = await CommonUtils.sendDataToBackend(values, '/save_ganaderia_details')
          if (data.status === 0) {
            await this.$vueAlert.alert(data.message)
          }
          console.log(JSON.stringify(data, null, 2));
        }
      },
  watch: {
    provincias(newProvincias) {
      this.provinciasData = newProvincias
    }
  }
}
</script>
