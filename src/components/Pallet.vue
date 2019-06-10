<template>
  <v-container fluid>
    <v-layout justify-center>
      <v-flex xs6>
          <v-card>
            <v-card-text v-for="mon in pokemon" :key="mon.name" class="headline text-xs-left">
                {{mon.name}}: {{numToText(mon.rating)}}
                </v-card-text>
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
            pokemon: this.$route.params.pokemon
        }
    },
    methods: {
        numToText(n) {
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
    beforeRouteLeave (to, from , next) {
    const answer = window.confirm('If leave this page and you have not saved your PokePallet, you cannot get it back. Are you sure you want to leave?')
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
