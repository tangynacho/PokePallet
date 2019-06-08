<template>
  <v-container fluid>
    <v-layout justify-center>
      <v-flex xs6>
        <p class="display-2">Welcome to PokePallet!</p>
        <ul class="headline text-xs-left">
          <li>You'll be presented with each and every pokemon in existence, one at a time.</li>
          <li>Then, you'll give that pokemon a rating and move on to the next one.</li>
          <li>Once you have rated all of the pokemon, you can see a whole bunch of stats about your preference in pokemon. Things like which generation you like the best, your favorite types, your preferred egg group, and much more!</li>
          <li>If you don't have time to rate every pokemon in one sitting, you can save your progress and finish later.</li>
          <li>At the end, you'll be able to download your very own PokePallet with all your stats to share and compare with friends!</li>
        </ul>
        <p class="display-1 mt-4">To get started, choose a rating system below:</p>
        <p class="headline text-xs-left">
          <v-btn color="red" class="white--text font-weight-bold" :to="'/newpage'">LIKE / DISLIKE</v-btn>Simply like or dislike each pokemon.
        </p>
        <p class="headline text-xs-left">
          <v-btn color="green" class="white--text font-weight-bold" :to="'/newpage'">INDIFFERECE</v-btn>Allow indifference and semi-like ratings.
        </p>
        <p class="headline text-xs-left">
          <v-btn color="blue" class="white--text font-weight-bold" :to="'/newpage'">TEN-SCALE</v-btn>Rate each pokemon on a scale from 1 to 10.
        </p>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: "Home"
};
</script>

<style scoped>
</style>
