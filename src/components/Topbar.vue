<template>
  <div class="colored">
    <p class="title text-xs-left ml-2">
      <v-btn icon title="Save your PokePallet">
        <v-icon color="white">mdi-floppy</v-icon>
      </v-btn>
      <v-btn icon title="Load your PokePallet">
        <v-icon color="white">mdi-upload</v-icon>
      </v-btn>
    </p>
  </div>
</template>

<script>
export default {
  name: 'Topbar'
}
</script>

<style scoped>
.colored {
  background-color: #555555;
}
</style>
