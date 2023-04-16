<template>
  <Dropdown
      v-model="value"
      :options="dataItems"
      option-label="nombre_profesional"
      filter
      show-clear
      placeholder="Selecciona un torero"
      class="form-control">
    <template #value="slotProps">
      <div v-if="slotProps.value" class="flex align-items-center">
        <div>{{ slotProps.value.nombre_profesional }}</div>
      </div>
      <span v-else>
        {{ slotProps.placeholder }}
      </span>
    </template>
    <template #option="slotProps">
      <div class="flex align-items-center">
        <div>{{ slotProps.option.nombre_profesional }}</div>
      </div>
    </template>
  </Dropdown>
  <small class="p-error" id="dd-error">{{ errorMessage || '&nbsp;' }}</small>
</template>

<script>
import Dropdown from 'primevue/dropdown';
import {useField} from 'vee-validate';

export default {
  name: "SearchDropdownBox",
  props: {
    fieldName: {
      type: String,
      required: true
    },
    items: {
      type: Array,
      required: true
    },
    selected: {
      type: Object,
      required: true
    }
  },
  components: {
    Dropdown
  },
  data() {
    const dataItems = []
    const {value, errorMessage} = useField(this.fieldName);
    return {
      dataItems,
      value,
      errorMessage
    }
  },
  mounted() {
    this.dataItems = this.items
    this.value = this.selected
  }
}
</script>