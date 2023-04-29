<template>
  <fieldset class="form-group border p-3">
    <legend class="w-auto px-2">Toreros</legend>
    <Form
        :initial-values="toreroStore.initialData"
        :validation-schema="schema"
        v-slot={handleSubmit}
    >
      <form @submit.prevent>
        <FieldArray name="toreroRow" v-slot="{ fields, push, remove }">
          <div class="row border border-primary">
            <div class="col-lg-6 float-left" v-for="(field, row) in fields" :key="field.key">
              <div class="card mt-2 mx-auto p-2 bg-light">
                <div class="card-body bg-light">
                  <div class="container">
                      <div class="controls">
                        <h3 class="text-center">Torero {{ row + 1 }}</h3>
                        <div class="row">
                          <div class="col-md-6">
                            <div class="form-group">
                              <Field type="hidden"
                                     :id="`toreroRow[${row}].id` + '_id'"
                                     :name="`toreroRow[${row}].id`"
                                     v-model="toreroStore.rows[row].id"/>

                              <label :for="`toreroRow[${row}].nombre` + '_id'">Nombre *</label>
                              <Field :id="`toreroRow[${row}].nombre` + '_id'" type="text"
                                     :name="`toreroRow[${row}].nombre`"
                                     v-model="toreroStore.rows[row].nombre"
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
                                     v-model="toreroStore.rows[row].apellidos"
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
                                     v-model="toreroStore.rows[row].apodo"
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
                              <Field :id="`toreroRow[${row}].tipo_torero_id` + '_id'"
                                     :name="`toreroRow[${row}].tipo_torero_id`"
                                     v-model="toreroStore.rows[row].tipo_torero_id"
                                     as="select"
                                     class="form-control">
                                <option v-for="option in dataDeposit.tipoToreros" :key="option.id" :value="option.id">
                                  {{ option.tipo_torero }}
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
                      @click="addToreroRow(push, fields)"
                      class="btn btn-success">Añadir +
              </button>
              <button type="button" @click="removeToreroRow(remove, fields) "
                      class="btn btn-danger mx-2">
                Borrar -
              </button>
              <button @click="handleSubmit((values) => {onSubmit(values, push, remove, fields)})"
                      class="btn btn-secondary">Guardar
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
import {usedataDepositStore} from "@/stores/dataDepositStore";
import {useToreroStore, toreroRowFields} from "@/stores/toreroFormStore";


export default {
  name: 'ToreroForm',
  components: {
    Form,
    Field,
    FieldArray,
    ErrorMessage,
  },
  data() {
    const dataDeposit = usedataDepositStore()
    const toreroStore = useToreroStore()
    const schema = markRaw(y_object().shape({
      toreroRow: y_array()
          .of(
              y_object().shape({
                nombre: y_string().required(customErrorMessages.required_with_name("El nombre")).min(2, customErrorMessages.min_2),
                apellidos: y_string().required(customErrorMessages.required_with_name("Los apellidos")).min(2, customErrorMessages.min_2),
                apodo: y_string().matches(/.{2,}/, {
                  excludeEmptyString: true,
                  message: customErrorMessages.min_2,
                })
              })
          )
          .strict(),
    }));
    return {
      dataDeposit,
      toreroStore,
      schema,
    }
  },
  methods:
      {
        addToreroRow(funcPush, addedFields) {
          if (addedFields.length < CommonUtils.maxNumInstances) {
            funcPush({...toreroRowFields})
          }
        },
        removeToreroRow(funcRemove, addedFields) {
          if (addedFields.length > 1) {
            const fieldKey = addedFields[addedFields.length - 1].key
            funcRemove(fieldKey)
          }
        },
        resetForm(push, remove, fields) {
          for (let i = fields.length - 1; i >= 0; i--) {
            remove(fields[i])
          }
          this.toreroStore.resetToreroRowFields()
          push({...toreroRowFields})
        },
        async onSubmit(values, funcPush, funcRemove, rowFields) {
          console.log(JSON.stringify(values, null, 2));
          const {data} = await CommonUtils.sendDataToBackend(values, '/save_torero_details')
          if (data.status === 0) {
            await this.$vueAlert.alert(data.message, "Error en la operación", 'error')
          } else {
            await this.dataDeposit.fetchAndStoreToreros()
            this.resetForm(funcPush, funcRemove, rowFields)
            await this.$vueAlert.alert("Los nuevos toreros han sido guardados", "Operación satisfactoria", 'success')
          }
          console.log(JSON.stringify(data, null, 2));
        }
      }
}
</script>
