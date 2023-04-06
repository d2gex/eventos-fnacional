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
    <url v-show="isListOpen">
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
    name: {
      type: String,
      required: true
    },
    id: String,
    placeholder: String,
    type: {
      type: String,
      required: true
    },
    items: {
      type: Array,
      required: true
    }
  },
  components: {
    Field,
    ErrorMessage,
  },
  methods: {
    filterResults() {
      return (this.items.filter(item => item.indexOf(this.search) > -1))
    },
    onChange() {
      this.results = this.filterResults()
      this.isListOpen = true
    }
  },
  data() {
    return {
      search: '',
      results: [],
      isListOpen: false
    }
  }
}
</script>
