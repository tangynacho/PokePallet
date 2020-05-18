<template>
  <span>
    <span v-for="(c, n) in colorsList" :key="n">
      <v-btn icon :color="c" class="white--text" @click="next(n + 1)">
        {{ n + 1 }}
      </v-btn>
    </span>
  </span>
</template>

<script>
/* eslint-disable */
export default {
  name: "Buttons",
  props: {
    rating: {
      type: Number,
      required: true
    },
    color: {
      type: String,
      required: true
    }
  },
  computed: {
    colorsList() {
      let l = new Array(10).fill("grey darken-1");
      l[this.rating - 1] = this.color;
      console.log(l);
      return l;
    }
  },
  methods: {
    next(n) {
      this.$emit("n", n);
    }
  }
};
</script>

<style scoped></style>
