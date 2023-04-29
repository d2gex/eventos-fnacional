<template>
  <Dropdown
      v-model="value"
      :options="dataItems"
      :placeholder="placeHolder"
      :option-label="optionLabel"
      filter
      show-clear
      class="form-control">
    <template #value="slotProps">
      <div v-if="slotProps.value" class="flex align-items-center">
        <div>{{ slotProps.value[optionLabel] }}</div>
      </div>
      <span v-else>
        {{ slotProps.placeholder }}
      </span>
    </template>
    <template #option="slotProps">
      <div class="flex align-items-center">
        <div>{{ slotProps.option[optionLabel] }}</div>
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
    inputValue: {
      type: Object,
      required: true
    },
    placeHolder: {
      type: String,
      required: true
    },
    optionLabel: {
      type: String,
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
  methods: {
    updateItems(newItems) {
      this.dataItems = newItems
      this.value = this.inputValue
    }
  },
  watch: {
    items(newItems) {
      // Update an instance of this component when fetching the  api data for the first time
      this.updateItems(newItems)
    },
  },
  mounted() {
    // Update cloned copies of this component once the api data has been fetched.
    if (this.items.length) {
      this.updateItems(this.items)
    }
  }
}
</script>