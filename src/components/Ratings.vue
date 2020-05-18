<template>
  <v-container fluid>
    <PreventUnload :when="true" />
    <v-layout justify-center>
      <v-flex v-if="waited" xs4>
        <v-card color="white" v-animate-css="'fadeInDown'">
          <v-img
            :src="current.img"
            class="center mt-2 mb-4"
            :width="w / 3"
            :height="h / 3"
            contain
          />
        </v-card>
        <p :class="medtext + ' mt-3'" v-animate-css="'fadeInDown'">
          #{{ currentID.replace(/\D/g, "") }} {{ current.name }}
        </p>
        <div v-animate-css="'fadeInUp'">
          <v-layout v-if="mode === 'like'" justify-center>
            <v-btn color="red" class="white--text" @click="next(3)"
              >DISLIKE</v-btn
            >
            <v-btn color="green" class="white--text" @click="next(7)"
              >LIKE</v-btn
            >
          </v-layout>
          <v-layout v-if="mode === 'spec'" justify-center>
            <v-btn color="red" class="white--text" @click="next(1)">HATE</v-btn>
            <v-btn color="purple" class="white--text" @click="next(3)"
              >DISLIKE</v-btn
            >
            <v-btn color="blue" class="white--text" @click="next(5)"
              >NEUTRAL</v-btn
            >
            <v-btn color="teal" class="white--text" @click="next(7)"
              >LIKE</v-btn
            >
            <v-btn color="green" class="white--text" @click="next(9)"
              >LOVE</v-btn
            >
          </v-layout>
          <v-layout v-if="mode === 'tens'" justify-center>
            <v-btn icon color="red" class="white--text" @click="next(1)"
              >1</v-btn
            >
            <v-btn icon color="pink" class="white--text" @click="next(2)"
              >2</v-btn
            >
            <v-btn icon color="purple" class="white--text" @click="next(3)"
              >3</v-btn
            >
            <v-btn icon color="deep-purple" class="white--text" @click="next(4)"
              >4</v-btn
            >
            <v-btn icon color="indigo" class="white--text" @click="next(5)"
              >5</v-btn
            >
            <v-btn icon color="blue" class="white--text" @click="next(6)"
              >6</v-btn
            >
            <v-btn icon color="cyan" class="white--text" @click="next(7)"
              >7</v-btn
            >
            <v-btn icon color="teal" class="white--text" @click="next(8)"
              >8</v-btn
            >
            <v-btn
              icon
              color="green darken-2"
              class="white--text"
              @click="next(9)"
              >9</v-btn
            >
            <v-btn icon color="green" class="white--text" @click="next(10)"
              >10</v-btn
            >
          </v-layout>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
/* eslint-disable */

import PreventUnload from "vue-prevent-unload";
export default {
  name: "Ratings",
  components: {
    PreventUnload
  },
  data() {
    return {
      // router parameters
      mode: this.$route.params.mode ? this.$route.params.mode : "tens",
      pokemon: this.$route.params.pokemon,
      // window info
      h: window.innerHeight,
      w: window.innerWidth,
      // variable for mount stalling
      waited: false,
      // current index
      i: 0
    };
  },
  computed: {
    // the pokedex number of the current pokemon
    currentID() {
      return this.pokemon[this.i].id;
    },
    // the current pokemon
    current() {
      return this.pokemon[this.i].data;
    },
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
    // assign the chosen rating to the current pokemon and move to the next one
    next(r) {
      // set the rating
      this.current.rating = r;
      // if not at the end
      if (this.i + 1 < this.pokemon.length) {
        // move forward to the next unrated mon
        this.findNext();
      } else {
        // otherwise, route to Pallet
        this.$router.push({
          name: "Pallet",
          params: {
            mode: this.mode,
            pokemon: this.pokemon
          }
        });
      }
    },
    wait() {
      this.waited = true;
    },
    findNext() {
      while (this.current.rating != 0 && this.i < this.pokemon.length - 1) {
        this.i++;
      }
      if (this.i == this.pokemon.length - 1 && this.current.rating != 0) {
        this.$router.push({
          name: "Pallet",
          params: {
            mode: this.mode,
            pokemon: this.pokemon
          }
        });
      }
    }
  },
  beforeMount() {
    window.setTimeout(() => {
      this.wait();
    }, 400);
  },
  mounted() {
    this.findNext();
  },
  beforeRouteLeave(to, from, next) {
    if (to.name !== "Pallet") {
      const answer = window.confirm(
        "If you leave this page, you will lose any unsaved progress. Are you sure you want to leave?"
      );
      if (answer) {
        next();
      } else {
        next(false);
      }
    } else {
      next();
    }
  }
};
</script>

<style scoped>
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.type-img {
  max-width: 150px;
  height: auto;
}
</style>
