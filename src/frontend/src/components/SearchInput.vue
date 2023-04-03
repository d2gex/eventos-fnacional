<template>
  <div>
    <input v-model="value" type="text" :name="name"/>
    <span>{{ errorMessage }}</span>
  </div>
</template>
<script setup>
import { defineProps } from 'vue';
import { useField } from 'vee-validate';

const props = defineProps({
  name: {
    type: String,
    required: true,
  },
});
// make sure to wrap the name in a function to maintain its reactivity
// this way vee-validate can react to the field name changing
const { errorMessage, value } = useField(() => props.name, undefined, {validateOnValueUpdate: false});
</script>