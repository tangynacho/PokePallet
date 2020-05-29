<template>
  <div id="app" class="fill-screen">
    <topbar />
    <router-view />
  </div>
</template>

<script>
/* eslint-disable */
import Topbar from "@/components/Topbar.vue";
export default {
  name: "App",
  components: {
    Topbar
  }
};
</script>

<style>
.fill-screen {
  min-height: 100vh;
}
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #eeeeee;
  background-color: #333333;
  height: 100%;
}
</style>
