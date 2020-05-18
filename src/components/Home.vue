<template>
  <v-container fluid>
    <v-layout justify-center>
      <v-flex xs12 xl6>
        <p :class="bigtext">Welcome to PokePallet! (Alpha)</p>
        <ul :class="`${liltext} text-xs-left`">
          <li>
            You'll be presented with all 890 pokemon, one at a time, giving each
            one a rating.
          </li>
          <li>
            Once you have rated all of the pokemon, you can see a whole bunch of
            stats about your preference in pokemon.
          </li>
          <li>
            At the end, you'll be able to download your very own PokePallet with
            all your stats to share and compare with friends!
          </li>
          <li>
            Currently, Megas and Regional Variants are not supported :/ But they
            are coming soon!
          </li>
          <li>
            The buttons at the top can be used to save/load your PokePallet so
            that you don't have to rate all the pokemon at once. Loading might
            only work from the Home page, but it should bring you right to the
            next pokemon you need to rate. If it doesn't work, try refreshing
            the page.
          </li>
        </ul>
        <v-card class="mt-4 pt-3" v-animate-css="'fadeInUp'">
          <p :class="medtext">To get started, choose a rating system below:</p>
          <p :class="`${liltext} text-xs-left`">
            <v-btn
              color="red"
              class="white--text font-weight-bold mode-btn"
              @click="setmode('tens')"
              >TEN-SCALE</v-btn
            >Rate each pokemon on a scale from 1 to 10.
          </p>
          <p :class="`${liltext} text-xs-left`">
            <v-btn
              disabled
              color="green"
              class="white--text font-weight-bold mode-btn"
              @click="setmode('like')"
              >LIKE / DISLIKE</v-btn
            >Coming Soon
          </p>
          <p :class="`${liltext} text-xs-left`">
            <v-btn
              disabled
              color="blue"
              class="white--text font-weight-bold mode-btn"
              @click="setmode('spec')"
              >SPECTRUM</v-btn
            >Coming Soon
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
      // mode variable
      mode: undefined
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
    setmode(mode) {
      this.$router.push({
        name: "Ratings",
        params: {
          mode,
          pokemon: pokemon
        }
      });
    }
  }
};
</script>

<style scoped>
.mode-btn {
  width: 120px;
}
.my-box {
  height: 16px;
  width: 16px;
}
.colored {
  background-color: #555555;
}
.inputfile {
  opacity: 0;
  overflow: hidden;
  position: absolute;
  z-index: -1;
}

.inputfile + label {
  cursor: pointer;
  font-weight: bold;
  padding-left: 20px;
  padding-right: 30px;
}
</style>
