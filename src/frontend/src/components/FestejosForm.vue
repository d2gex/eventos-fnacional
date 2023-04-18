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
                             celebracion="festejos.celebracion"
                             :selected-festejo="selectedFestejo"
                             :tipo-festejos="tipoFestejos"
                             :selected-provincia="selectedProvincia"
                             :provincias="provincias"
            />
          </div>
          <div class="row">
            <FestejoGanaderias :items="ganaderiasData" :selected="selectedGanaderias"/>
          </div>

        </div>
        <div class="col-md-6">
          <FestejoToreros :torerosData="torerosData"
                          :selected-torero="selectedToreros"
                          :torero-premios-data="toreroPremiosData"
                          :selected-torero-premio="selectedToreroPremio"/>
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
  props: {
    selectedProvincia: {
      type: Number,
      required: true
    },
    provincias: {
      type: Array,
      require: true
    },
    selectedFestejo: {
      type: Number,
      required: true
    },
    tipoFestejos: {
      type: Array,
      require: true
    },
    selectedToreros: {
      type: Number,
      required: true
    },
    torerosData: {
      type: Array,
      required: true
    },
    selectedGanaderias: {
      type: Number,
      required: true
    },
    ganaderiasData: {
      type: Array,
      required: true
    },
    selectedToreroPremio: {
      type: Number,
      required: true
    },
    toreroPremiosData: {
      type: Array,
      required: true
    }
  },
  components: {
    Form,
    FestejoDetalles,
    FestejoToreros,
    FestejoGanaderias
  },
  data() {
    const initialData = {
      festejos: {
        tipoFestejo: '',
        nombreFestejo: '',
        poblacion: '',
        provincia: '',
        celebracion: '',
      }
    };

    const schema = markRaw(y_object().shape({
      festejos: y_object().shape({
        nombreFestejo: y_string().required(customErrorMessages.required_with_name("El nombre")).min(2, customErrorMessages.min_2),
        poblacion: y_string().required(customErrorMessages.required_with_name("La poblacion")).min(2, customErrorMessages.min_2),
        provincia: y_string().required(customErrorMessages.required_with_name("Los provincia")).min(2, customErrorMessages.min_2),
        celebracion: y_string().required(customErrorMessages.required_with_name("La fecha del festejo")).min(2, customErrorMessages.min_2),
      }),
      toreroRow: y_array()
          .of(
              y_object().shape({
                toreroName: y_object().required(customErrorMessages.required_with_name("El nombre")),
              })
          )
          .strict(),
      ganaderiaRow: y_array()
          .of(
              y_object().shape({
                ganaderiaName: y_object().required(customErrorMessages.required_with_name("El nombre"))
              })
          )
          .strict(),
    }));
    return {
      initialData,
      schema
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
