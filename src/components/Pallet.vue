<template>
  <v-container fluid>
    <v-layout justify-center>
      <v-flex xs6>
        <v-card>
          <v-card-text
            v-for="mon in pokemon"
            :key="mon.data.name"
            class="title text-xs-left"
          >{{ mon.data.name }}: {{ numToText(mon.data.rating) }}</v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data () {
    return {
      mode: this.$route.params.mode,
      pokemon: this.$route.params.pokemon,
      ts: ['normal', 'fire', 'fighting', 'water', 'flying', 'grass', 'poison', 'electric', 'ground', 'psychic', 'rock', 'ice', 'bug', 'dragon', 'ghost', 'dark', 'steel', 'fairy'],
      gs: ['1', '2', '3', '4', '5', '6', '7'],
      cs: ['red', 'blue', 'yellow', 'green', 'black', 'brown', 'purple', 'gray', 'white', 'pink'],
      types: {},
      gens: {},
      colors: {},
      two_stages: {},
      three_stages: {},
      pseudo_lines: {},
      starter_lines: {},
      gens_by_starters: {},
      regional_birds: {},
      regional_rodents: {},
      regional_bugs: {},
      regional_sets: {},
      regional_sets_with_starters: {}
    }
  },
  mounted () {
    this.process()
  },
  methods: {
    process () {
      // initialize types
      this.ts.foreach(t => {
        this.types[t] = {
          count: 0,
          score: 0,
          avg: 0
        }
      })
      // initialize gens
      this.gs.foreach(g => {
        this.gens[g] = {
          count: 0,
          score: 0,
          avg: 0
        }
      })
      // initialize colors
      this.cs.foreach(c => {
        this.colors[c] = {
          count: 0,
          score: 0,
          avg: 0
        }
      })
      // for each pokemon
      this.pokemon.foreach(mon => {
        // none of this is relevant to mega evolutions
        if (!mon.mega) {
          // extract relevant attributes from current pokemon
          let type = mon.type
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
          this.types[type].count++
          this.types[type].score += rating
          this.gens[gen].count++
          this.gens[gen].score += rating
          this.colors[color].count++
          this.colors[color].score += rating
          // if pokemon is in a 2-stage line
          if (stages === 2) {
            if (line in this.two_stages) {
              this.two_stages[line].count++
              this.two_stages[line].score += rating
            } else {
              this.two_stages[line] = {
                count: 0,
                score: 0,
                avg: 0
              }
            }
          }
          // if pokemon is in a 3-stage line
          if (stages === 3) {
            if (line in this.three_stages) {
              this.three_stages[line].count++
              this.three_stages[line].score += rating
            } else {
              this.three_stages[line] = {
                count: 0,
                score: 0,
                avg: 0
              }
            }
          }
          // if pokemon is in a pseudo-legendary line
          if (pseudo) {
            if (line in this.pseudo_lines) {
              this.pseudo_lines[line].count++
              this.pseudo_lines[line].score += rating
            } else {
              this.pseudo_lines[line] = {
                count: 0,
                score: 0,
                avg: 0
              }
            }
          }
          // if pokemon is in a starter line
          if (starter) {
            if (line in this.starter_lines) {
              this.starter_lines[line].count++
              this.starter_lines[line].score += rating
            } else {
              this.starter_lines[line] = {
                count: 0,
                score: 0,
                avg: 0
              }
            }
            if (gen in this.gens_by_starters) {
              this.gens_by_starters[gen].count++
              this.gens_by_starters[gen].score += rating
            } else {
              this.gens_by_starters[gen] = {
                count: 0,
                score: 0,
                avg: 0
              }
            }
            if (gen in this.regional_set_with_starters) {
              this.regional_set_with_starters[gen].count++
              this.regional_set_with_starters[gen].score += rating
            } else {
              this.regional_set_with_starters[gen] = {
                count: 0,
                score: 0,
                avg: 0
              }
            }
          }
          // if pokemon is in a regional bird line
          if (regionalBird) {
            if (line in this.regional_birds) {
              this.regional_birds[line].count++
              this.regional_birds[line].score += rating
            } else {
              this.regional_birds[line] = {
                count: 0,
                score: 0,
                avg: 0
              }
            }
            if (gen in this.regional_sets) {
              this.regional_sets[gen].count++
              this.regional_sets[gen].score += rating
            } else {
              this.regional_sets[gen] = {
                count: 0,
                score: 0,
                avg: 0
              }
            }
            if (gen in this.regional_set_with_starters) {
              this.regional_set_with_starters[gen].count++
              this.regional_set_with_starters[gen].score += rating
            } else {
              this.regional_set_with_starters[gen] = {
                count: 0,
                score: 0,
                avg: 0
              }
            }
          }
          // if pokemon is in a regional rodent line
          if (regionalRodent) {
            if (line in this.regional_rodents) {
              this.regional_rodents[line].count++
              this.regional_rodents[line].score += rating
            } else {
              this.regional_rodents[line] = {
                count: 0,
                score: 0,
                avg: 0
              }
            }
            if (gen in this.regional_sets) {
              this.regional_sets[gen].count++
              this.regional_sets[gen].score += rating
            } else {
              this.regional_sets[gen] = {
                count: 0,
                score: 0,
                avg: 0
              }
            }
            if (gen in this.regional_set_with_starters) {
              this.regional_set_with_starters[gen].count++
              this.regional_set_with_starters[gen].score += rating
            } else {
              this.regional_set_with_starters[gen] = {
                count: 0,
                score: 0,
                avg: 0
              }
            }
          }
          // if pokemon is in a regional bug line
          if (regionalBug) {
            if (line in this.regional_bugs) {
              this.regional_bugs[line].count++
              this.regional_bugs[line].score += rating
            } else {
              this.regional_bugs[line] = {
                count: 0,
                score: 0,
                avg: 0
              }
            }
            if (gen in this.regional_sets) {
              this.regional_sets[gen].count++
              this.regional_sets[gen].score += rating
            } else {
              this.regional_sets[gen] = {
                count: 0,
                score: 0,
                avg: 0
              }
            }
            if (gen in this.regional_set_with_starters) {
              this.regional_set_with_starters[gen].count++
              this.regional_set_with_starters[gen].score += rating
            } else {
              this.regional_set_with_starters[gen] = {
                count: 0,
                score: 0,
                avg: 0
              }
            }
          }
          // set averages
          this.types.foreach(x => {
            x.avg = x.score / x.count
          })
          this.gens.foreach(x => {
            x.avg = x.score / x.count
          })
          this.colors.foreach(x => {
            x.avg = x.score / x.count
          })
          this.two_stages.foreach(x => {
            x.avg = x.score / x.count
          })
          this.three_stages.foreach(x => {
            x.avg = x.score / x.count
          })
          this.pseudo_lines.foreach(x => {
            x.avg = x.score / x.count
          })
          this.starter_lines.foreach(x => {
            x.avg = x.score / x.count
          })
          this.gens_by_starters.foreach(x => {
            x.avg = x.score / x.count
          })
          this.regional_birds.foreach(x => {
            x.avg = x.score / x.count
          })
          this.regional_rodents.foreach(x => {
            x.avg = x.score / x.count
          })
          this.regional_bugs.foreach(x => {
            x.avg = x.score / x.count
          })
          this.regional_sets.foreach(x => {
            x.avg = x.score / x.count
          })
          this.regional_sets_with_starters.foreach(x => {
            x.avg = x.score / x.count
          })
        }
      })
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
