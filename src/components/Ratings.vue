<template>
  <v-container fluid>
    <prevent-unload :when="true" />
    <v-layout justify-center>
      <v-flex v-if="waited" xs12 md8 lg4>
        <v-card color="white" v-animate-css="'fadeInDown'">
          <v-img
            :src="current.img"
            class="center mt-2 mb-4"
            :width="small ? w / 2 : w / 3.5"
            :height="h / 3.5"
            contain
          />
        </v-card>
        <p :class="medtext + ' mt-3'" v-animate-css="'fadeInDown'">
          #{{ currentID.replace(/\D/g, "") }} {{ current.name }}
        </p>
        <div v-animate-css="'fadeInUp'">
          <v-layout justify-center my-4>
            <v-btn large icon color="red" class="white--text" @click="next(1)"
              >1</v-btn
            >
            <v-btn large icon color="pink" class="white--text" @click="next(2)"
              >2</v-btn
            >
            <v-btn
              large
              icon
              color="purple"
              class="white--text"
              @click="next(3)"
              >3</v-btn
            >
            <v-btn
              large
              icon
              color="deep-purple"
              class="white--text"
              @click="next(4)"
              >4</v-btn
            >
            <v-btn
              large
              icon
              color="indigo"
              class="white--text"
              @click="next(5)"
              >5</v-btn
            >
            <span v-if="!small">
              <v-btn
                large
                icon
                color="blue"
                class="white--text"
                @click="next(6)"
                >6</v-btn
              >
              <v-btn
                large
                icon
                color="cyan"
                class="white--text"
                @click="next(7)"
                >7</v-btn
              >
              <v-btn
                large
                icon
                color="teal"
                class="white--text"
                @click="next(8)"
                >8</v-btn
              >
              <v-btn
                large
                icon
                color="green darken-2"
                class="white--text"
                @click="next(9)"
                >9</v-btn
              >
              <v-btn
                large
                icon
                color="green"
                class="white--text"
                @click="next(10)"
                >10</v-btn
              >
            </span>
          </v-layout>
          <v-layout v-if="small" justify-center my-4>
            <v-btn large icon color="blue" class="white--text" @click="next(6)"
              >6</v-btn
            >
            <v-btn large icon color="cyan" class="white--text" @click="next(7)"
              >7</v-btn
            >
            <v-btn large icon color="teal" class="white--text" @click="next(8)"
              >8</v-btn
            >
            <v-btn
              large
              icon
              color="green darken-2"
              class="white--text"
              @click="next(9)"
              >9</v-btn
            >
            <v-btn
              large
              icon
              color="green"
              class="white--text"
              @click="next(10)"
              >10</v-btn
            >
          </v-layout>
          <v-layout justify-center my-4>
            <v-btn
              color="amber"
              class="black--text font-weight-bold"
              @click="preview()"
              >PREVIEW YOUR POKEPALLET</v-btn
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
      // pokemon from the router
      pokemon: this.$route.params.pokemon,
      // window info
      h: window.innerHeight,
      w: window.innerWidth,
      // variable for mount stalling
      waited: false,
      // variable to help routing
      finished: false,
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
    },
    small() {
      return this.w < 700;
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
        this.finish();
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
        this.finish();
      }
    },
    finish() {
      this.finished = true;
      this.$router.push({
        name: "Pallet",
        params: {
          pokemon: this.pokemon,
          completed: true
        }
      });
    },
    preview() {
      this.$router.push({
        name: "Pallet",
        params: {
          pokemon: this.pokemon,
          completed: false
        }
      });
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
    if (to.name == "Pallet") {
      next();
    } else {
      const answer = window.confirm(
        "If you leave this page, you will lose any unsaved progress. Are you sure you want to leave?"
      );
      if (answer) {
        next();
      } else {
        next(false);
      }
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
</style>
