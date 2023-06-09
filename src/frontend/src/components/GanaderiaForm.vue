<template>
  <fieldset class="form-group border p-3">
    <Form
        :initial-values="ganaderiaStore.initialData"
        :validation-schema="schema"
        v-slot={handleSubmit}
    >
      <form @submit.prevent>
        <FieldArray name="ganaderiaRow" v-slot="{ fields, push, remove }">
          <div class="row ">
            <div class="col-lg-12" v-for="(field, row) in fields" :key="field.key">
              <div class="card mt-2 mx-auto p-2 bg-light">
                <h4 class="text-center">Ganadería {{ row + 1 }}</h4>
                <div class="card-body bg-light">
                  <div class="container">
                    <div class="controls">
                      <div class="row">
                        <div class="col-md-12">
                          <div class="form-group">
                            <Field type="hidden"
                                   :id="`ganaderiaRow[${row}].id` + '_id'"
                                   :name="`ganaderiaRow[${row}].id`"
                                   v-model="ganaderiaStore.rows[row].id"/>

                            <label :for="`ganaderiaRow[${row}].nombre_ganaderia` + '_id'">Nombre <span
                                class="field_required">*</span></label>
                            <Field :id="`ganaderiaRow[${row}].nombre_ganaderia` + '_id'" type="text"
                                   :name="`ganaderiaRow[${row}].nombre_ganaderia`"
                                   v-model="ganaderiaStore.rows[row].nombre_ganaderia"
                                   class="form-control"
                                   placeholder="Entra el nombre *"/>
                            <div class="field-error">
                              <ErrorMessage as="div" :name="`ganaderiaRow[${row}].nombre_ganaderia`"/>
                            </div>
                          </div>

                        </div>
                        <div class="col-md-6">
                          <div class="form-group">
                            <label :for="`ganaderiaRow[${row}].provincia_id` + '_id'">Provincia <span
                                class="field_required">*</span></label>
                            <Field :id="`ganaderiaRow[${row}].provincia_id` + '_id'"
                                   :name="`ganaderiaRow[${row}].provincia_id`"
                                   v-model="ganaderiaStore.rows[row].provincia_id"
                                   as="select"
                                   class="form-select">
                              <option v-for="option in dataDeposit.provincias.data" :key="option.id" :value="option.id">
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
            <div class="col-lg-12 mx-auto my-3  text-center">
              <button type="button"
                      @click="addGanaderiaRow(push, fields)"
                      class="btn btn-success">Añadir +
              </button>
              <button type="button" @click="removeGanaderiaRow(remove, fields) "
                      class="btn btn-danger mx-2">
                Borrar -
              </button>
              <button @click="handleSubmit((values) => {onSubmit(values, push, remove, fields)})"
                      class="btn btn-primary">Guardar
              </button>
            </div>
          </div>
        </FieldArray>
      </form>
    </Form>
  </fieldset>
</template>

<script>
import {Field, Form, FieldArray, ErrorMessage} from 'vee-validate';
import {object as y_object, string as y_string, array as y_array} from "yup";
import {markRaw} from "vue";
import {customErrorMessages, CommonUtils} from "@/assets/common";
import {useGanaderiaStore, ganaderiaRowFields} from "@/stores/ganaderiaFormStore";
import {usedataDepositStore} from "@/stores/dataDepositStore";

export default {
  name: 'GanaderiaForm',
  components: {
    Form,
    Field,
    FieldArray,
    ErrorMessage
  },
  data() {
    const ganaderiaStore = useGanaderiaStore();
    const dataDeposit = usedataDepositStore();
    const schema = markRaw(y_object().shape({
      ganaderiaRow: y_array()
          .of(
              y_object().shape({
                nombre_ganaderia: y_string().required(customErrorMessages.required_with_name("El nombre")).min(2, customErrorMessages.min_2)
              })
          )
          .strict(),
    }));
    return {
      ganaderiaStore,
      dataDeposit,
      schema,
    }
  },
  methods:
      {
        addGanaderiaRow(funcPush, addedFields) {
          if (addedFields.length < CommonUtils.maxNumInstances) {
            funcPush({...ganaderiaRowFields})
          }
        },
        removeGanaderiaRow(funcRemove, addedFields) {
          if (addedFields.length > 1) {
            const fieldKey = addedFields[addedFields.length - 1].key
            funcRemove(fieldKey)
          }
        },
        resetForm(push, remove, fields) {
          for (let i = fields.length - 1; i >= 0; i--) {
            remove(fields[i])
          }
          this.ganaderiaStore.resetGanaderiaRowFields()
          push({...ganaderiaRowFields})
        },
        async onSubmit(values, funcPush, funcRemove, rowFields) {
          console.log(JSON.stringify(values, null, 2));
          const {data} = await CommonUtils.sendDataToBackend(values, '/save_ganaderia_details')
          if (data.status === 0) {
            await this.$vueAlert.alert(data.message, "Error en la operación", 'error')
          } else {
            await this.dataDeposit.fetchAndStoreGanaderias()
            this.resetForm(funcPush, funcRemove, rowFields)
            await this.$vueAlert.alert("Las nuevas ganaderias han sido guardadas", "Operación satisfactoria", 'success')
          }
          console.log(JSON.stringify(data, null, 2));
        }
      }
}
</script>
