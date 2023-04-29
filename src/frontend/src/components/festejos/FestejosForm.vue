<template>
  <Form
      @submit="onSubmit"
      :initial-values="initialData"
      :validation-schema="schema"
  >
    <div class="row ">
      <div class="col-md-6">
        <div class="row">
          <FestejoDetalles nombre-festejo="festejos.nombre_festejo"
                           celebracion="festejos.fecha"
                           poblacion="festejos.poblacion_id"
                           provincia="festejos.provincia_id"
                           tipo-festejo="festejos.tipo_festejo_id"
                           :selected-festejo="selectedFestejo"
                           :tipo-festejos="tipoFestejos"
                           :selected-poblacion="selectedPoblacion"
                           :poblaciones="poblaciones"
          />
        </div>
        <div class="row">
          <FestejoGanaderias :items="dataDeposit.ganaderiaItems" :selected="selectedGanaderia"/>
        </div>

      </div>
      <div class="col-md-6">
        <FestejoToreros :torerosData="dataDeposit.toreroItems"
                        :selected-torero="selectedTipoTorero"
                        :torero-premios-data="toreroPremiosData"
                        :selected-torero-premio="selectedToreroPremio"/>
      </div>
    </div>
    <div class="row ">
      <div class="col-lg-8 mx-auto my-3  text-center">
        <button type="submit" class="btn btn-primary">Guardar Festejo</button>
      </div>
    </div>
  </Form>
</template>

<script>
import {Form} from 'vee-validate';
import {CommonUtils, customErrorMessages} from "@/assets/common";
import FestejoDetalles from "@/components/festejos/FestejoDetalles.vue";
import FestejoToreros from "@/components/festejos/FestejoToreros.vue";
import FestejoGanaderias from "@/components/festejos/FestejoGanaderias.vue";
import {array as y_array, object as y_object, string as y_string} from "yup";
import {markRaw} from "vue";
import {usedataDepositStore} from "@/stores/dataDepositStore";

export default {
  name: 'FestejosForm',
  props: {
    selectedFestejo: {
      type: Number,
      required: true
    },
    tipoFestejos: {
      type: Array,
      require: true
    },
    selectedToreroPremio: {
      type: Number,
      required: true
    },
    toreroPremiosData: {
      type: Array,
      required: true
    },
    selectedPoblacion: {
      type: Number,
      required: true
    },
    poblaciones: {
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
    const dataDeposit = usedataDepositStore()
    const selectedGanaderia = CommonUtils.selectedGanaderia
    const selectedTipoTorero = CommonUtils.selectedTipoTorero
    const initialData = {
      festejos: {
        nombre_festejo: '',
        fecha: '',
        poblacion_id: '',
        provincia_id: '',
        tipo_festejo_id: '',
      }
    };

    const schema = markRaw(y_object().shape({
      festejos: y_object().shape({
        nombre_festejo: y_string().required(customErrorMessages.required_with_name("El nombre")).min(2, customErrorMessages.min_2),
        fecha: y_string().required(customErrorMessages.required_with_name("La fecha del festejo")).min(2, customErrorMessages.min_2),
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
      dataDeposit,
      selectedGanaderia,
      selectedTipoTorero,
      initialData,
      schema
    }
  },
  methods:
      {
        async onSubmit(values) {
          console.log(JSON.stringify(values, null, 2));
          const {data} = await CommonUtils.sendDataToBackend(values, '/save_festejos')
          if (data.status === 0) {
            await this.$vueAlert.alert(data.message)
          }
          console.log(JSON.stringify(data, null, 2));
        }
      }
}
</script>
