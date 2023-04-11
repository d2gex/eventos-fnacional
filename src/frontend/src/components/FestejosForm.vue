<template>
  <fieldset class="form-group border p-3">
    <legend class="w-auto px-2">Festejos</legend>
    <Form
        @submit="onSubmit"
        :initial-values="initialData"
        :validation-schema="schema"
    >
      <div class="row border border-primary">
        <div class="col-md-6">
          <div class="row">
            <FestejoDetalles nombre-festejo="festejos.nombreFestejo"
                             poblacion="festejos.poblacion"
                             provincia="festejos.provincia"
                             tipo-festejo="festejos.tipoFestejo"
                             :selected-festejo="selected"
                             :tipos-festejos="tipoFestejos"/>
          </div>
          <div class="row">
            <FestejoGanaderias :items="ganaderiasData"/>
          </div>

        </div>
        <div class="col-md-6">
          <FestejoToreros :items="torerosData"/>
        </div>
      </div>
      <div class="row ">
        <div class="col-lg-8 mx-auto my-3 border border-danger text-center">
          <button type="submit" class="btn btn-secondary">Guardar</button>
        </div>
      </div>
    </Form>
  </fieldset>
</template>

<script>
import {Form} from 'vee-validate';
import {customErrorMessages} from "@/assets/common";
import FestejoDetalles from "@/components/FestejoDetalles.vue";
import FestejoToreros from "@/components/FestejoToreros.vue";
import FestejoGanaderias from "@/components/FestejoGanaderias.vue";
import {array as y_array, object as y_object, string as y_string} from "yup";
import {markRaw} from "vue";

export default {
  name: 'FestejosForm',
  components: {
    Form,
    FestejoDetalles,
    FestejoToreros,
    FestejoGanaderias
  },
  data() {
    const selected = 'Opcion 1'
    const tipoFestejos = ['Opcion 1', 'Opcion 2', 'Opcion 3']
    const initialData = {
      festejos: {
        tipoFestejo: '',
        nombreFestejo: '',
        poblacion: '',
        provincia: ''
      }
    }
    const torerosData = ["Jose Antonio", "Daniel Garcia", "David 'El Litri'", "Sonia Espartaca", "Laura Fogar 'La Cute'"].map(v => v.toLowerCase())
    const ganaderiasData = ["Ganaderia 1", "Ganaderia 2", "Ganaderia 3", "Ganaderia 4", "Ganaderia 5"].map(v => v.toLowerCase())
    const schema = markRaw(y_object().shape({
      festejos: y_object().shape({
        nombreFestejo: y_string().required(customErrorMessages.required_with_name("El nombre")).min(2, customErrorMessages.min_2),
        poblacion: y_string().required(customErrorMessages.required_with_name("La poblacion")).min(2, customErrorMessages.min_2),
        provincia: y_string().required(customErrorMessages.required_with_name("Los provincia")).min(2, customErrorMessages.min_2),
      }),
      toreroRow: y_array()
          .of(
              y_object().shape({
                toreroName: y_string().required(customErrorMessages.required_with_name("El nombre")).min(1, customErrorMessages.min_2),
              })
          )
          .strict(),
      ganaderiaRow: y_array()
          .of(
              y_object().shape({
                ganaderiaName: y_string().required(customErrorMessages.required_with_name("El nombre")).min(1, customErrorMessages.min_2),
              })
          )
          .strict(),
    }));
    return {
      selected,
      tipoFestejos,
      initialData,
      schema,
      torerosData,
      ganaderiasData
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
