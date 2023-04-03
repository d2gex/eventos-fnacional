<template>
  <div>
    <Form
        @submit="onSubmit"
        :validation-schema="schema"
    >
      <SearchInput name="email"/>
      <SearchInput name="password"/>
      <SearchInputField name="anothertext"/>
      <button type="submit" class="btn btn-secondary">Guardar</button>
    </Form>
  </div>
</template>
<script setup>
import {Form} from 'vee-validate';
import * as yup from 'yup';
import SearchInput from "@/components/SearchInput.vue";
import SearchInputField from "@/components/SearchInputField.vue";
// Define a validation schema
const schema = yup.object({
  email: yup.string().required().min(2),
  password: yup.string().required().min(2),
  anothertext: yup.string().required().min(2),
});

function onSubmit(values) {
  console.log(JSON.stringify(values, null, 2));
}
</script>