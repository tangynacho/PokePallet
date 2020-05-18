<template>
  <v-container fluid>
    <v-layout justify-center>
      <p class="display-1">Loading...</p>
    </v-layout>
  </v-container>
</template>

<script>
/* eslint-disable */
export default {
  name: "Loader",
  data() {
    return {
      pokemon: this.$route.params.pokemon,
      destination: this.$route.params.destination
    };
  },
  mounted() {
    this.$router.push({
      name: this.destination,
      params: {
        pokemon: this.pokemon
      }
    });
  }
};
</script>

<style scoped></style>
