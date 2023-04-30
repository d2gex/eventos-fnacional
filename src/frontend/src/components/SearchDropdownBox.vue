<template>
  <Dropdown
      v-model="storeData.data"
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
    inputObject: {
      type: Object,
      required: true
    },
    items: {
      type: Array,
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
    const storeData = this.inputObject;

    return {
      dataItems,
      value,
      errorMessage,
      storeData
    }
  },
  methods: {
    updateItems(newItems) {
      this.dataItems = newItems
    }
  },
  watch: {
    items(newItems) {
      // Update an instance of this component when fetching the  api data for the first time
      this.updateItems(newItems)
    },
    'storeData.data': function (newData) {
      // Ensure useField's value is up to date with storeDAta.data to avoid validation problems
      this.value = newData
    },
    'inputObject.data': function (newData) {
      // Ensure that storeData.data is aware of external changes done on inputObject.data
      this.storeData.data = newData
    }
  },
  mounted() {
    // Update cloned copies of this component once the api data has been fetched.
    if (this.items.length) {
      this.updateItems(this.items)
    }
  }
}
</script>