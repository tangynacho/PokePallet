<template>
  <v-container fluid>
    <v-layout justify-center mb-4>
      <v-btn color="red" class="white--text" @click="changeSort('types')">TYPES</v-btn>
      <v-btn color="green" class="white--text" @click="changeSort('gens')">GENS</v-btn>
      <v-btn color="blue" class="white--text" @click="changeSort('colors')">COLORS</v-btn>
      <v-btn color="yellow" class="white--text" @click="changeSort('starter_lines')">STARTERS</v-btn>
    </v-layout>
    <v-layout justify-center>
      <v-flex xs6>
        <v-card v-if="sortBy === 'rating'">
          <v-card-text
            v-for="mon in pokemon"
            :key="mon.data.name"
            class="title text-xs-left"
          >{{ mon.data.name }}: {{ numToText(mon.data.rating) }}</v-card-text>
        </v-card>
        <v-card v-else-if="sortBy === 'starter_lines'">
          <v-card-text
            v-for="x in sortedArray"
            :key="sortedArray.indexOf(x)"
            class="title text-xs-left"
          >
            <span v-for="mon in pokemon" :key="mon.id">
              <span v-if="mon.id === x.key">{{ mon.data.name }}: {{ x.avg }}</span>
            </span>
          </v-card-text>
        </v-card>
        <v-card v-else>
          <v-card-text
            v-for="x in sortedArray"
            :key="sortedArray.indexOf(x)"
            class="title text-xs-left"
          >{{ x.key }}: {{ x.avg }}</v-card-text>
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

function valueCheck (array, value, v, rating) {
  let dict
  array.forEach(d => {
    let val
    if (value === 'line') {
      val = d.line
    } else if (value === 'gen') {
      val = d.gen
    }
    if (val === v) {
      dict = d
    }
  })
  if (dict) {
    dict.count++
    dict.score += rating
  } else {
    array.push({
      key: v,
      count: 1,
      score: rating,
      avg: 0
    })
  }
  return array
}

export default {
  data () {
    return {
      mode: this.$route.params.mode,
      pokemon: this.$route.params.pokemon,
      sortBy: 'rating',
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
      regional_sets_with_starters: []
    }
  },
  computed: {
    sortedArray () {
      /* eslint-disable no-eval */
      return eval('this.' + this.sortBy)
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
            this.two_stages = valueCheck(this.two_stages, 'line', line, rating)
          }
          // if pokemon is in a 3-stage line
          if (stages === 3) {
            this.three_stages = valueCheck(this.three_stages, 'line', line, rating)
          }
          // if pokemon is in a pseudo-legendary line
          if (pseudo) {
            this.pseudo_lines = valueCheck(this.pseudo_lines, 'line', line, rating)
          }
          // if pokemon is in a starter line
          if (starter) {
            console.log(this.starter_lines)
            this.starter_lines = valueCheck(this.starter_lines, 'line', line, rating)
            console.log(this.starter_lines)
            this.gens_by_starters = valueCheck(this.gens_by_starters, 'gen', gen, rating)
            this.regional_sets_with_starters = valueCheck(this.regional_sets_with_starters, 'gen', gen, rating)
          }
          // if pokemon is in a regional bird line
          if (regionalBird) {
            this.regional_birds = valueCheck(this.regional_birds, 'line', line, rating)
            this.regional_sets = valueCheck(this.regional_sets, 'gen', gen, rating)
            this.regional_sets_with_starters = valueCheck(this.regional_sets_with_starters, 'gen', gen, rating)
          }
          // if pokemon is in a regional rodent line
          if (regionalRodent) {
            this.regional_rodents = valueCheck(this.regional_rodents, 'line', line, rating)
            this.regional_sets = valueCheck(this.regional_sets, 'gen', gen, rating)
            this.regional_sets_with_starters = valueCheck(this.regional_sets_with_starters, 'gen', gen, rating)
          }
          // if pokemon is in a regional bug line
          if (regionalBug) {
            this.regional_bugs = valueCheck(this.regional_bugs, 'line', line, rating)
            this.regional_sets = valueCheck(this.regional_sets, 'gen', gen, rating)
            this.regional_sets_with_starters = valueCheck(this.regional_sets_with_starters, 'gen', gen, rating)
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
    changeSort (s) {
      this.sortBy = s
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
