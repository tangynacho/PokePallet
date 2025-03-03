<template>
  <v-container fluid>
    <prevent-unload :when="true" />
    <p v-if="completed" :class="`${bigtext} font-weight-bold`">
      Welcome to your PokéPallet!
    </p>
    <p v-else :class="`${liltext} font-weight-bold`">
      You are viewing an incomplete PokéPallet.
    </p>
    <v-btn
      v-if="!completed"
      color="amber"
      class="black--text font-weight-bold mb-4"
      @click="back_to_ratings()"
      >BACK TO RATINGS</v-btn
    >
    <p v-if="!small" :class="liltext">
      Use the buttons to see all sorts of different rankings! <br />Click on a
      Pokemon to edit its rating. Click on a group to expand it.
    </p>
    <p v-else-if="!changing" :class="`${liltext} mb-4`">
      Press Change Limits to configure your rankings! <br />
      <br />
      Tap on a Pokemon to change its rating.<br />
      Tap a group to expand it.
    </p>
    <p v-else :class="`${liltext} mb-4`">
      Use the buttons to configure, then press Save Limits to see the rankings!
      <br />
      <br />
      (Aggregated Rankings will clear all other limits)
    </p>
    <v-btn
      v-if="!changing && small"
      small
      color="amber"
      class="font-weight-bold"
      @click="changing = true"
      >CHANGE LIMITS</v-btn
    >
    <v-btn
      v-if="changing"
      small
      color="amber"
      class="font-weight-bold"
      @click="changing = false"
      >SAVE LIMITS</v-btn
    >
    <v-btn
      v-if="changing"
      small
      color="amber"
      class="font-weight-bold"
      @click="reset_limits()"
      >RESET LIMITS</v-btn
    >
    <v-layout justify-center :column="small">
      <v-flex v-show="changing || !small" xs12 md3 :mr-4="!small" :mt-4="small">
        <div>
          <p :class="`${medtext} my-2`">Limit Types</p>
          <v-layout justify-center>
            <v-btn
              :small="small"
              dark
              :color="
                type_limits['all'] && sortBy !== 'types' ? 'red darken-3' : ''
              "
              class="font-weight-bold"
              @click="toggle('type', 'all')"
              >SHOW ALL TYPES</v-btn
            >
            <v-btn
              :small="small"
              dark
              :color="this.sortBy == 'types' ? 'blue darken-2' : ''"
              class="font-weight-bold"
              @click="toggleSort('types')"
              >AGGREGATE TYPES</v-btn
            >
          </v-layout>
          <span v-for="t in Object.keys(type_limits)" :key="t">
            <v-btn
              :small="small"
              :disabled="sortBy == 'types'"
              v-if="t !== 'all'"
              dark
              :color="type_limits[t] ? 'red darken-3' : ''"
              @click="toggle('type', t)"
              >{{ t }} TYPES</v-btn
            >
          </span>
        </div>
        <div class="my-4">
          <p :class="`${medtext} my-2`">Limit Gens</p>
          <v-layout justify-center>
            <v-btn
              :small="small"
              dark
              :color="
                gen_limits['all'] && sortBy !== 'gens' ? 'red darken-3' : ''
              "
              class="font-weight-bold"
              @click="toggle('gen', 'all')"
              >SHOW ALL GENS</v-btn
            >
            <v-btn
              :small="small"
              dark
              :color="this.sortBy == 'gens' ? 'blue darken-1' : ''"
              class="font-weight-bold"
              @click="toggleSort('gens')"
              >AGGREGATE GENS</v-btn
            >
          </v-layout>
          <span v-for="g in Object.keys(gen_limits)" :key="g">
            <v-btn
              :small="small"
              :disabled="sortBy == 'gens'"
              v-if="g !== 'all'"
              dark
              :color="gen_limits[g] ? 'red darken-3' : ''"
              @click="toggle('gen', g)"
              >GEN {{ g }}</v-btn
            >
          </span>
        </div>
        <div class="mt-4">
          <p :class="`${medtext} my-2`">Limit Stages</p>
          <v-layout justify-center>
            <v-btn
              :small="small"
              dark
              :color="
                stage_limits['all'] && sortBy !== 'stages' ? 'red darken-3' : ''
              "
              class="font-weight-bold"
              @click="toggle('stage', 'all')"
              >SHOW ALL STAGES</v-btn
            >
            <v-btn
              :small="small"
              dark
              :color="this.sortBy == 'stages' ? 'blue darken-1' : ''"
              class="font-weight-bold"
              @click="toggleSort('stages')"
              >AGGREGATE STAGES</v-btn
            >
          </v-layout>
          <span v-for="s in Object.keys(stage_limits)" :key="s">
            <v-btn
              :small="small"
              :disabled="sortBy == 'stages'"
              v-if="s !== 'all'"
              dark
              :color="stage_limits[s] ? 'red darken-3' : ''"
              @click="toggle('stage', s)"
              >{{ s }}</v-btn
            >
          </span>
        </div>
      </v-flex>
      <v-flex v-show="!changing" xs12 lg6>
        <v-layout justify-center mt-4>
          <v-flex xs12 v-if="idToChange === 'None'">
            <v-btn
              v-if="!changing && !small"
              color="amber"
              class="font-weight-bold"
              @click="reset_limits()"
              >SHOW ALL POKEMON</v-btn
            >
            <v-layout>
              <p
                v-if="any_allowed"
                class="subtitle-1 text-xs-left mb-2 ml-2 bot"
              >
                Showing {{ show_range[0] + 1 }} - {{ last_shown + 1 }} of
                {{ sorted_allowed.length }}
              </p>
              <v-flex text-xs-right>
                <v-btn
                  :disabled="show_range[0] === 0"
                  :round="!small"
                  :icon="small"
                  color="grey darken-3"
                  class="white--text"
                  @click="changeRange(false)"
                  >{{ prevtext }}</v-btn
                >
                <v-btn
                  :disabled="last_shown + 1 === sorted_allowed.length"
                  :round="!small"
                  :icon="small"
                  color="grey darken-3"
                  class="white--text"
                  @click="changeRange(true)"
                  >{{ nexttext }}</v-btn
                >
              </v-flex>
            </v-layout>
            <v-card color="grey darken-3">
              <span v-if="!any_allowed">
                <v-card-text :class="`${liltext} text-xs-center`"
                  >No results.</v-card-text
                >
              </span>
              <span
                v-for="x in sorted_allowed_shown"
                :key="sorted_allowed_shown.indexOf(x)"
                :class="`${liltext} my-0 py-0 text-xs-left`"
              >
                <v-card
                  v-if="sortBy === 'ratings'"
                  class="mx-0 my-1 px-0 py-0"
                  @click="idToChange = x.id"
                >
                  <v-layout>
                    <v-flex xs3 class="center" align="center">{{
                      x.data.name
                    }}</v-flex>
                    <v-flex xs7>
                      <v-progress-linear
                        height="20"
                        :color="typeColors[x.data.types[0]]"
                        :value="x.data.rating * 10"
                      />
                    </v-flex>
                    <v-flex xs2 class="center" align="center">{{
                      x.data.rating
                    }}</v-flex>
                  </v-layout>
                </v-card>
                <v-card
                  v-else-if="lineSorts.includes(sortBy)"
                  class="mx-0 my-1 px-0 py-0"
                  @click="changeSort('ratings', 'line', x.key)"
                >
                  <span v-for="mon in pokemon" :key="mon.id">
                    <v-layout v-if="mon.id === x.key">
                      <v-flex xs3 class="center" align="center">{{
                        mon.data.name
                      }}</v-flex>
                      <v-flex xs7>
                        <v-progress-linear
                          :color="typeColors[mon.data.types[0]]"
                          height="20"
                          :value="x.avg * 10"
                        />
                      </v-flex>
                      <v-flex xs2 class="center" align="center">{{
                        x.avg
                      }}</v-flex>
                    </v-layout>
                  </span>
                </v-card>
                <v-card
                  v-else-if="genSorts.includes(sortBy)"
                  class="mx-0 my-1 px-0 py-0"
                  @click="changeSort('ratings', 'gen', x.key)"
                >
                  <v-layout>
                    <v-flex xs3 class="center" align="center"
                      >Gen {{ x.key }}</v-flex
                    >
                    <v-flex xs7>
                      <v-progress-linear
                        :color="genColors[parseInt(x.key) - 1]"
                        height="20"
                        :value="x.avg * 10"
                      />
                    </v-flex>
                    <v-flex xs2 class="center" align="center">{{
                      x.avg
                    }}</v-flex>
                  </v-layout>
                </v-card>
                <v-card
                  v-else-if="typeSorts.includes(sortBy)"
                  class="mx-0 my-1 px-0 py-0"
                  @click="changeSort('ratings', 'type', x.key)"
                >
                  <v-layout>
                    <v-flex xs3 class="center" align="center">{{
                      x.key
                    }}</v-flex>
                    <v-flex xs7>
                      <v-progress-linear
                        :color="typeColors[x.key]"
                        height="20"
                        :value="x.avg * 10"
                      />
                    </v-flex>
                    <v-flex xs2 class="center" align="center">{{
                      x.avg
                    }}</v-flex>
                  </v-layout>
                </v-card>
                <v-card
                  v-else-if="stageSorts.includes(sortBy)"
                  class="mx-0 my-1 px-0 py-0"
                  @click="changeSort('ratings', 'stage', x.key)"
                >
                  <v-layout>
                    <v-flex xs3 class="center" align="center">
                      {{ x.key.charAt(0).toUpperCase() + x.key.slice(1) }}
                      Stage
                    </v-flex>
                    <v-flex xs7>
                      <v-progress-linear
                        :color="stageColors[x.key]"
                        height="20"
                        :value="x.avg * 10"
                      />
                    </v-flex>
                    <v-flex xs2 class="center" align="center">{{
                      x.avg
                    }}</v-flex>
                  </v-layout>
                </v-card>
              </span>
            </v-card>
          </v-flex>
          <v-flex xs12 md10 v-else>
            <v-card color="white" v-animate-css="'fadeInDown'">
              <v-img
                :src="mon_to_change.data.img"
                class="center-img mt-2 mb-4"
                :width="small ? w / 2 : w / 3.5"
                :height="h / 3.5"
                contain
              />
            </v-card>
            <p :class="medtext + ' mt-3'" v-animate-css="'fadeInDown'">
              #{{ idToChange.replace(/\D/g, "") }}
              {{ mon_to_change.data.name }}
            </p>
            <div v-animate-css="'fadeInUp'">
              <v-layout justify-center my-4>
                <v-btn
                  large
                  icon
                  color="red"
                  class="white--text"
                  @click="changeRating(1)"
                  >1</v-btn
                >
                <v-btn
                  large
                  icon
                  color="pink"
                  class="white--text"
                  @click="changeRating(2)"
                  >2</v-btn
                >
                <v-btn
                  large
                  icon
                  color="purple"
                  class="white--text"
                  @click="changeRating(3)"
                  >3</v-btn
                >
                <v-btn
                  large
                  icon
                  color="deep-purple"
                  class="white--text"
                  @click="changeRating(4)"
                  >4</v-btn
                >
                <v-btn
                  large
                  icon
                  color="indigo"
                  class="white--text"
                  @click="changeRating(5)"
                  >5</v-btn
                >
                <span v-if="!small">
                  <v-btn
                    large
                    icon
                    color="blue"
                    class="white--text"
                    @click="changeRating(6)"
                    >6</v-btn
                  >
                  <v-btn
                    large
                    icon
                    color="cyan"
                    class="white--text"
                    @click="changeRating(7)"
                    >7</v-btn
                  >
                  <v-btn
                    large
                    icon
                    color="teal"
                    class="white--text"
                    @click="changeRating(8)"
                    >8</v-btn
                  >
                  <v-btn
                    large
                    icon
                    color="green darken-2"
                    class="white--text"
                    @click="changeRating(9)"
                    >9</v-btn
                  >
                  <v-btn
                    large
                    icon
                    color="green"
                    class="white--text"
                    @click="changeRating(10)"
                    >10</v-btn
                  >
                </span>
              </v-layout>
              <v-layout v-if="small" justify-center my-4>
                <v-btn
                  large
                  icon
                  color="blue"
                  class="white--text"
                  @click="changeRating(6)"
                  >6</v-btn
                >
                <v-btn
                  large
                  icon
                  color="cyan"
                  class="white--text"
                  @click="changeRating(7)"
                  >7</v-btn
                >
                <v-btn
                  large
                  icon
                  color="teal"
                  class="white--text"
                  @click="changeRating(8)"
                  >8</v-btn
                >
                <v-btn
                  large
                  icon
                  color="green darken-2"
                  class="white--text"
                  @click="changeRating(9)"
                  >9</v-btn
                >
                <v-btn
                  large
                  icon
                  color="green"
                  class="white--text"
                  @click="changeRating(10)"
                  >10</v-btn
                >
              </v-layout>
            </div>
          </v-flex>
        </v-layout>
      </v-flex>
      <v-flex v-show="changing || !small" xs12 md3 :ml-4="!small" :mt-4="small">
        <div>
          <p :class="`${medtext} my-2`">Limit Traits</p>
          <v-layout justify-center>
            <v-btn
              :small="small"
              dark
              :color="boolean_limits['all'] ? 'red darken-3' : ''"
              class="font-weight-bold"
              @click="toggle('boolean', 'all')"
              >CLEAR TRAITS</v-btn
            >
          </v-layout>
          <span v-for="b in Object.keys(boolean_limits)" :key="b">
            <v-btn
              v-if="b !== 'all'"
              :small="small"
              dark
              :color="boolean_limits[b] ? 'red darken-3' : ''"
              @click="toggle('boolean', b)"
              >{{ boolean_to_upperplural(b) }}</v-btn
            >
          </span>
        </div>
        <div class="my-4">
          <p :class="`${medtext} my-2`">Aggregated Rankings</p>
          <v-btn
            :small="small"
            dark
            :color="this.sortBy == 'starter_lines' ? 'green darken-2' : ''"
            @click="changeSort('starter_lines')"
            >STARTER LINES</v-btn
          >
          <v-btn
            :small="small"
            dark
            :color="this.sortBy == 'pseudo_lines' ? 'green darken-2' : ''"
            @click="changeSort('pseudo_lines')"
            >PSEUDO LEGENDARY LINES</v-btn
          >
          <v-btn
            :small="small"
            dark
            :color="this.sortBy == 'gens_by_starters' ? 'green darken-2' : ''"
            @click="changeSort('gens_by_starters')"
            >GENS BY STARTER LINES</v-btn
          >
          <v-btn
            :small="small"
            dark
            :color="this.sortBy == 'regional_birds' ? 'green darken-2' : ''"
            @click="changeSort('regional_birds')"
            >REGIONAL BIRD LINES</v-btn
          >
          <v-btn
            :small="small"
            dark
            :color="this.sortBy == 'regional_rodents' ? 'green darken-2' : ''"
            @click="changeSort('regional_rodents')"
            >REGIONAL RODENT LINES</v-btn
          >
          <v-btn
            :small="small"
            dark
            :color="this.sortBy == 'regional_bugs' ? 'green darken-2' : ''"
            @click="changeSort('regional_bugs')"
            >REGIONAL BUG LINES</v-btn
          >
          <v-btn
            :small="small"
            dark
            :color="
              this.sortBy == 'regional_sets_with_starters'
                ? 'green darken-2'
                : ''
            "
            @click="changeSort('regional_sets_with_starters')"
            >REGIONAL SETS</v-btn
          >
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
/* eslint-disable */

