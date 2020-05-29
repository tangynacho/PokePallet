<template>
  <v-container fluid>
    <v-layout justify-center>
      <v-flex xs10 xl8>
        <p :class="bigtext">Welcome to PokePallet! (Beta)</p>
        <ul :class="`${liltext} text-xs-left`">
          <li>
            You'll be presented with all {{ pokemon.length }} pokemon, one at a
            time, giving each one a rating from 1 to 10. This number includes
            all Regional Variant forms.
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
            for sharing and comparing with friends, or updating whenever new
            Pokemon or other features are added!
          </li>
        </ul>
        <v-layout justify-center mt-4 pt-3>
          <v-flex xs12 md8>
            <v-card class="mt-4 py-4" v-animate-css="'fadeInUp'">
              <p :class="medtext">
                Click the button when you're ready to begin.
              </p>
              <v-btn
                round
                large
                color="red darken-2"
                :class="`${btntext} white--text font-weight-bold`"
                @click="start()"
                >LET'S GO!
              </v-btn>
            </v-card>
          </v-flex>
        </v-layout>
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
      return this.w < 700
        ? "title"
        : this.w < 1000
        ? "headline"
        : this.w < 1500
        ? "display-1"
        : this.w < 2000
        ? "display-2"
        : "display-3";
    },
    medtext() {
      return this.w < 700
        ? "subtitle-1"
        : this.w < 1000
        ? "title"
        : this.w < 1500
        ? "headline"
        : this.w < 2000
        ? "display-1"
        : "display-2";
    },
    liltext() {
      return this.w < 700
        ? "subtitle-2"
        : this.w < 1000
        ? "subtitle-1"
        : this.w < 1500
        ? "title"
        : this.w < 2000
        ? "headline"
        : "display-1";
    },
    btntext() {
      return this.w < 700
        ? this.bigtext
        : this.w < 2000
        ? this.liltext
        : "headline";
    }
  },
  methods: {
    // set the mode and begin rating
    start() {
      this.$router.push({
        name: "Loader",
        params: {
          pokemon: pokemon,
          destination: "Ratings"
        }
      });
    }
  }
};
</script>

<style scoped></style>
