<template>
  <div class="colored pt-3 pb-1">
    <p class="title text-xs-left ml-4">
      <v-icon color="white">mdi-floppy</v-icon>Save
    </p>
  </div>
</template>

<script>
export default {
  name: "Topbar",
  data() {
    return {
      var: "val"
    };
  }
};
</script>

<style scoped>
.colored {
  background-color: #555555;
}
</style>