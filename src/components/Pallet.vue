<template>
  <v-container fluid>
    <prevent-unload :when="true" />
    <p class="display-3 font-weight-bold">Welcome to your PokéPallet!</p>
    <v-layout justify-center>
      <v-flex xs3 id="col2" class="mb-4 mr-2">
        <div>
          <p class="display-1 my-2">Limit Traits</p>
          <v-layout justify-center>
            <v-btn
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
              dark
              :color="boolean_limits[b] ? 'red darken-3' : ''"
              @click="toggle('boolean', b)"
              >{{ boolean_to_upperplural(b) }}</v-btn
            >
          </span>
        </div>
        <div class="my-4">
          <p class="display-1 my-2">Aggregated Rankings</p>
          <v-btn
            dark
            :color="this.sortBy == 'starter_lines' ? 'green darken-2' : ''"
            @click="changeSort('starter_lines')"
            >STARTER LINES</v-btn
          >
          <v-btn
            dark
            :color="this.sortBy == 'pseudo_lines' ? 'green darken-2' : ''"
            @click="changeSort('pseudo_lines')"
            >PSEUDO LEGENDARY LINES</v-btn
          >
          <v-btn
            dark
            :color="this.sortBy == 'gens_by_starters' ? 'green darken-2' : ''"
            @click="changeSort('gens_by_starters')"
            >GENS BY STARTER LINES</v-btn
          >
          <v-btn
            dark
            :color="this.sortBy == 'regional_birds' ? 'green darken-2' : ''"
            @click="changeSort('regional_birds')"
            >REGIONAL BIRD LINES</v-btn
          >
          <v-btn
            dark
            :color="this.sortBy == 'regional_rodents' ? 'green darken-2' : ''"
            @click="changeSort('regional_rodents')"
            >REGIONAL RODENT LINES</v-btn
          >
          <v-btn
            dark
            :color="this.sortBy == 'regional_bugs' ? 'green darken-2' : ''"
            @click="changeSort('regional_bugs')"
            >REGIONAL BUG LINES</v-btn
          >
          <v-btn
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
      <v-flex xs6 id="col3" class="mb-4">
        <p class="headline mb-4">
          Use the buttons to see all sorts of different rankings!
        </p>
        <v-btn color="amber" class="font-weight-bold" @click="reset_limits()"
          >SHOW ALL POKEMON</v-btn
        >
        <v-layout justify-center mt-4>
          <v-flex xs12>
            <v-card color="grey darken-3">
              <span v-if="!any_allowed">
                <v-card-text class="headline text-xs-center"
                  >No results.</v-card-text
                >
              </span>
              <span
                v-for="x in sortedArray"
                :key="sortedArray.indexOf(x)"
                class="headline my-0 py-0 text-xs-left"
              >
                <v-card v-if="sortBy === 'ratings'" class="mx-0 my-1 px-0 py-0">
                  <v-layout v-if="allowed(x.data)">
                    <v-flex xs3 class="center" align="center">{{
                      x.data.name
                    }}</v-flex>
                    <v-flex v-if="idToChange != x.id" xs6>
                      <v-progress-linear
                        striped
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
                      >{{ x.data.rating }}</v-flex
                    >
                    <v-flex
                      v-if="idToChange != x.id"
                      xs2
                      class="text-xs-center"
                    >
                      <v-btn
                        color="grey darken-3"
                        class="white--text"
                        round
                        @click="setIDToChange(x.id)"
                        >EDIT</v-btn
                      >
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
                  class="mx-0 my-1 px-0 py-0"
                >
                  <span v-for="mon in pokemon" :key="mon.id">
                    <v-layout v-if="mon.id === x.key">
                      <v-flex xs3 class="center" align="center">{{
                        mon.data.name
                      }}</v-flex>
                      <v-flex xs5>
                        <v-progress-linear
                          :color="typeColors[mon.data.types[0]]"
                          height="20"
                          :value="x.avg * 10"
                        />
                      </v-flex>
                      <v-flex xs2 class="center" align="center">{{
                        x.avg
                      }}</v-flex>
                      <v-flex xs2 class="text-xs-center">
                        <v-btn
                          color="grey darken-3"
                          class="white--text"
                          round
                          @click="changeSort('ratings', 'line', x.key)"
                          >EDIT LINE</v-btn
                        >
                      </v-flex>
                    </v-layout>
                  </span>
                </v-card>
                <v-card
                  v-else-if="genSorts.includes(sortBy)"
                  class="mx-0 my-1 px-0 py-0"
                >
                  <v-layout>
                    <v-flex xs3 class="center" align="center"
                      >Gen {{ x.key }}</v-flex
                    >
                    <v-flex xs5>
                      <v-progress-linear
                        :color="genColors[parseInt(x.key) - 1]"
                        height="20"
                        :value="x.avg * 10"
                      />
                    </v-flex>
                    <v-flex xs2 class="center" align="center">{{
                      x.avg
                    }}</v-flex>
                    <v-flex xs2 class="text-xs-center">
                      <v-btn
                        color="grey darken-3"
                        class="white--text"
                        round
                        @click="changeSort('ratings', 'gen', x.key)"
                        >EDIT GEN</v-btn
                      >
                    </v-flex>
                  </v-layout>
                </v-card>
                <v-card
                  v-else-if="typeSorts.includes(sortBy)"
                  class="mx-0 my-1 px-0 py-0"
                >
                  <v-layout>
                    <v-flex xs3 class="center" align="center">{{
                      x.key
                    }}</v-flex>
                    <v-flex xs5>
                      <v-progress-linear
                        :color="typeColors[x.key]"
                        height="20"
                        :value="x.avg * 10"
                      />
                    </v-flex>
                    <v-flex xs2 class="center" align="center">{{
                      x.avg
                    }}</v-flex>
                    <v-flex xs2 class="text-xs-center">
                      <v-btn
                        color="grey darken-3"
                        class="white--text"
                        round
                        @click="changeSort('ratings', 'type', x.key)"
                        >EDIT TYPE</v-btn
                      >
                    </v-flex>
                  </v-layout>
                </v-card>
                <v-card
                  v-else-if="stageSorts.includes(sortBy)"
                  class="mx-0 my-1 px-0 py-0"
                >
                  <v-layout>
                    <v-flex xs3 class="center" align="center"
                      >{{
                        x.key.charAt(0).toUpperCase() + x.key.slice(1)
                      }}
                      Stage</v-flex
                    >
                    <v-flex xs5>
                      <v-progress-linear
                        :color="stageColors[x.key]"
                        height="20"
                        :value="x.avg * 10"
                      />
                    </v-flex>
                    <v-flex xs2 class="center" align="center">{{
                      x.avg
                    }}</v-flex>
                    <v-flex xs2 class="text-xs-center">
                      <v-btn
                        color="grey darken-3"
                        class="white--text"
                        round
                        @click="changeSort('ratings', 'stage', x.key)"
                        >EDIT STAGE</v-btn
                      >
                    </v-flex>
                  </v-layout>
                </v-card>
              </span>
            </v-card>
          </v-flex>
        </v-layout>
      </v-flex>
      <v-flex xs3 id="col1" class="mb-4 ml-2">
        <div>
          <p class="display-1 my-2">Limit Types</p>
          <v-layout justify-center>
            <v-btn
              dark
              :color="
                type_limits['all'] && sortBy !== 'types' ? 'red darken-3' : ''
              "
              class="font-weight-bold"
              @click="toggle('type', 'all')"
              >SHOW ALL TYPES</v-btn
            >
            <v-btn
              dark
              :color="this.sortBy == 'types' ? 'blue darken-2' : ''"
              class="font-weight-bold"
              @click="toggleSort('types')"
              >AGGREGATE TYPES</v-btn
            >
          </v-layout>
          <span v-for="t in Object.keys(type_limits)" :key="t">
            <v-btn
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
          <p class="display-1 my-2">Limit Gens</p>
          <v-layout justify-center>
            <v-btn
              dark
              :color="
                gen_limits['all'] && sortBy !== 'gens' ? 'red darken-3' : ''
              "
              class="font-weight-bold"
              @click="toggle('gen', 'all')"
              >SHOW ALL GENS</v-btn
            >
            <v-btn
              dark
              :color="this.sortBy == 'gens' ? 'blue darken-1' : ''"
              class="font-weight-bold"
              @click="toggleSort('gens')"
              >AGGREGATE GENS</v-btn
            >
          </v-layout>
          <span v-for="g in Object.keys(gen_limits)" :key="g">
            <v-btn
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
          <p class="display-1 my-2">Limit Stages</p>
          <v-layout justify-center>
            <v-btn
              dark
              :color="
                stage_limits['all'] && sortBy !== 'stages' ? 'red darken-3' : ''
              "
              class="font-weight-bold"
              @click="toggle('stage', 'all')"
              >SHOW ALL STAGES</v-btn
            >
            <v-btn
              dark
              :color="this.sortBy == 'stages' ? 'blue darken-1' : ''"
              class="font-weight-bold"
              @click="toggleSort('stages')"
              >AGGREGATE STAGES</v-btn
            >
          </v-layout>
          <span v-for="s in Object.keys(stage_limits)" :key="s">
            <v-btn
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
      sortBy: "ratings",
      idToChange: "None",
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
    }
  },
  mounted() {
    this.process();
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
    }
  },
  beforeRouteLeave(to, from, next) {
    const answer = window.confirm(
      "If leave this page and you have not saved your PokéPallet, you cannot get it back. Are you sure you want to leave?"
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
