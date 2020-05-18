<template>
  <v-container fluid>
    <v-layout justify-center>
      <v-flex xs12 xl6>
        <p :class="bigtext">Welcome to PokePallet! (Alpha)</p>
        <ul :class="`${liltext} text-xs-left`">
          <li>
            You'll be presented with all {{ pokemon.length }} pokemon, one at a
            time, giving each one a rating from 1 to 10.
          </li>
          <li>
            Currently, Regional Variants are not supported :/ But they are
            coming soon!
          </li>
          <li>
            If you don't have time to rate them all at once, use the Save button
            at the top to save your progress, and the Load button to load it
            back up when you return.
          </li>
          <li>
            Once you have rated all of the pokemon, you'll be able to see a
            whole bunch of stats about your preference in pokemon! If you made
            any mistakes or change your mind on anything, you can change all of
            your ratings there.
          </li>
          <li>
            Don't forget to Save at the end! A completed PokePallet is useful
            for sharing and comparing with friends!
          </li>
        </ul>
        <v-card class="mt-4 pt-3" v-animate-css="'fadeInUp'">
          <p :class="medtext">Click the button when you're ready to begin.</p>
          <p class="text-xs-center`">
            <v-btn
              min-height="100%"
              large
              color="red darken-2"
              :class="`${liltext} white--text font-weight-bold`"
              @click="start()"
              >LET'S GO!
            </v-btn>
          </p>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
/* eslint-disable */

// loads the json file
let pokemonJSON = require("@/data/pokemon.json");
// turns the Object into an array of Objects
let pokemon = Object.keys(pokemonJSON).map(function(key) {
  return { id: key, data: pokemonJSON[key] };
});
// sorts the array by id number
pokemon.sort(function(x, y) {
  if (x.id < y.id) {
    return -1;
  }
  if (x.id > y.id) {
    return 1;
  }
  return 0;
});

export default {
  name: "Home",
  data() {
    return {
      // window info
      h: window.innerHeight,
      w: window.innerWidth,
      pokemon: pokemon
    };
  },
  computed: {
    // determine font size
    bigtext() {
      return this.h < 720
        ? "display-1"
        : this.h > 1080
        ? "display-3"
        : "display-2";
    },
    medtext() {
      return this.h < 720
        ? "headline"
        : this.h > 1080
        ? "display-2"
        : "display-1";
    },
    liltext() {
      return this.h < 720 ? "title" : this.h > 1080 ? "display-1" : "headline";
    }
  },
  methods: {
    // set the mode and begin rating
    start() {
      this.$router.push({
        name: "Ratings",
        params: {
          pokemon: pokemon
        }
      });
    }
  }
};
</script>

<style scoped></style>
