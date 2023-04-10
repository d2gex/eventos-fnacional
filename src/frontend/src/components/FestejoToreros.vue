<template>
  <fieldset class="form-group border p-3">
    <legend class="w-auto px-2">Toreros y Premios</legend>
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
                      <h3 class="text-center">Torero/Premio {{ row + 1 }}</h3>
                      <div class="row">
                        <div class="col-md-6">
                          <div class="form-group">
                            <label :for="`toreroName_${row}`">Torero *</label>
                            <SearchBox :items="items" type="text" :name="`toreroRow[${row}].toreroName`"/>
                          </div>
                        </div>
                        <div class="col-md-4">
                          <div class="form-group">
                            <label :for="`toreroRow[${row}].tipoPremio`">Tipo de Festejo *</label>
                            <Field :id="`tipoPremio_id_${row}`" :name="`toreroRow[${row}].tipoPremio`"
                                   v-model="tipoPremioSelected[row]" as="select" class="form-control">
                              <option v-for="(tipo, tipo_index) in tipoPremios" :key="tipo_index" :value="tipo">
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
import {FieldArray, Form, Field} from "vee-validate";
import SearchBox from "@/components/SearchBox.vue";
import {customErrorMessages} from "@/assets/common";
import {markRaw} from "vue";
import {array as y_array, object as y_object, string as y_string} from "yup";

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
    FieldArray,
    Field,
    Form
  },
  data() {
    const maxRows = 6;
    const tipoPremios = ['Oreja', 'Rabo', 'Ovación'];
    const tipoPremioSelected = Array(maxRows).fill(tipoPremios[0])
    const toreroRowFields = {
      toreroName: '',
    };
    const initialData = {
      toreroRow: [toreroRowFields]
    };

    const schema = markRaw(y_object().shape({
      toreroRow: y_array()
          .of(
              y_object().shape({
                toreroName: y_string().required(customErrorMessages.required_with_name("El nombre")).min(1, customErrorMessages.min_2),
              })
          )
          .strict(),
    }));
    return {
      maxRows,
      toreroRowFields,
      initialData,
      schema,
      tipoPremios,
      tipoPremioSelected
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
