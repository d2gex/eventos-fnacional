<template>

  <div class="card mt-2 mx-auto p-2 bg-light">
    <div class="card-body bg-light">
      <div class="container">
        <div class="controls">
          <h3 class="text-center">Detalles del Festejo</h3>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">

                <label for="nombreFestejo">Nombre *</label>
                <InputForm type="text" :id="nombreFestejo + '_id'" :name='nombreFestejo'
                           placeholder="Entra el festejo *"/>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for="poblacion">Población *</label>
                <InputForm type="text" :id="poblacion + '_id'" :name='poblacion'
                           placeholder="Entra la población *"/>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for="provincia">Provincia *</label>
                <Field :id="provincia + '_id'" :name='provincia'
                       v-model="selectedProvinciaId" as="select" class="form-control">
                  <option v-for="option in provincias" :key="option.id" :value="option.id">
                    {{ option.provincia }}
                  </option>
                </Field>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label :for="tipoFestejo">Tipo de Festejo *</label>
                <Field :id="tipoFestejo + '_id'" :name="tipoFestejo"
                       v-model="selectedFestejoId" as="select" class="form-control">
                  <option v-for="option in tipoFestejos" :key="option.id" :value="option.id">
                    {{ option.tipo_festejo }}
                  </option>
                </Field>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label :for="celebracion + '_id'">Fecha del Festejo *</label>
                <VueDatePicker
                    :id="celebracion + '_id'"
                    model-type="dd/MM/yyyy"
                    v-model="dateFestejoValue"
                    format="dd/MM/yyyy"
                    :year-range="[1600, 2100]"
                    :enable-time-picker="false"></VueDatePicker>
                <ErrorMessage as="div" class="field-error" :name="celebracion"/>
                <Field :name="celebracion" type="hidden" v-model="dateFestejoValue">
                </Field>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import InputForm from "@/components/InputForm.vue";
import {Field, ErrorMessage} from "vee-validate";
import VueDatePicker from '@vuepic/vue-datepicker';
import {date} from "yup";

export default {
  name: "FestejoDetalles",
  methods: {date},
  components: {InputForm, Field, ErrorMessage, VueDatePicker},
  props: {
    nombreFestejo: String,
    poblacion: String,
    provincia: String,
    tipoFestejo: String,
    celebracion: String,
    selectedFestejo: {
      type: Number,
      required: true
    },
    selectedProvincia: {
      type: Number,
      required: true
    },
    tipoFestejos: {
      type: Array,
      required: true
    },
    provincias: {
      type: Array,
      required: true
    }
  },
  data() {
    const dateFestejoValue = new Date().toLocaleDateString();
    return {
      selectedFestejoId: this.selectedFestejo, // avoid making the prop accidentally writable
      selectedProvinciaId: this.selectedProvincia,
      dateFestejoValue
    }
  }
}
</script>