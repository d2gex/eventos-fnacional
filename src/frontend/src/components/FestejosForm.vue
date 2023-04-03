<template>
  <fieldset class="form-group border p-3">
    <legend class="w-auto px-2">Festejos</legend>
    <Form
        @submit="onSubmit"
        :initial-values="initialData"
        :validation-schema="schema"
    >
      <div class="row border border-primary">
        <div class="col-lg-6 float-left">
          <div class="card mt-2 mx-auto p-2 bg-light">
            <div class="card-body bg-light">
              <div class="container">
                <div class="controls">
                  <div class="row">
                    <div class="col-md-6">
                      <div class="form-group">
                        <label :for="'festejos.nombreFestejo'">Nombre *</label>
                        <Field id="nombreFestejo_id" type="text" :name="'festejos.nombreFestejo'"
                               class="form-control"
                               placeholder="Entra el nombre *"/>
                        <div class="field-error">
                          <ErrorMessage as="div" :name="'festejos.nombreFestejo'"/>
                        </div>

                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="form-group">
                        <label :for="'festejos.poblacion'">Población *</label>
                        <Field id="poblacion_id" type="text" :name="'festejos.poblacion'"
                               class="form-control"
                               placeholder="Entra la población *"/>
                        <div class="field-error">
                          <ErrorMessage as="div" :name="'festejos.poblacion'"/>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-md-6">
                      <div class="form-group">
                        <label :for="'festejos.provincia'">Provincia *</label>
                        <Field id="'provincia_id'" type="text" :name="'festejos.provincia'"
                               class="form-control"
                               placeholder="Entra la pronvicia *"/>
                        <div class="field-error">
                          <ErrorMessage as="div" :name="'festejos.provincia'"/>
                        </div>
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="form-group">
                        <label :for="'festejos.tipoFestejo'">Tipo de Festejo *</label>
                        <Field id="tipoFestejo_id" :name="'festejos.tipoFestejo'"
                               v-model="selected" as="select" class="form-control">
                          <option v-for="(tipo, tipo_index) in tipoFestejos" :key="tipo_index" :value="tipo">
                            {{ tipo }}
                          </option>
                        </Field>
                      </div>
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
      <div class="row ">
        <div class="col-lg-8 mx-auto my-3 border border-danger text-center">
          <button type="submit" class="btn btn-secondary">Guardar</button>
        </div>
      </div>
    </Form>
  </fieldset>
</template>

<script>
import {Field, Form, ErrorMessage} from 'vee-validate';
import {object as y_object, string as y_string} from "yup";
import {markRaw} from "vue";
import customErrorMessages from "@/assets/common";

export default {
  name: 'FestejosForm',
  components: {
    Form,
    Field,
    ErrorMessage,
  },
  data() {
    const tipoFestejos = ['Opcion 1', 'Opcion 2', 'Opcion 3']
    const selected = 'Opcion 1'

    const initialData = {
      festejos: {
        tipoFestejo: '',
        nombreFestejo: '',
        poblacion: '',
        provincia: ''
      }
      // toreros: [{toreroName: ''}],
      // premios: [{premio: ''}]
    }
    const schema = markRaw(y_object().shape({
      festejos: y_object().shape({
        nombreFestejo: y_string().required(customErrorMessages.required_with_name("El nombre")).min(2, customErrorMessages.min_2),
        poblacion: y_string().required(customErrorMessages.required_with_name("La poblacion")).min(2, customErrorMessages.min_2),
        provincia: y_string().required(customErrorMessages.required_with_name("Los provincia")).min(2, customErrorMessages.min_2)
      })
      // toreroRow: y_array()
      //     .of(
      //         y_object().shape({
      //           nombreFestejo: y_string().required(customErrorMessages.required_with_name("El nombre")).min(2, customErrorMessages.min_2),
      //           poblacion: y_string().required(customErrorMessages.required_with_name("Los poblacion")).min(2, customErrorMessages.min_2),
      //           provincia: y_string().required(customErrorMessages.required_with_name("Los provincia")).min(2, customErrorMessages.min_2)
      //         })
      //     )
      //     .strict(),
    }));
    const maxRows = 6;
    return {
      tipoFestejos,
      selected,
      initialData,
      schema,
      maxRows
    }
  },
  methods:
      {
        onSubmit(values) {
          console.log(JSON.stringify(values, null, 2));
        }
      }
}
</script>
