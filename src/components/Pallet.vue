<template>
  <v-container fluid>
    <v-btn color="amber" class="font-weight-bold" @click="changeSort('ratings')">ALL POKEMON</v-btn>
    <v-layout justify-center mb-2>
      <v-btn color="red darken-3" dark @click="changeSort('types')">TYPES</v-btn>
      <v-btn color="green darken-2" dark @click="changeSort('gens')">GENS</v-btn>
      <v-btn color="blue darken-2" dark @click="changeSort('colors')">COLORS</v-btn>
    </v-layout>
    <v-layout>
      <v-flex xs3 id="col1" class="mb-4">
        <div>
          <p class="display-1 mb-2">Aggregated Rankings</p>
          <v-btn dark @click="changeSort('two_stages')">TWO STAGE LINES</v-btn>
          <v-btn dark @click="changeSort('three_stages')">THREE STAGE LINES</v-btn>
          <v-btn dark @click="changeSort('pseudo_lines')">PSEUDO LEGENDARY LINES</v-btn>
          <v-btn dark @click="changeSort('starter_lines')">STARTER LINES</v-btn>
          <v-btn dark @click="changeSort('gens_by_starters')">GENS BY STARTER LINES</v-btn>
          <v-btn dark @click="changeSort('regional_birds')">REGIONAL BIRD LINES</v-btn>
          <v-btn dark @click="changeSort('regional_rodents')">REGIONAL RODENT LINES</v-btn>
          <v-btn dark @click="changeSort('regional_bugs')">REGIONAL BUG LINES</v-btn>
          <v-btn dark @click="changeSort('regional_sets_with_starters')">REGIONAL SETS</v-btn>
        </div>
        <div>
          <p class="display-1 my-2">Other</p>
          <v-btn dark @click="changeSort('ratings', { stages: '1' })">SINGLE FORMS</v-btn>
          <v-btn
            dark
            @click="changeSort('ratings', { starter: true, stage: '1' })"
          >FIRST FORM STARTERS</v-btn>
          <v-btn
            dark
            @click="changeSort('ratings', { starter: true, stage: '2' })"
          >MIDDLE FORM STARTERS</v-btn>
          <v-btn
            dark
            @click="changeSort('ratings', { starter: true, stage: '3' })"
          >FINAL FORM STARTERS</v-btn>
        </div>
      </v-flex>
      <v-flex xs3 id="col2" class="mb-4">
        <p class="display-1 my-2">Type Rankings</p>
        <v-btn
          v-for="t in ts"
          :key="t"
          dark
          @click="changeSort('ratings', { types: t })"
        >{{ t }} TYPES</v-btn>
      </v-flex>
      <v-flex xs3 id="col3" class="mb-4">
        <p class="display-1 my-2">Gen Rankings</p>
        <v-btn v-for="g in gs" :key="g" dark @click="changeSort('ratings', { gen: g })">GEN {{ g }}</v-btn>
      </v-flex>
      <v-flex xs3 id="col4" class="mb-4">
        <p class="display-1 my-2">Color Rankings</p>
        <v-btn v-for="c in cs" :key="c" dark @click="changeSort('ratings', { color: c })">{{ c }}</v-btn>
      </v-flex>
    </v-layout>
    <v-layout justify-center>
      <v-flex xs6>
        <v-card>
          <span v-if="sortedArray.length === 0">
            <v-card-text class="title text-xs-left">No results.</v-card-text>
          </span>
          <v-card-text v-for="x in sortedArray" :key="sortedArray.indexOf(x)" class="headline">
            <span v-if="sortBy === 'ratings'">
              <span v-if="allowed(x.data)">
                {{ x.data.name }}: {{ x.data.rating }}
                <v-progress-linear :color="x.data.color" height="20" :value="x.data.rating*10" />
              </span>
            </span>
            <span v-else-if="lineSorts.includes(sortBy)">
              <span v-for="mon in pokemon" :key="mon.id">
                <span v-if="mon.id === x.key">
                  {{ mon.data.name }}: {{ x.avg }}
                  <v-progress-linear :color="mon.data.color" height="20" :value="x.avg*10" />
                </span>
              </span>
            </span>
            <span v-else-if="genSorts.includes(sortBy)">
              {{ x.key }}: {{ x.avg }}
              <v-progress-linear
                :color="genColors[parseInt(x.key)-1]"
                height="20"
                :value="x.avg*10"
              />
            </span>
            <span v-else-if="typeSorts.includes(sortBy)">
              {{ x.key }}: {{ x.avg }}
              <v-progress-linear :color="typeColors[x.key]" height="20" :value="x.avg*10" />
            </span>
            <span v-else-if="sortBy === 'colors'">
              {{ x.key }}: {{ x.avg }}
              <v-progress-linear
                :color="(x.key === 'gray') ? 'grey' : x.key"
                height="20"
                :value="x.avg*10"
              />
            </span>
            <span v-else>
              {{ x.key }}: {{ x.avg }}
              <v-progress-linear color="yellow" height="20" :value="x.avg*10" />
            </span>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>

