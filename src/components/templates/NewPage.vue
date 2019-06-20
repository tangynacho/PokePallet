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
  name: 'NewPage',
  data () {
    return {
      h: window.innerHeight,
      w: window.innerWidth
    }
  },
  computed: {
    bigtext () {
      return this.h < 720
        ? 'display-1'
        : this.h > 1080
          ? 'display-3'
          : 'display-2'
    },
    medtext () {
      return this.h < 720
        ? 'headline'
        : this.h > 1080
          ? 'display-2'
          : 'display-1'
    },
    liltext () {
      return this.h < 720 ? 'title' : this.h > 1080 ? 'display-1' : 'headline'
    }
  }
}
</script>

<style scoped>
</style>
