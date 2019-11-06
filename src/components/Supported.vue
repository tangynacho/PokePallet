<template>
  <v-container fluid>
    <v-layout justify-center>
      <v-flex xs12 xl6>
        <p :class="bigtext">Currently, this app can be used to rank your favorite:</p>
        <ul :class="`${medtext} text-xs-left`">
          <li>Pokemon</li>
          <li>Type of Pokemon</li>
          <li>Generation of Pokemon</li>
          <li>Color of Pokemon</li>
          <li>2-Stage Line</li>
          <li>3-Stage Line</li>
          <li>Pseudo Legendary Line</li>
          <li>Starter Line</li>
          <li>Generation by Starter Line</li>
          <li>Regional Bird Line</li>
          <li>Regional Rodent Line</li>
          <li>Regional Bug Line</li>
          <li>Regional Set (Starters, Birds, Rodents and Bugs)</li>
          <li>X Types, where X is any existing Pokemon Type</li>
          <li>Pokemon from Generation X, where X is an existing Generation of Pokemon</li>
          <li>X Colored Pokemon, where X is an existing official Pokedex Color</li>
          <li>Single Form Pokemon</li>
          <li>First Form Starter Pokemon</li>
          <li>Middle Form Starter Pokemon</li>
          <li>Final Form Starter Pokemon</li>
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
