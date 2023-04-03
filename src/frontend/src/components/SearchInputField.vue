<template>
  <Field id="nombreFestejo_id" type="text" :name="name"
         class="form-control"
         placeholder="Entra el nombre *"/>
  <div class="field-error">
    <ErrorMessage as="div" :name="name"/>
  </div>
</template>

<script>
import {Field, ErrorMessage} from 'vee-validate';

export default {
  name: 'SearchInput',
  props:{'name': String},
  components: {
    Field,
    ErrorMessage,
  },
  methods:
      {
        onSubmit(values) {
          console.log(JSON.stringify(values, null, 2));
        }
      }
}
</script>
