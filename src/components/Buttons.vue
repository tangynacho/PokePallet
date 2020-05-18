<template>
  <span v-if="expanded">
    <span v-for="(c, n) in colorsList" :key="n">
      <v-btn icon :color="c" class="white--text" @click="next(n + 1)">
        {{ n + 1 }}
      </v-btn>
    </span>
  </span>
  <span v-else>
    <v-btn icon :color="color" class="white--text" @click="change()">{{
      rating
    }}</v-btn>
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
    },
    id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      expanded: false
    };
  },
  computed: {
    colorsList() {
      let l = new Array(10).fill("grey darken-1");
      l[this.rating - 1] = this.color;
      return l;
    }
  },
  methods: {
    toggle() {
      this.expanded = !this.expanded;
    },
    change() {
      this.$emit("i", this.id);
      this.toggle();
    },
    next(n) {
      this.$emit("n", n);
      this.toggle();
    }
  }
};
</script>

<style scoped></style>
