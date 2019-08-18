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
          <li>Then, you'll give that pokemon a rating and move on to the next one.</li>
          <li>
            Once you have rated all of the pokemon, you can see a whole bunch of
            stats about your preference in pokemon. Click
            <router-link v-bind:to="'/supported'">here</router-link>
            <span>for a list of currently supported stats.</span>
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
          <p :class="medtext">Here are some options to customize your experience:</p>
          <v-flex text-xs-left>
            <div class="my-2">
              <input class="my-box ml-3 mr-1" type="checkbox" v-model="megas" disabled />
              <label class="title">Include Mega Evolutions</label>
            </div>
            <div class="mb-3 ml-4" v-if="megas">
              <input class="my-box ml-3 mr-1" type="checkbox" v-model="megasGen6" disabled />
              <label class="title">Consider all Mega Evolutions as Generation 6 Pokemon</label>
            </div>
            <div class="my-2">
              <input class="my-box ml-3 mr-1" type="checkbox" v-model="alolans" disabled />
              <label class="title">Include Alolan Forms</label>
            </div>
            <div class="mb-3 ml-4" v-if="alolans">
              <input class="my-box ml-3 mr-1" type="checkbox" v-model="alolansGen7" disabled />
              <label class="title">Consider all Alolan Forms as Generation 7 Pokemon</label>
            </div>
            <div class="my-2">
              <input class="my-box ml-3 mr-1" type="checkbox" v-model="ultraLegends" disabled />
              <label class="title">Consider Ultra-Beasts as Legendaries</label>
            </div>
          </v-flex>
        </v-card>
        <v-card class="mt-4 pt-3" v-animate-css="'fadeInUp'">
          <p :class="medtext">To get started, choose a rating system below:</p>
          <p :class="`${liltext} text-xs-left`">
            <v-btn
              disabled
              color="red"
              class="white--text font-weight-bold mode-btn"
              @click="setmode('like')"
            >LIKE / DISLIKE</v-btn>Simply like or dislike each pokemon.
          </p>
          <p :class="`${liltext} text-xs-left`">
            <v-btn
              disabled
              color="green"
              class="white--text font-weight-bold mode-btn"
              @click="setmode('spec')"
            >SPECTRUM</v-btn>Choose a rating for each pokemon on a spectrum from love to hate.
          </p>
          <p :class="`${liltext} text-xs-left`">
            <v-btn
              color="blue"
              class="white--text font-weight-bold mode-btn"
              @click="setmode('tens')"
            >TEN-SCALE</v-btn>Rate each pokemon on a scale from 1 to 10.
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
      // window info
      h: window.innerHeight,
      w: window.innerWidth,
      // mode variable
      mode: undefined,
      // flags
      megas: false,
      megasGen6: false,
      alolans: false,
      alolansGen7: false,
      ultraLegends: false
    }
  },
  computed: {
    // determine font size
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
    // set the mode and begin rating
    setmode (mode) {
      this.$router.push({ name: 'Ratings', params: { mode, megas: this.megas, megasGen6: this.megasGen6, alolans: this.alolans, alolansGen7: this.alolansGen7, ultraLegends: this.ultraLegends } })
    }
  }
}
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
