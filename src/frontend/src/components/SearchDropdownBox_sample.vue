<template>
  <div class="card flex justify-content-center">
    <Dropdown v-model="value"
              :options="countries"
              filter
              optionLabel="name"
              placeholder="Select a Country"
              class="w-full md:w-14rem">
      <template #value="slotProps">
        <div v-if="slotProps.value" class="flex align-items-center">
          <div>{{ slotProps.value.name }}</div>
        </div>
        <span v-else>
                    {{ slotProps.placeholder }}
                </span>
      </template>
      <template #option="slotProps">
        <div class="flex align-items-center">
          <div>{{ slotProps.option.name }}</div>
        </div>
      </template>
    </Dropdown>
  </div>
  <small class="p-error" id="dd-error">{{ errorMessage || '&nbsp;' }}</small>
</template>

<script setup>
import {ref} from "vue";
import Dropdown from 'primevue/dropdown';
import {defineProps} from "vue";
import {useField} from "vee-validate";

const props = defineProps({
  fieldName: {
    type: String,
    required: true
  }
});

const { value, errorMessage } = useField(props.fieldName);
// const selectedCountry = ref();
const countries = ref([
  {name: 'Australia', code: 'AU'},
  {name: 'Brazil', code: 'BR'},
  {name: 'China', code: 'CN'},
  {name: 'Egypt', code: 'EG'},
  {name: 'France', code: 'FR'},
  {name: 'Germany', code: 'DE'},
  {name: 'India', code: 'IN'},
  {name: 'Japan', code: 'JP'},
  {name: 'Spain', code: 'ES'},
  {name: 'United States', code: 'US'}
]);
</script>