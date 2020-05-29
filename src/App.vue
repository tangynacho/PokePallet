<template>
  <div id="app" class="fill-screen">
    <topbar />
    <router-view />
    <footbar class="bottom" />
  </div>
</template>

<script>
/* eslint-disable */
import Topbar from "@/components/Topbar.vue";
import Footbar from "@/components/Footbar.vue";
export default {
  name: "App",
  components: {
    Topbar,
    Footbar
  }
};
</script>

<style>
.fill-screen {
  min-height: 100vh;
}
.bottom {
  position: fixed;
  bottom: 0px;
  right: 0px;
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
