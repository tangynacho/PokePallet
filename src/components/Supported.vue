<template>
  <v-container fluid>
    <v-layout justify-center>
      <v-flex xs12 xl6>
        <p :class="bigtext">Currently Supported Stats</p>
        <ul :class="`${medtext} text-xs-left`">
          <li>stat 1</li>
        </ul>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: 'Supported',
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
