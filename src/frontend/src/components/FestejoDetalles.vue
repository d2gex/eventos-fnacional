<template>

  <div class="card mt-2 mx-auto p-2 bg-light">
    <div class="card-body bg-light">
      <div class="container">
        <div class="controls">
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
                <InputForm type="text" :id="provincia + '_id'" :name='provincia'
                           placeholder="Entra la provincia *"/>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label :for="tipoFestejo">Tipo de Festejo *</label>
                <Field :id="tipoFestejo + '_id'" :name="tipoFestejo"
                       v-model="selected" as="select" class="form-control">
                  <option v-for="(tipo, tipo_index) in tiposFestejos" :key="tipo_index" :value="tipo">
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
</template>

<script>
import InputForm from "@/components/InputForm.vue";
import {Field} from "vee-validate";

export default {
  name: "FestejoDetalles",
  props: {
    nombreFestejo: String,
    poblacion: String,
    provincia: String,
    tipoFestejo: String,
    selectedFestejo: String,
    tiposFestejos: Array
  },
  components: {InputForm, Field},
  data() {
    return {
      selected: this.selectedFestejo // avoid making the prop accidentally writable
    }
  }
}
</script>