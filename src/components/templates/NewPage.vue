<template>
  <div>
    <p class="display-1">New Page</p>
    <router-link v-bind:to="'/'">Home</router-link>
  </div>
</template>

<script>
export default {
  name: "NewPage",
  data() {
    return {
      var: "val"
    };
  }
};
</script>

<style scoped>
</style>