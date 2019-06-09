<template>
  <v-container fluid>
    <v-layout justify-center>
      <v-flex xs12>
        <p class="display-1">New Page</p>
        <router-link v-bind:to="'/'">Home</router-link>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: 'NewPage'
}
</script>

<style scoped>
</style>
