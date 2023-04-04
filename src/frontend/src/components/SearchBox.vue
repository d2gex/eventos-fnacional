<template>
  <div class="input-box">
    <Field :id="id"
           :type="type"
           :name="name"
           :placeholder="placeholder"
           v-model="search"
           @input="onChange"
           class="form-control"
    />
    <ErrorMessage as="div" class="field-error" :name="name"/>
  </div>
  <div class="mt-2">
    <url class="">
      <li class="d-flex flex-column ml-3 border-bottom" v-for="(item, index) in results" :key="index">
        <span>{{ item }}</span>
      </li>
    </url>
  </div>
</template>

<script>
import {Field, ErrorMessage} from 'vee-validate';

export default {
  name: 'SearchBox',
  props: {
    name: String,
    id: String,
    placeholder: String,
    type: String
  },
  components: {
    Field,
    ErrorMessage,
  },
  methods: {
    onChange() {
    }
  },
  data() {
    return {
      search: '',
      results: Array(5).fill("Jose Antonio Garcia Gonzalez 'El Litri'").map(v => v.toLowerCase())
    }
  }
}
</script>