function takeAvg(array) {
  array.forEach(x => {
    if (x.count > 0) {
      x.avg = parseFloat((x.score / x.count).toFixed(2));
    } else {
      x.avg = 0;
    }
  });
  return array;
}

function avgSort(a, b) {
  if (a.avg > b.avg) {
    return -1;
  } else if (a.avg < b.avg) {
    return 1;
  }
  return 0;
}

function ratingSort(a, b) {
  if (a.data.rating > b.data.rating) {
    return -1;
  } else if (a.data.rating < b.data.rating) {
    return 1;
  }
  return 0;
}

function valueCheck(array, value, rating) {
  let arr = array;
  let dict;
  arr.forEach(d => {
    let val = d.key;
    if (val === value) {
      dict = d;
    }
  });
  if (dict !== undefined) {
    dict.count++;
    dict.score += rating;
  } else {
    arr.push({
      key: value,
      count: 1,
      score: rating,
      avg: 0
    });
  }
  return arr;
}

import Buttons from "./Buttons.vue";
import PreventUnload from "vue-prevent-unload";

export default {
  components: {
    Buttons,
    PreventUnload
  },
  data() {
    return {
      pokemon: this.$route.params.pokemon,
      completed: this.$route.params.completed,
      h: window.innerHeight,
      w: window.innerWidth,
      sortBy: "ratings",
      idToChange: "None",
      hover: "",
      show_range: [0, 19],
      changing: false,
      line_limit: "",
      gen_limits: {
        1: false,
        2: false,
        3: false,
        4: false,
        5: false,
        6: false,
        7: false,
        8: false,
        all: true
      },
      type_limits: {
        Normal: false,
        Fire: false,
        Fighting: false,
        Water: false,
        Flying: false,
        Grass: false,
        Poison: false,
        Electric: false,
        Ground: false,
        Psychic: false,
        Rock: false,
        Ice: false,
        Bug: false,
        Dragon: false,
        Ghost: false,
        Dark: false,
        Steel: false,
        Fairy: false,
        all: true
      },
      stage_limits: {
        first: false,
        middle: false,
        final: false,
        all: true
      },
      boolean_limits: {
        alolan: false,
        galarian: false,
        starter: false,
        legendary: false,
        mythical: false,
        pseudo: false,
        baby: false,
        regional_bird: false,
        regional_rodent: false,
        regional_bug: false,
        fossil: false,
        ultra: false,
        all: true
      },
      lineSorts: [
        "pseudo_lines",
        "starter_lines",
        "regional_birds",
        "regional_rodents",
        "regional_bugs"
      ],
      typeSorts: ["types"],
      genSorts: ["gens", "gens_by_starters", "regional_sets_with_starters"],
      stageSorts: ["stages"],
      typeColors: {
        Normal: "brown lighten-4",
        Fire: "deep-orange accent-3",
        Fighting: "red darken-4",
        Water: "blue darken-1",
        Flying: "indigo lighten-3",
        Grass: "green darken-2",
        Poison: "purple darken-1",
        Electric: "amber darken-1",
        Ground: "orange accent-2",
        Psychic: "pink",
        Rock: "brown",
        Ice: "light-blue lighten-3",
        Bug: "light-green darken-1",
        Dragon: "deep-purple accent-2",
        Ghost: "deep-purple darken-4",
        Dark: "grey darken-4",
        Steel: "blue-grey lighten-3",
        Fairy: "pink lighten-3"
      },
      genColors: [
        "red",
        "amber",
        "green",
        "cyan",
        "black",
        "deep-purple",
        "orange",
        "grey"
      ],
      stageColors: {
        first: "red",
        middle: "green",
        final: "blue"
      },
      types: [],
      gens: [],
      stages: [],
      pseudo_lines: [],
      starter_lines: [],
      gens_by_starters: [],
      regional_birds: [],
      regional_rodents: [],
      regional_bugs: [],
      regional_sets: [],
      regional_sets_with_starters: []
    };
  },
  computed: {
    sortedArray() {
      /* eslint-disable no-eval */
      return eval("this." + this.sortBy);
    },
    sorted_allowed() {
      let sa = [];
      if (this.sortBy === "ratings") {
        for (let mon in this.sortedArray) {
          mon = this.sortedArray[mon];
          if (this.allowed(mon.data)) {
            sa.push(mon);
          }
        }
      } else {
        sa = this.sortedArray;
      }
      return sa;
    },
    last_shown() {
      if (this.show_range[1] >= this.sorted_allowed.length) {
        return this.sorted_allowed.length - 1;
      } else {
        return this.show_range[1];
      }
    },
    sorted_allowed_shown() {
      let i1 = this.show_range[0];
      let i2 = this.last_shown + 1;
      return this.sorted_allowed.slice(i1, i2);
    },
    ratings() {
      return this.pokemon.concat().sort(ratingSort);
    },
    any_allowed() {
      let any = false;
      if (this.sortBy === "ratings") {
        for (let a in this.sortedArray) {
          if (this.allowed(this.sortedArray[a].data)) {
            any = true;
          }
        }
      } else {
        return true;
      }
      return any;
    },
    mon_to_change() {
      let gotmon = false;
      for (let mon in this.pokemon) {
        mon = this.pokemon[mon];
        if (mon.id === this.idToChange) {
          console.log(mon);
          return mon;
          gotmon = true;
          break;
        }
      }
      if (!gotmon) {
        return "None";
      }
    },
    small() {
      return this.w < 700;
    },
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
        ? "title"
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
    prevtext() {
      if (this.small) {
        return "<<";
      } else {
        return "< PREV";
      }
    },
    nexttext() {
      if (this.small) {
        return ">>";
      } else {
        return "NEXT >";
      }
    }
  },
  mounted() {
    this.process();
  },
  watch: {
    changing() {
      this.idToChange = "None";
    }
  },
  methods: {
    process() {
      // initialize types
      Object.keys(this.type_limits).forEach(t => {
        if (t !== "all") {
          this.types.push({
            key: t,
            count: 0,
            score: 0,
            avg: 0
          });
        }
      });
      // initialize gens
      Object.keys(this.gen_limits).forEach(g => {
        if (g !== "all") {
          g = parseInt(g);
          this.gens.push({
            key: g,
            count: 0,
            score: 0,
            avg: 0
          });
        }
      });
      Object.keys(this.stage_limits).forEach(s => {
        if (s !== "all") {
          this.stages.push({
            key: s,
            count: 0,
            score: 0,
            avg: 0
          });
        }
      });
      // for each pokemon
      this.pokemon.forEach(mon => {
        mon = mon.data;
        if (this.allowed(mon)) {
          // none of this is relevant to mega evolutions
          if (!mon.mega) {
            // extract relevant attributes from current pokemon
            let type1 = mon.types[0];
            let type2;
            if (mon.types.length > 1) {
              type2 = mon.types[1];
            }
            let gen = mon.gen;
            let stage = this.findForm(mon);
            let rating = mon.rating;
            let line = mon.line;
            let pseudo = mon.pseudo;
            let starter = mon.starter;
            let regionalBird = mon.regional_bird;
            let regionalRodent = mon.regional_rodent;
            let regionalBug = mon.regional_bug;
            // add in data for current pokemon's type, gen
            let typeDict1;
            this.types.forEach(t => {
              if (t.key === type1) {
                typeDict1 = t;
              }
            });
            let typeDict2;
            if (type2) {
              this.types.forEach(t => {
                if (t.key === type2) {
                  typeDict2 = t;
                }
              });
            }
            let genDict;
            this.gens.forEach(g => {
              if (g.key === gen) {
                genDict = g;
              }
            });
            let stageDict;
            this.stages.forEach(s => {
              if (s.key === stage) {
                stageDict = s;
              }
            });
            typeDict1.count++;
            typeDict1.score += rating;
            if (typeDict2) {
              typeDict2.count++;
              typeDict2.score += rating;
            }
            genDict.count++;
            genDict.score += rating;
            stageDict.count++;
            stageDict.score += rating;
            // if pokemon is in a pseudo-legendary line
            if (pseudo) {
              this.pseudo_lines = valueCheck(this.pseudo_lines, line, rating);
            }
            // if pokemon is in a starter line
            if (starter) {
              this.starter_lines = valueCheck(this.starter_lines, line, rating);
              this.gens_by_starters = valueCheck(
                this.gens_by_starters,
                gen,
                rating
              );
              this.regional_sets_with_starters = valueCheck(
                this.regional_sets_with_starters,
                gen,
                rating
              );
            }
            // if pokemon is in a regional bird line
            if (regionalBird) {
              this.regional_birds = valueCheck(
                this.regional_birds,
                line,
                rating
              );
              this.regional_sets = valueCheck(this.regional_sets, gen, rating);
              this.regional_sets_with_starters = valueCheck(
                this.regional_sets_with_starters,
                gen,
                rating
              );
            }
            // if pokemon is in a regional rodent line
            if (regionalRodent) {
              this.regional_rodents = valueCheck(
                this.regional_rodents,
                line,
                rating
              );
              this.regional_sets = valueCheck(this.regional_sets, gen, rating);
              this.regional_sets_with_starters = valueCheck(
                this.regional_sets_with_starters,
                gen,
                rating
              );
            }
            // if pokemon is in a regional bug line
            if (regionalBug) {
              this.regional_bugs = valueCheck(this.regional_bugs, line, rating);
              this.regional_sets = valueCheck(this.regional_sets, gen, rating);
              this.regional_sets_with_starters = valueCheck(
                this.regional_sets_with_starters,
                gen,
                rating
              );
            }
          }
        }
      });
      // set and sort by averages
      this.types = takeAvg(this.types).sort(avgSort);
      this.gens = takeAvg(this.gens).sort(avgSort);
      this.stages = takeAvg(this.stages).sort(avgSort);
      this.pseudo_lines = takeAvg(this.pseudo_lines).sort(avgSort);
      this.starter_lines = takeAvg(this.starter_lines).sort(avgSort);
      this.gens_by_starters = takeAvg(this.gens_by_starters).sort(avgSort);
      this.regional_birds = takeAvg(this.regional_birds).sort(avgSort);
      this.regional_rodents = takeAvg(this.regional_rodents).sort(avgSort);
      this.regional_bugs = takeAvg(this.regional_bugs).sort(avgSort);
      this.regional_sets = takeAvg(this.regional_sets).sort(avgSort);
      this.regional_sets_with_starters = takeAvg(
        this.regional_sets_with_starters
      ).sort(avgSort);
    },
    changeSort(s = "ratings", k = "", v = "") {
      if (s !== "ratings") {
        this.reset_limits();
      } else if (k !== "") {
        this.reset_limits();
        this.toggle(k, v);
      } else {
        this.line_limit = "";
      }
      this.sortBy = s;
      this.idToChange = "None";
    },
    toggleSort(s) {
      if (this.sortBy == s) {
        this.changeSort();
      } else {
        this.changeSort(s);
      }
    },
    toggle(group, limit) {
      if (group == "line") {
        this.line_limit = limit;
      } else {
        let aggs = ["type", "gen", "stage"];
        if (!aggs.includes(group) || group + "s" === this.sortBy) {
          this.changeSort();
        }
        /* eslint-disable no-eval */
        group = eval("this." + group + "_limits");
        if (limit == "all") {
          for (let g in group) {
            group[g] = false;
          }
          group[limit] = true;
        } else {
          group[limit] = !group[limit];
          let all_off = true;
          for (let g in group) {
            if (group[g]) {
              all_off = false;
              break;
            }
          }
          if (all_off) {
            group["all"] = true;
          } else {
            group["all"] = false;
          }
        }
      }
      this.reset();
    },
    reset_limits() {
      this.line_limit = "";
      let gl = this.gen_limits;
      let tl = this.type_limits;
      let sl = this.stage_limits;
      let bl = this.boolean_limits;
      if (!gl["all"]) {
        this.toggle("gen", "all");
      }
      if (!tl["all"]) {
        this.toggle("type", "all");
      }
      if (!sl["all"]) {
        this.toggle("stage", "all");
      }
      if (!bl["all"]) {
        this.toggle("boolean", "all");
      }
      this.changeSort("ratings");
    },
    allowed(mon) {
      let allow = true;
      let gl = this.gen_limits;
      let tl = this.type_limits;
      let sl = this.stage_limits;
      let bl = this.boolean_limits;
      if (this.line_limit !== "") {
        if (mon["line"] == this.line_limit) {
          return true;
        } else {
          return false;
        }
      }
      if (!bl["all"]) {
        let good = false;
        for (let l in bl) {
          if (bl[l] && mon[l]) {
            good = true;
            break;
          }
        }
        if (!good) {
          allow = false;
        }
      }
      if (allow && !gl["all"]) {
        let gs = [];
        for (let l in gl) {
          if (gl[l]) {
            gs.push(l);
          }
        }
        if (!gs.includes(mon["gen"].toString())) {
          allow = false;
        }
      }
      if (allow && !tl["all"]) {
        let ts = [];
        for (let l in tl) {
          if (tl[l]) {
            ts.push(l);
          }
        }
        let good = false;
        for (let mt in mon["types"]) {
          if (ts.includes(mon["types"][mt])) {
            good = true;
          }
        }
        if (!good) {
          allow = false;
        }
      }
      if (allow && !sl["all"]) {
        let ss = [];
        for (let l in sl) {
          if (sl[l]) {
            ss.push(l);
          }
        }
        if (!ss.includes(this.findForm(mon))) {
          allow = false;
        }
      }
      return allow;
    },
    changeRating(value) {
      this.mon_to_change.data.rating = value;
      this.reset();
    },
    reset() {
      this.types = [];
      this.gens = [];
      this.stages = [];
      this.pseudo_lines = [];
      this.starter_lines = [];
      this.gens_by_starters = [];
      this.regional_birds = [];
      this.regional_rodents = [];
      this.regional_bugs = [];
      this.regional_sets = [];
      this.regional_sets_with_starters = [];
      this.idToChange = "None";
      this.process();
    },
    findForm(mon) {
      if (mon.stage === mon.stages) {
        return "final";
      } else if (mon.stages === "3" && mon.stage === "2") {
        return "middle";
      }
      return "first";
    },
    boolean_to_upperplural(b) {
      let b2ups = {
        alolan: "ALOLAN FORMS",
        galarian: "GALARIAN FORMS",
        starter: "STARTERS",
        legendary: "LEGENDARIES",
        mythical: "MYTHICALS",
        pseudo: "PSEUDO-LEGENDARIES",
        baby: "BABIES",
        regional_bird: "REGIONAL BIRDS",
        regional_rodent: "REGIONAL RODENTS",
        regional_bug: "REGIONAL BUGS",
        fossil: "FOSSILS",
        ultra: "ULTRA BEASTS"
      };
      return b2ups[b];
    },
    back_to_ratings() {
      this.$router.push({
        name: "Ratings",
        params: {
          pokemon: this.pokemon
        }
      });
    },
    changeRange(forward) {
      if (forward) {
        this.show_range = this.show_range.map(x => x + 20);
      } else {
        this.show_range = this.show_range.map(x => x - 20);
      }
    }
  },
  beforeRouteLeave(to, from, next) {
    if (!this.completed && to.name == "Ratings") {
      next();
    } else {
      const answer = window.confirm(
        "If leave this page and you have not saved your PokéPallet, you cannot get it back. Are you sure you want to leave?"
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
  text-align: center;
  align-self: center;
  justify-self: center;
}
.bot {
  text-align: center;
  align-self: flex-end;
  justify-self: center;
}
.above {
  position: absolute;
  z-index: 2;
}
.center-img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>
