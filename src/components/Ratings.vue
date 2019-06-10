<template>
  <v-container fluid>
    <v-layout justify-center>
      <v-flex xs6>
        <v-card  v-animate-css="'fadeInDown'">
            <v-img :src="require(`@/assets/images/${current.name}.png`)" :max-width="w/4" class="center"/>
        </v-card>
        <p class="display-1 mt-3" v-animate-css="'fadeInDown'">#{{currentID}} {{current.name}}</p>
        <v-layout justify-center>
          <v-btn color="green" class="white--text" @click="next(1)">LIKE</v-btn>
        </v-layout>
        <router-link v-bind:to="'/'">Home</router-link>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
const mon = (name, types, gen, stage, stages, relations, color, eggs, mega, alolan, starter, regional, legendary, mythical, pseudo, baby, rating) => ({name, types, gen, stage, stages, relations, color, eggs, mega, alolan, starter, regional, legendary, mythical, pseudo, baby, rating})

export default {
  name: 'Ratings',
  data () {
    return {
      mode: this.$route.params.mode,
      i: 0,
      h: window.innerHeight,
      w: window.innerWidth,
      pokemon: {
        '001': mon('Bulbasaur', ['grass', 'poison'], 1, 1, 3, ['002', '003', '003m'], 'green', ['monster', 'grass'], false, false, true, [false, false, false], false, false, false, false, 0),
        '002': mon('Ivysaur', ['grass', 'poison'], 1, 2, 3, ['001', '003', '003m'], 'green', ['monster', 'grass'], false, false, true, [false, false, false], false, false, false, false, 0),
        '003': mon('Venusaur', ['grass', 'poison'], 1, 3, 3, ['001', '002', '003m'], 'green', ['monster', 'grass'], false, false, true, [false, false, false], false, false, false, false, 0),
        '003m': mon('Mega Venusaur', ['grass', 'poison'], 1, 4, 3, ['001', '002', '003'], 'green', ['monster', 'grass'], true, false, true, [false, false, false], false, false, false, false, 0),
        '004': mon('Charmander', ['fire', 'fire'], 1, 1, 3, ['005', '006', '006mx', '006my'], 'red', ['monster', 'dragon'], false, false, true, [false, false, false], false, false, false, false, 0),
        '005': mon('Charmeleon', ['fire', 'fire'], 1, 2, 3, ['004', '006', '006mx', '006my'], 'red', ['monster', 'dragon'], false, false, true, [false, false, false], false, false, false, false, 0),
        '006': mon('Charizard', ['fire', 'flying'], 1, 3, 3, ['004', '005', '006mx', '006my'], 'red', ['monster', 'dragon'], false, false, true, [false, false, false], false, false, false, false, 0),
        '006mx': mon('Mega Charizard X', ['fire', 'dragon'], 1, 4, 3, ['004', '005', '006'], 'red', ['monster', 'dragon'], true, false, true, [false, false, false], false, false, false, false, 0),
        '006my': mon('Mega Charizard Y', ['fire', 'flying'], 1, 4, 3, ['004', '005', '006'], 'red', ['monster', 'dragon'], true, false, true, [false, false, false], false, false, false, false, 0),
        '007': mon('Squirtle', ['water', 'water'], 1, 1, 3, ['008', '009', '009m'], 'blue', ['monster', 'water 1'], false, false, true, [false, false, false], false, false, false, false, 0),
        '008': mon('Wartortle', ['water', 'water'], 1, 2, 3, ['007', '009', '009m'], 'blue', ['monster', 'water 1'], false, false, true, [false, false, false], false, false, false, false, 0),
        '009': mon('Blastoise', ['water', 'water'], 1, 3, 3, ['007', '008', '009m'], 'blue', ['monster', 'water 1'], false, false, true, [false, false, false], false, false, false, false, 0),
        '009m': mon('Mega Blastoise', ['water', 'water'], 1, 4, 3, ['007', '008', '009'], 'blue', ['monster', 'water 1'], true, false, true, [false, false, false], false, false, false, false, 0),
        '010': mon('Caterpie', ['bug', 'bug'], 1, 1, 3, ['011', '012'], 'green', ['bug'], false, false, false, [false, true, false], false, false, false, false, 0)
      }
    }
  },
  computed: {
    currentID () {
      return Object.keys(this.pokemon)[this.i]
    },
    current () {
      return this.pokemon[this.currentID]
    }
  },
  methods: {
    next (r) {
      this.current.rating = r
      if ((this.i + 1) < Object.keys(this.pokemon).length) {
        this.i++
      } else {
        this.$router.push({name: 'Pallet', params: { mode: this.mode, pokemon: this.pokemon }})
      }
    }
  }
}
</script>

<style scoped>
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>
