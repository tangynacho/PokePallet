<template>
  <div id="app">
    <topbar/>
    <router-view/>
  </div>
</template>

<script>
import Topbar from '@/components/Topbar.vue'
export default {
  name: 'App',
  components: {
    Topbar
  }
}
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #eeeeee;
  background-color: #333333;
  height: 100vh;
}
</style>
