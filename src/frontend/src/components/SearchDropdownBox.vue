<template>
  <fieldset class="form-group border p-3">
    <legend class="w-auto px-2">Ganaderias</legend>

    <div class="row border border-primary">
      <div class="col-lg-12">
        <div class="card mt-2 mx-auto p-2 bg-light">
          <div class="card-body bg-light">
            <div class="container">
              <div class="controls">
                <h3 class="text-center">Test</h3>
                <div class="row">
                  <div class="col-md-12">
                    <div class="form-group">
                      <Dropdown v-model="selectedCountry"
                                :options="countries"
                                filter
                                optionLabel="name"
                                placeholder="Select a Country">
                        <template #value="slotProps">
                          <div v-if="slotProps.value" class="flex align-items-center">
                            <div>{{ slotProps.value.name }}</div>
                          </div>
                          <span v-else>{{ slotProps.placeholder }}</span>
                        </template>
                        <template #option="slotProps">
                          <div class="flex align-items-center">
                            <div>{{ slotProps.option.name }}</div>
                          </div>
                        </template>
                      </Dropdown>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- /.8 -->
      </div>
      <!-- /.row-->
    </div>


  </fieldset>
</template>

<script>
import Dropdown from 'primevue/dropdown';

export default {
  name: "SearchDropdownBox",
  components: {
    Dropdown
  },
  data() {
    const selectedCountry = '';
    const countries = [
      {name: 'Australia', code: 'AU'},
      {name: 'Brazil', code: 'BR'},
      {name: 'China', code: 'CN'},
      {name: 'Egypt', code: 'EG'},
      {name: 'France', code: 'FR'},
      {name: 'Germany', code: 'DE'},
      {name: 'India', code: 'IN'},
      {name: 'Japan', code: 'JP'},
      {name: 'Spain', code: 'ES'},
      {name: 'United States', code: 'US'}
    ];

    return {
      selectedCountry,
      countries
    }
  }
}

</script>