function takeAvg (array) {
  array.forEach(x => {
    if (x.count > 0) {
      x.avg = x.score / x.count
    } else {
      x.avg = 0
    }
  })
  return array
}

function avgSort (a, b) {
  if (a.avg > b.avg) {
    return -1
  } else if (a.avg < b.avg) {
    return 1
  }
  return 0
}

function ratingSort (a, b) {
  if (a.data.rating > b.data.rating) {
    return -1
  } else if (a.data.rating < b.data.rating) {
    return 1
  }
  return 0
}

function valueCheck (array, value, rating) {
  let arr = array
  let dict
  arr.forEach(d => {
    let val = d.key
    if (val === value) {
      dict = d
    }
  })
  if (dict !== undefined) {
    dict.count++
    dict.score += rating
  } else {
    arr.push({
      key: value,
      count: 1,
      score: rating,
      avg: 0
    })
  }
  return arr
}

export default {
  data () {
    return {
      mode: this.$route.params.mode,
      pokemon: this.$route.params.pokemon,
      ts: ['normal', 'fire', 'fighting', 'water', 'flying', 'grass', 'poison', 'electric', 'ground', 'psychic', 'rock', 'ice', 'bug', 'dragon', 'ghost', 'dark', 'steel', 'fairy'],
      gs: ['1', '2', '3', '4', '5', '6', '7'],
      cs: ['red', 'blue', 'yellow', 'green', 'black', 'brown', 'purple', 'gray', 'white', 'pink'],
      types: [],
      gens: [],
      colors: [],
      two_stages: [],
      three_stages: [],
      pseudo_lines: [],
      starter_lines: [],
      gens_by_starters: [],
      regional_birds: [],
      regional_rodents: [],
      regional_bugs: [],
      regional_sets: [],
      regional_sets_with_starters: [],
      sortBy: 'ratings',
      onlyShow: {},
      lineSorts: ['two_stages', 'three_stages', 'pseudo_lines', 'starter_lines', 'regional_birds', 'regional_rodents', 'regional_bugs'],
      genSorts: ['gens', 'gens_by_starters', 'regional_sets_with_starters'],
      typeSorts: ['types'],
      genColors: ['red', 'amber', 'green', 'cyan', 'black', 'deep-purple', 'orange'],
      typeColors: {
        normal: 'brown lighten-4',
        fire: 'deep-orange accent-3',
        fighting: 'red darken-4',
        water: 'blue darken-1',
        flying: 'indigo lighten-3',
        grass: 'light-green darken-2',
        poison: 'purple darken-1',
        electric: 'amber darken-1',
        ground: 'orange accent-2',
        psychic: 'pink',
        rock: 'brown',
        ice: 'light-blue lighten-3',
        bug: 'light-green darken-1',
        dragon: 'deep-purple accent-2',
        ghost: 'deep-purple darken-4',
        dark: 'grey darken-4',
        steel: 'blue-grey lighten-3',
        fairy: 'pink lighten-3'
      }
    }
  },
  computed: {
    sortedArray () {
      /* eslint-disable no-eval */
      return eval('this.' + this.sortBy)
    },
    ratings () {
      return this.pokemon.concat().sort(ratingSort)
    }
  },
  mounted () {
    this.process()
  },
  methods: {
    process () {
      // initialize types
      this.ts.forEach(t => {
        this.types.push({
          key: t,
          count: 0,
          score: 0,
          avg: 0
        })
      })
      // initialize gens
      this.gs.forEach(g => {
        this.gens.push({
          key: g,
          count: 0,
          score: 0,
          avg: 0
        })
      })
      // initialize colors
      this.cs.forEach(c => {
        this.colors.push({
          key: c,
          count: 0,
          score: 0,
          avg: 0
        })
      })
      // for each pokemon
      this.pokemon.forEach(mon => {
        mon = mon.data

        // none of this is relevant to mega evolutions
        if (!mon.mega) {
          // extract relevant attributes from current pokemon
          let type1 = mon.types[0]
          let type2
          if (mon.types.length > 1) {
            type2 = mon.types[1]
          }
          let gen = mon.gen
          let color = mon.color
          let rating = mon.rating
          let stages = mon.stages
          let line = mon.line
          let pseudo = mon.pseudo
          let starter = mon.starter
          let regionalBird = mon.regional_bird
          let regionalRodent = mon.regional_rodent
          let regionalBug = mon.regional_bug
          // add in data for current pokemon's type, gen, color
          let typeDict1
          this.types.forEach(t => {
            if (t.key === type1) {
              typeDict1 = t
            }
          })
          let typeDict2
          if (type2) {
            this.types.forEach(t => {
              if (t.key === type2) {
                typeDict2 = t
              }
            })
          }
          let genDict
          this.gens.forEach(g => {
            if (g.key === gen) {
              genDict = g
            }
          })
          let colorDict
          this.colors.forEach(c => {
            if (c.key === color) {
              colorDict = c
            }
          })
          typeDict1.count++
          typeDict1.score += rating
          if (typeDict2) {
            typeDict2.count++
            typeDict2.score += rating
          }
          genDict.count++
          genDict.score += rating
          colorDict.count++
          colorDict.score += rating
          // if pokemon is in a 2-stage line
          if (stages === 2) {
            this.two_stages = valueCheck(this.two_stages, line, rating)
          }
          // if pokemon is in a 3-stage line
          if (stages === 3) {
            this.three_stages = valueCheck(this.three_stages, line, rating)
          }
          // if pokemon is in a pseudo-legendary line
          if (pseudo) {
            this.pseudo_lines = valueCheck(this.pseudo_lines, line, rating)
          }
          // if pokemon is in a starter line
          if (starter) {
            this.starter_lines = valueCheck(this.starter_lines, line, rating)
            this.gens_by_starters = valueCheck(this.gens_by_starters, gen, rating)
            this.regional_sets_with_starters = valueCheck(this.regional_sets_with_starters, gen, rating)
          }
          // if pokemon is in a regional bird line
          if (regionalBird) {
            this.regional_birds = valueCheck(this.regional_birds, line, rating)
            this.regional_sets = valueCheck(this.regional_sets, gen, rating)
            this.regional_sets_with_starters = valueCheck(this.regional_sets_with_starters, gen, rating)
          }
          // if pokemon is in a regional rodent line
          if (regionalRodent) {
            this.regional_rodents = valueCheck(this.regional_rodents, line, rating)
            this.regional_sets = valueCheck(this.regional_sets, gen, rating)
            this.regional_sets_with_starters = valueCheck(this.regional_sets_with_starters, gen, rating)
          }
          // if pokemon is in a regional bug line
          if (regionalBug) {
            this.regional_bugs = valueCheck(this.regional_bugs, line, rating)
            this.regional_sets = valueCheck(this.regional_sets, gen, rating)
            this.regional_sets_with_starters = valueCheck(this.regional_sets_with_starters, gen, rating)
          }
        }
      })
      // set and sort by averages
      this.types = takeAvg(this.types).sort(avgSort)
      this.gens = takeAvg(this.gens).sort(avgSort)
      this.colors = takeAvg(this.colors).sort(avgSort)
      this.two_stages = takeAvg(this.two_stages).sort(avgSort)
      this.three_stages = takeAvg(this.three_stages).sort(avgSort)
      this.pseudo_lines = takeAvg(this.pseudo_lines).sort(avgSort)
      this.starter_lines = takeAvg(this.starter_lines).sort(avgSort)
      this.gens_by_starters = takeAvg(this.gens_by_starters).sort(avgSort)
      this.regional_birds = takeAvg(this.regional_birds).sort(avgSort)
      this.regional_rodents = takeAvg(this.regional_rodents).sort(avgSort)
      this.regional_bugs = takeAvg(this.regional_bugs).sort(avgSort)
      this.regional_sets = takeAvg(this.regional_sets).sort(avgSort)
      this.regional_sets_with_starters = takeAvg(this.regional_sets_with_starters).sort(avgSort)
    },
    numToText (n) {
      if (n === 1) {
        if (this.mode === 'spec') {
          return 'Hate'
        } else {
          return '1'
        }
      } else if (n === 2) {
        return '2'
      } else if (n === 3) {
        if (this.mode === 'spec' || this.mode === 'like') {
          return 'Dislike'
        } else {
          return '3'
        }
      } else if (n === 4) {
        return '4'
      } else if (n === 5) {
        if (this.mode === 'spec') {
          return 'Neutral'
        } else {
          return '5'
        }
      } else if (n === 6) {
        return '6'
      } else if (n === 7) {
        if (this.mode === 'spec' || this.mode === 'like') {
          return 'Like'
        } else {
          return '7'
        }
      } else if (n === 8) {
        return '8'
      } else if (n === 9) {
        if (this.mode === 'spec') {
          return 'Love'
        } else {
          return '8'
        }
      } else if (n === 10) {
        return '10'
      }
    },
    changeSort (s = 'ratings', o = {}) {
      this.sortBy = s
      this.onlyShow = o
    },
    allowed (mon) {
      let al = true
      const keys = Object.keys(this.onlyShow)
      keys.forEach(key => {
        if (key !== 'types') {
          if (mon[key] !== this.onlyShow[key]) {
            al = false
          }
        } else {
          if (mon[key][0] !== this.onlyShow[key] && mon[key][1] !== this.onlyShow[key]) {
            al = false
          }
        }
      })
      return al
    }
  },
  beforeRouteLeave (to, from, next) {
    const answer = window.confirm(
      'If leave this page and you have not saved your PokePallet, you cannot get it back. Are you sure you want to leave?'
    )
    if (answer) {
      next()
    } else {
      next(false)
    }
  }
}
</script>

<style scoped>
</style>
