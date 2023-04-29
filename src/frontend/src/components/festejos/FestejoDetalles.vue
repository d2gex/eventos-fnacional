<template>

  <div class="card mt-2 mx-auto p-2 bg-light">
    <div class="card-body bg-light">
      <div class="container">
        <div class="controls">
          <h3 class="text-center">Detalles del Festejo</h3>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">

                <label for="nombreFestejo">Nombre <span class="field_required">*</span></label>
                <InputForm type="text" :id="nombreFestejo + '_id'" :name='nombreFestejo'
                           placeholder="Entra el festejo *"/>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for="poblacion">Población <span class="field_required">*</span></label>
                <Field :id="poblacion + '_id'"
                       :name='poblacion'
                       v-model="selectBox.selectedPoblacion"
                       as="select"
                        class="form-select">
                  <option v-for="option in selectBox.poblaciones" :key="option.id" :value="option.id">
                    {{ option.ciudad }}
                  </option>
                </Field>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for="provincia">Provincia <span class="field_required">*</span></label>
                <Field :id="provincia + '_id'"
                       :name='provincia'
                       v-model="selectedProvincia"
                       as="select"
                       class="form-select">
                  <option v-for="option in dataDeposit.provincias" :key="option.id" :value="option.id">
                    {{ option.provincia }}
                  </option>
                </Field>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label :for="tipoFestejo">Tipo de Festejo <span class="field_required">*</span></label>
                <Field :id="tipoFestejo + '_id'"
                       :name="tipoFestejo"
                       v-model="selectBox.selectedFestejo"
                       as="select"
                        class="form-select">
                  <option v-for="option in selectBox.tipoFestejos" :key="option.id" :value="option.id">
                    {{ option.tipo_festejo }}
                  </option>
                </Field>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label :for="celebracion + '_id'">Fecha del Festejo <span class="field_required">*</span></label>
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
import {usedataDepositStore} from "@/stores/dataDepositStore";
import {CommonUtils} from "@/assets/common";

export default {
  name: "FestejoDetalles",
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
    tipoFestejos: {
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
  data() {
    const dataDeposit = usedataDepositStore()
    const dateFestejoValue = new Date().toLocaleDateString();
    const selectBox = {
      selectedFestejo: '',
      selectedPoblacion: '',
      poblaciones: [],
      tipoFestejos: []
    };
    const selectedProvincia = CommonUtils.selectedProvincia;
    return {
      dataDeposit,
      dateFestejoValue,
      selectBox,
      selectedProvincia
    }
  },
  methods: {
    updateSelectBox(newItems, dataProp, selectedProp) {
      this.selectBox[dataProp] = this[dataProp]
      this.selectBox[selectedProp] = this.selectBox[dataProp][this[selectedProp]].id
    }
  },
  watch: {
    tipoFestejos(newItem) {
      this.updateSelectBox(newItem, 'tipoFestejos', 'selectedFestejo')
    },
    poblaciones(newItem) {
      this.updateSelectBox(newItem, 'poblaciones', 'selectedPoblacion')
    },
  },
  mounted() {
    if (this.tipoFestejos.length) {
      this.updateSelectBox(this.tipoFestejos, 'tipoFestejos', 'selectedFestejo')
    }
    if (this.tipoFestejos.length) {
      this.updateSelectBox(this.tipoFestejos, 'poblaciones', 'selectedPoblacion')
    }
  }
}
</script>