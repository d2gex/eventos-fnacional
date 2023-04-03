<template>
  <Field :id="id"
         :type="type"
         :name="name"
         :placeholder="placeholder"
         class="form-control"
  />
  <ErrorMessage as="div" class="field-error" :name="name"/>
</template>

<script>
import {Field, ErrorMessage} from 'vee-validate';

export default {
  name: 'InputForm',
  props: {
    'name': String,
    'id': String,
    'placeholder': String,
    'type': String
  },
  components: {
    Field,
    ErrorMessage,
  }
}
</script>
