<template>
  <div class="colored">
    <p class="title text-xs-left ml-2 py-3">
      <input name="home" id="home" class="inputfile" />
      <label
        title="Return to Homepage"
        for="home"
        @click="$router.push({ name: 'Home' })"
        >HOME</label
      >
      <input name="save" id="save" class="inputfile" />
      <label title="Save Your PokePallet" for="save" @click="save">SAVE</label>
      <input
        type="file"
        accept=".json"
        name="load"
        id="load"
        class="inputfile"
      />
      <label title="Load A PokePallet" for="load">LOAD</label>
    </p>
  </div>
</template>

<script>
/* eslint-disable */

// loads the json file
let pokemonJSON = require("@/data/pokemon.json");
// turns the Object into an array of Objects
let pokemon = Object.keys(pokemonJSON).map(function(key) {
  return { id: key, data: pokemonJSON[key] };
});
// sorts the array by id number
pokemon.sort(function(x, y) {
  if (x.id < y.id) {
    return -1;
  }
  if (x.id > y.id) {
    return 1;
  }
  return 0;
});

function saveJSON(pokemon) {
  let pokemonJSON = {};
  pokemon.forEach(mon => {
    pokemonJSON[mon.id] = mon.data;
  });
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
  data() {
    return {
      pokemon: pokemon
    };
  },
  methods: {
    save() {
      saveJSON(this.pokemon);
    },
    load(newPokemon) {
      for (let pok of this.pokemon) {
        let hasit = false;
        for (let mon of newPokemon) {
          if (mon.id === pok.id) {
            hasit = true;
            for (let key in pok.data) {
              if (key !== "rating") {
                mon.data[key] = pok.data[key];
              }
            }
            break;
          }
        }
        if (!hasit) {
          newPokemon.push({
            id: pok.id,
            data: pok.data
          });
        }
      }
      newPokemon.sort(function(x, y) {
        if (x.id < y.id) {
          return -1;
        }
        if (x.id > y.id) {
          return 1;
        }
        return 0;
      });
      this.pokemon = newPokemon;
      this.$router.push({
        name: "Ratings",
        params: {
          pokemon: newPokemon
        }
      });
    }
  },
  mounted() {
    let fileSelector = document.getElementById("load");
    if (fileSelector) {
      fileSelector.addEventListener("change", event => {
        let file = fileSelector.files[0];
        let reader = new FileReader();
        reader.onload = e => {
          let pokemonJSON = JSON.parse(e.target.result);
          // turns the Object into an array of Objects
          let pokemon = Object.keys(pokemonJSON).map(function(key) {
            return { id: key, data: pokemonJSON[key] };
          });
          // sorts the array by id number
          pokemon.sort(function(x, y) {
            if (x.id < y.id) {
              return -1;
            }
            if (x.id > y.id) {
              return 1;
            }
            return 0;
          });
          this.load(pokemon);
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
  z-index: -1;
  width: 0px;
}

.inputfile + label {
  cursor: pointer;
  font-weight: bold;
  padding-left: 20px;
  padding-right: 30px;
}
</style>
