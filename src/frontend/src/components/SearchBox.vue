<template>
  <div class="input-box">
    <Field :id="id"
           :type="type"
           :name="name"
           :placeholder="placeholder"
           v-model="search"
           @input="onChange"
           @keydown.down="onArrowDown"
           @keydown.up="onArrowUp"
           @keydown.enter="onEnter"
           class="form-control"
    />
    <ErrorMessage as="div" class="field-error" :name="name"/>
  </div>
  <div class="mt-2">
    <ul class="list-group" v-show="isListOpen">
      <li :class="{ 'active': index === arrowCounter }" class="list-group-item" v-for="(item, index) in results"
          :key="index">
        <span @click="setResult(item)">{{ capitalizeWords(item) }}</span>
      </li>
    </ul>
  </div>
</template>

<script>
import {Field, ErrorMessage} from 'vee-validate';
import {CommonUtils} from "@/assets/common";

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
    ErrorMessage
  },
  methods: {
    filterResults() {
      return (this.items.filter(item => item.indexOf(this.search) > -1))
    },
    onChange() {
      this.results = this.filterResults()
      this.isListOpen = true
    },
    setResult(item) {
      this.search = item
      this.isListOpen = false
    },
    handleClickOutside(event) {
      if (!this.$el.contains(event.target)) {
        this.isListOpen = false;
      }
    },
    onArrowDown() {
      const last_el_offset = this.results.length - 1
      const first_el_offset = 0
      if (this.arrowCounter === last_el_offset) {
        this.arrowCounter = first_el_offset
      } else {
        this.arrowCounter = this.arrowCounter + 1;
      }
    },
    onArrowUp() {
      const last_el_offset = this.results.length - 1
      const first_el_offset = 0
      if (this.arrowCounter === first_el_offset) {
        this.arrowCounter = last_el_offset
      } else {
        this.arrowCounter = this.arrowCounter - 1;
      }
    },
    onEnter() {
      this.search = this.results[this.arrowCounter];
      this.arrowCounter = -1;
      this.isListOpen = false;
    },
    capitalizeWords (item) {
      return CommonUtils.capitalizeWords(item)
    }
  },
  data() {
    return {
      search: '',
      results: [],
      isListOpen: false,
      arrowCounter: -1
    }
  },
  mounted() {
    document.addEventListener('click', this.handleClickOutside);
  },
  unmounted() {
    document.removeEventListener('click', this.handleClickOutside);
  }
}
</script>
