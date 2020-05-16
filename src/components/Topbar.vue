<template>
  <div class="colored">
    <p class="title text-xs-left ml-2 py-3">
      <input name="home" id="home" class="inputfile" />
      <label title="Return to Homepage" for="home" @click="$router.push({ name: 'Home' })">HOME</label>
      <input name="save" id="save" class="inputfile" />
      <label title="Save Your PokePallet" for="save" @click="save">SAVE</label>
      <input type="file" accept=".json" name="load" id="load" class="inputfile" />
      <label title="Load A PokePallet" for="load">LOAD</label>
    </p>
  </div>
</template>

<script>
/* eslint-disable */
let pokemonJSON = require("@/data/pokemon.json");

function saveJSON () {
  let text = JSON.stringify(pokemonJSON);
  var a = document.createElement("a");
  a.setAttribute(
    "href",
    "data:text/plain;charset=utf-8," + encodeURIComponent(text)
  );
  a.setAttribute("download", "pokepallet.json");
  a.click();
}

export default {
  name: "Topbar",
  methods: {
    save () {
      saveJSON();
    },
    load (pokemon) {
      this.$router.push({
        name: "Ratings",
        params: {
          pokemon
        }
      });
    }
  },
  mounted () {
    let fileSelector = document.getElementById("load");
    if (fileSelector) {
      fileSelector.addEventListener("change", event => {
        let file = fileSelector.files[0];
        let reader = new FileReader();
        reader.onload = e => {
          let pokemonJSON = JSON.parse(e.target.result);
          // turns the Object into an array of Objects
          let pokemon = Object.keys(pokemonJSON).map(function (key) {
            return { id: key, data: pokemonJSON[key] };
          });
          // sorts the array by id number
          pokemon.sort(function (x, y) {
            if (x.id < y.id) {
              return -1;
            }
            if (x.id > y.id) {
              return 1;
            }
            return 0;
          });
          this.load(pokemon)
        };
        reader.readAsText(file);
      });
    }
  }
};
</script>

<style scoped>
.colored {
  background-color: #555555;
}
.inputfile {
  opacity: 0;
  overflow: hidden;
  position: absolute;
  z-index: -1;
}

.inputfile + label {
  cursor: pointer;
  font-weight: bold;
  padding-left: 20px;
  padding-right: 30px;
}
</style>
