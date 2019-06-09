<template>
  <v-container fluid>
    <v-layout justify-center>
      <v-flex xs12 xl6>
        <p :class="bigtext">Welcome to PokePallet!</p>
        <ul :class="`${liltext} text-xs-left`">
          <li>
            You'll be presented with each and every pokemon in existence, one at
            a time.
          </li>
          <li>
            Then, you'll give that pokemon a rating and move on to the next one.
          </li>
          <li>
            Once you have rated all of the pokemon, you can see a whole bunch of
            stats about your preference in pokemon. Things like which generation
            you like the best, your favorite types, your preferred egg group,
            and much more!
          </li>
          <li>
            If you don't have time to rate every pokemon in one sitting, you can
            save your progress and finish later.
          </li>
          <li>
            At the end, you'll be able to download your very own PokePallet with
            all your stats to share and compare with friends!
          </li>
        </ul>
        <v-card class="mt-4 pt-3" v-animate-css="'fadeInUp'">
          <p :class="medtext">To get started, choose a rating system below:</p>
          <p :class="`${liltext} text-xs-left`">
            <v-btn
              color="red"
              class="white--text font-weight-bold mode-btn"
              @click="setmode('lik')"
              >LIKE / DISLIKE</v-btn
            >Simply like or dislike each pokemon.
          </p>
          <p :class="`${liltext} text-xs-left`">
            <v-btn
              color="green"
              class="white--text font-weight-bold mode-btn"
              @click="setmode('ind')"
              >INDIFFERECE</v-btn
            >Allow indifference and semi-like ratings.
          </p>
          <p :class="`${liltext} text-xs-left`">
            <v-btn
              color="blue"
              class="white--text font-weight-bold mode-btn"
              @click="setmode('ten')"
              >TEN-SCALE</v-btn
            >Rate each pokemon on a scale from 1 to 10.
          </p>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>

export default {
  name: 'Home',
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
  },
  methods: {
    setmode (mode) {
      this.$router.push({name: 'Ratings', params: { mode: mode }})
    }
  }
}
</script>

<style scoped>
.mode-btn {
  width: 120px;
}
</style>
