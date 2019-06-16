const mon = (name, types, gen, stage, stages, relations, color, eggs, mega, alolan, starter, regional, legendary, mythical, pseudo, baby, rating) => ({name, types, gen, stage, stages, relations, color, eggs, mega, alolan, starter, regional, legendary, mythical, pseudo, baby, rating})

export default {
  name: 'Ratings',
  data () {
    return {
      mode: (this.$route.params.mode) ? this.$route.params.mode : 'like',
      i: 0,
      h: window.innerHeight,
      w: window.innerWidth,
      waited: false,
      pokemon: {
        '001': mon('Bulbasaur', ['grass', 'poison'], 1, 1, 3, ['002', '003', '003m'], 'green', ['monster', 'grass'], false, false, true, [false, false, false], false, false, false, false, 0),
        '002': mon('Ivysaur', ['grass', 'poison'], 1, 2, 3, ['001', '003', '003m'], 'green', ['monster', 'grass'], false, false, true, [false, false, false], false, false, false, false, 0),
        '003': mon('Venusaur', ['grass', 'poison'], 1, 3, 3, ['001', '002', '003m'], 'green', ['monster', 'grass'], false, false, true, [false, false, false], false, false, false, false, 0),
        '003m': mon('Mega Venusaur', ['grass', 'poison'], 1, 4, 3, ['001', '002', '003'], 'green', ['monster', 'grass'], true, false, true, [false, false, false], false, false, false, false, 0),
        '004': mon('Charmander', ['fire', 'fire'], 1, 1, 3, ['005', '006', '006mx', '006my'], 'red', ['monster', 'dragon'], false, false, true, [false, false, false], false, false, false, false, 0),
        '005': mon('Charmeleon', ['fire', 'fire'], 1, 2, 3, ['004', '006', '006mx', '006my'], 'red', ['monster', 'dragon'], false, false, true, [false, false, false], false, false, false, false, 0),
        '006': mon('Charizard', ['fire', 'flying'], 1, 3, 3, ['004', '005', '006mx', '006my'], 'red', ['monster', 'dragon'], false, false, true, [false, false, false], false, false, false, false, 0),
        '006mx': mon('Mega Charizard X', ['fire', 'dragon'], 1, 4, 3, ['004', '005', '006'], 'red', ['monster', 'dragon'], true, false, true, [false, false, false], false, false, false, false, 0),
        '006my': mon('Mega Charizard Y', ['fire', 'flying'], 1, 4, 3, ['004', '005', '006'], 'red', ['monster', 'dragon'], true, false, true, [false, false, false], false, false, false, false, 0),
        '007': mon('Squirtle', ['water', 'water'], 1, 1, 3, ['008', '009', '009m'], 'blue', ['monster', 'water 1'], false, false, true, [false, false, false], false, false, false, false, 0),
        '008': mon('Wartortle', ['water', 'water'], 1, 2, 3, ['007', '009', '009m'], 'blue', ['monster', 'water 1'], false, false, true, [false, false, false], false, false, false, false, 0),
        '009': mon('Blastoise', ['water', 'water'], 1, 3, 3, ['007', '008', '009m'], 'blue', ['monster', 'water 1'], false, false, true, [false, false, false], false, false, false, false, 0),
        '009m': mon('Mega Blastoise', ['water', 'water'], 1, 4, 3, ['007', '008', '009'], 'blue', ['monster', 'water 1'], true, false, true, [false, false, false], false, false, false, false, 0),
        '010': mon('Caterpie', ['bug', 'bug'], 1, 1, 3, ['011', '012'], 'green', ['bug'], false, false, false, [false, true, false], false, false, false, false, 0)
      }
    }
  },
}
