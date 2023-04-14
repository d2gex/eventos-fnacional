<template>
  <Dropdown
      v-model="selectedItem"
      option-label="nombre_profesional"
      :options="dataItems"
      :virtualScrollerOptions="{ itemSize: optionItemSize }"
      filter
      class="form-control">
    <template #value="slotProps">
      <div v-if="slotProps.value" class="flex align-items-center">
        <div>{{ slotProps.value.nombre_profesional }}</div>
      </div>
      <span v-else>{{ slotProps.placeholder }}</span>
    </template>
    <template #option="slotProps">
      <div class="flex align-items-center">
        <div>{{ slotProps.option.nombre_profesional }}</div>
      </div>
    </template>
  </Dropdown>
</template>

<script>
import Dropdown from 'primevue/dropdown';

export default {
  name: "SearchDropdownBox",
  props: {
    items: {
      type: Array,
      required: true
    },
    selected: {
      type: Object,
      required: true
    },
    optionItemSize: {
      type: Number,
      required: true
    }
  },
  components: {
    Dropdown,
  },
  data() {
    const dataItems = []
    const selectedItem = '';
    return {
      dataItems,
      selectedItem
    }
  },
  mounted() {
    this.dataItems = this.items
    this.selectedItem = this.selected

  }
}
</script>