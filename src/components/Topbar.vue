<template>
  <div class="colored">
    <p class="title text-xs-left ml-2">
      <v-btn
        color="red"
        class="white--text font-weight-bold mode-btn"
        title="Home"
        @click="$router.push({ name: 'Home' })"
      >
        HOME
      </v-btn>
      <v-btn
        disabled
        color="green"
        class="white--text font-weight-bold mode-btn"
        title="Save your PokePallet"
      >
        SAVE
      </v-btn>
      <v-btn
        disabled
        color="blue"
        class="white--text font-weight-bold mode-btn"
        title="Load your PokePallet"
      >
        LOAD
      </v-btn>
    </p>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: "Topbar"
};
</script>

<style scoped>
.colored {
  background-color: #555555;
}
</style>
