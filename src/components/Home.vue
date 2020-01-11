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
            The buttons at the top will be used to save/load your PokePallet so
            that you don't have to rate all the pokemon at once. This
            functionality is coming soon. As of now, you'll have to do it all
            without leaving the page.
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
          mode
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
</style>
