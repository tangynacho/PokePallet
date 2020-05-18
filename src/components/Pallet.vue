<template>
  <v-container fluid>
    <v-layout justify-center mt-2>
      <v-flex xs4 id="col2" class="mb-4">
        <p class="display-1 my-2">Type Rankings</p>
        <v-btn
          v-for="t in ts"
          :key="t"
          dark
          @click="changeSort('ratings', { types: t })"
          >{{ t }} TYPES</v-btn
        >
      </v-flex>
      <v-flex xs3 id="col3" class="mb-4">
        <v-flex my-4>
          <v-btn
            color="amber"
            class="font-weight-bold"
            @click="changeSort('ratings')"
            >ALL POKEMON
          </v-btn>
          <v-layout justify-center mb-2>
            <v-btn color="red darken-3" dark @click="changeSort('types')"
              >TYPES</v-btn
            >
            <v-btn color="blue darken-2" dark @click="changeSort('gens')"
              >GENS</v-btn
            >
          </v-layout>
        </v-flex>
        <p class="display-1 my-2">Gen Rankings</p>
        <v-btn
          v-for="g in gs"
          :key="g"
          dark
          @click="changeSort('ratings', { gen: g })"
          >GEN {{ g }}</v-btn
        >
      </v-flex>
      <v-flex xs4 id="col1" class="mb-4">
        <div>
          <p class="display-1 my-2">Aggregated Rankings</p>
          <v-btn dark @click="changeSort('pseudo_lines')"
            >PSEUDO LEGENDARY LINES</v-btn
          >
          <v-btn dark @click="changeSort('starter_lines')">STARTER LINES</v-btn>
          <v-btn dark @click="changeSort('gens_by_starters')"
            >GENS BY STARTER LINES</v-btn
          >
          <v-btn dark @click="changeSort('regional_birds')"
            >REGIONAL BIRD LINES</v-btn
          >
          <v-btn dark @click="changeSort('regional_rodents')"
            >REGIONAL RODENT LINES</v-btn
          >
          <v-btn dark @click="changeSort('regional_bugs')"
            >REGIONAL BUG LINES</v-btn
          >
          <v-btn dark @click="changeSort('regional_sets_with_starters')"
            >REGIONAL SETS</v-btn
          >
        </div>
      </v-flex>
    </v-layout>
    <v-layout justify-center>
      <v-flex xs6>
        <v-card color="grey darken-3">
          <span v-if="sortedArray.length === 0">
            <v-card-text class="title text-xs-left">No results.</v-card-text>
          </span>
          <span
            v-for="x in sortedArray"
            :key="sortedArray.indexOf(x)"
            class="headline my-0 py-0 text-xs-left"
          >
            <v-card v-if="sortBy === 'ratings'" class="mx-0 my-0 px-0 py-0">
              <v-layout v-if="allowed(x.data)">
                <v-flex xs3 class="center" align="center">
                  {{ x.data.name }}
                </v-flex>
                <v-flex v-if="idToChange != x.id" xs6>
                  <v-progress-linear
                    height="20"
                    :color="typeColors[x.data.types[0]]"
                    :value="x.data.rating * 10"
                  />
                </v-flex>
                <v-flex
                  v-if="idToChange != x.id"
                  xs1
                  class="center"
                  align="center"
                >
                  {{ x.data.rating }}
                </v-flex>
                <v-flex v-if="idToChange != x.id" xs2 class="text-xs-center">
                  <v-btn
                    color="red darken-2"
                    class="white--text"
                    round
                    @click="setIDToChange(x.id)"
                  >
                    EDIT
                  </v-btn>
                </v-flex>
                <v-flex xs9 v-if="idToChange == x.id">
                  <buttons
                    :rating="x.data.rating"
                    :color="typeColors[x.data.types[0]]"
                    @n="changeRating"
                  />
                </v-flex>
              </v-layout>
            </v-card>
            <v-card
              v-else-if="lineSorts.includes(sortBy)"
              class="mx-0 my-0 px-0 py-0"
            >
              <span v-for="mon in pokemon" :key="mon.id">
                <v-layout v-if="mon.id === x.key">
                  <v-flex xs3 class="center" align="center">
                    {{ mon.data.name }}
                  </v-flex>
                  <v-flex xs5>
                    <v-progress-linear
                      :color="typeColors[mon.data.types[0]]"
                      height="20"
                      :value="x.avg * 10"
                    />
                  </v-flex>
                  <v-flex xs2 class="center" align="center">
                    {{ x.avg }}
                  </v-flex>
                  <v-flex xs2 class="text-xs-center">
                    <v-btn
                      color="red darken-2"
                      class="white--text"
                      round
                      @click="changeSort('ratings', { line: x.key })"
                    >
                      EDIT LINE
                    </v-btn>
                  </v-flex>
                </v-layout>
              </span>
            </v-card>
            <v-card
              v-else-if="genSorts.includes(sortBy)"
              class="mx-0 my-0 px-0 py-0"
            >
              <v-layout>
                <v-flex xs3 class="center" align="center">
                  Gen {{ x.key }}
                </v-flex>
                <v-flex xs5>
                  <v-progress-linear
                    :color="genColors[parseInt(x.key) - 1]"
                    height="20"
                    :value="x.avg * 10"
                  />
                </v-flex>
                <v-flex xs2 class="center" align="center">
                  {{ x.avg }}
                </v-flex>
                <v-flex xs2 class="text-xs-center">
                  <v-btn
                    color="red darken-2"
                    class="white--text"
                    round
                    @click="changeSort('ratings', { gen: x.key })"
                  >
                    EDIT GEN
                  </v-btn>
                </v-flex>
              </v-layout>
            </v-card>
            <v-card
              v-else-if="typeSorts.includes(sortBy)"
              class="mx-0 my-0 px-0 py-0"
            >
              <v-layout>
                <v-flex xs3 class="center" align="center">
                  {{ x.key }}
                </v-flex>
                <v-flex xs5>
                  <v-progress-linear
                    :color="typeColors[x.key]"
                    height="20"
                    :value="x.avg * 10"
                  />
                </v-flex>
                <v-flex xs2 class="center" align="center">
                  {{ x.avg }}
                </v-flex>
                <v-flex xs2 class="text-xs-center">
                  <v-btn
                    color="red darken-2"
                    class="white--text"
                    round
                    @click="changeSort('ratings', { types: x.key })"
                  >
                    EDIT TYPE
                  </v-btn>
                </v-flex>
              </v-layout>
            </v-card>
          </span>
        </v-card>
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

export default {
  components: {
    Buttons
  },
  data() {
    return {
      pokemon: this.$route.params.pokemon,
      sortBy: "ratings",
      onlyShow: {},
      idToChange: "None",
      gs: [1, 2, 3, 4, 5, 6, 7, 8],
      ts: [
        "Normal",
        "Fire",
        "Fighting",
        "Water",
        "Flying",
        "Grass",
        "Poison",
        "Electric",
        "Ground",
        "Psychic",
        "Rock",
        "Ice",
        "Bug",
        "Dragon",
        "Ghost",
        "Dark",
        "Steel",
        "Fairy"
      ],
      lineSorts: [
        "pseudo_lines",
        "starter_lines",
        "regional_birds",
        "regional_rodents",
        "regional_bugs"
      ],
      genSorts: ["gens", "gens_by_starters", "regional_sets_with_starters"],
      typeSorts: ["types"],
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
      types: [],
      gens: [],
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
    ratings() {
      return this.pokemon.concat().sort(ratingSort);
    }
  },
  mounted() {
    this.process();
  },
  methods: {
    process() {
      // initialize types
      this.ts.forEach(t => {
        this.types.push({
          key: t,
          count: 0,
          score: 0,
          avg: 0
        });
      });
      // initialize gens
      this.gs.forEach(g => {
        this.gens.push({
          key: g,
          count: 0,
          score: 0,
          avg: 0
        });
      });
      // for each pokemon
      this.pokemon.forEach(mon => {
        mon = mon.data;

        // none of this is relevant to mega evolutions
        if (!mon.mega) {
          // extract relevant attributes from current pokemon
          let type1 = mon.types[0];
          let type2;
          if (mon.types.length > 1) {
            type2 = mon.types[1];
          }
          let gen = mon.gen;
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
          typeDict1.count++;
          typeDict1.score += rating;
          if (typeDict2) {
            typeDict2.count++;
            typeDict2.score += rating;
          }
          genDict.count++;
          genDict.score += rating;
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
            this.regional_birds = valueCheck(this.regional_birds, line, rating);
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
      });
      // set and sort by averages
      this.types = takeAvg(this.types).sort(avgSort);
      this.gens = takeAvg(this.gens).sort(avgSort);
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
    changeSort(s = "ratings", o = {}) {
      this.sortBy = s;
      this.onlyShow = o;
      this.idToChange = "None";
    },
    allowed(mon) {
      let al = true;
      const keys = Object.keys(this.onlyShow);
      keys.forEach(key => {
        if (key !== "types") {
          if (mon[key] !== this.onlyShow[key]) {
            al = false;
          }
        } else {
          if (
            mon[key][0] !== this.onlyShow[key] &&
            mon[key][1] !== this.onlyShow[key]
          ) {
            al = false;
          }
        }
      });
      return al;
    },
    setIDToChange(i) {
      this.idToChange = i;
    },
    changeRating(value) {
      this.pokemon.forEach(mon => {
        if (mon.id === this.idToChange) {
          mon.data.rating = value;
          this.reset();
        }
      });
    },
    reset() {
      this.types = [];
      this.gens = [];
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
    }
  },
  beforeRouteLeave(to, from, next) {
    const answer = window.confirm(
      "If leave this page and you have not saved your PokePallet, you cannot get it back. Are you sure you want to leave?"
    );
    if (answer) {
      next();
    } else {
      next(false);
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
</style>
