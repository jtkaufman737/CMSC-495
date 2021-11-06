<template>
  <div class="boardlist">
    <h5 class="text-center">Explore Fault Tree Analysis boards</h5>
    <table>
      <tr class="row">
        <th class="col">Name</th>
        <th class="col">Description</th>
      </tr>
      <tr v-for="board in boardList" :key="board.id" class="row">
        <td class="col"><a @click="runNav(board.id)">{{ board.name }}</a></td>
        <td class="col">{{ board.description }}</td>
      </tr>
    </table>
  </div>
</template>
<script>
export default {
  name: 'BoardList',
  data() {
    return {
      boardList:[
        { id: 1, name: "test 1", description: "test 1"},
        { id: 2, name: "test 2", description: "test 2"},
        { id: 3, name: "test 3", description: "test 3"},
        { id: 4, name: "test 4", description: "test 4"},
        { id: 5, name: "test 5", description: "test 5"},
        { id: 6, name: "test 6", description: "test 6"},
        { id: 7, name: "test 7", description: "test 7"},
      ]
    }
  },
  methods:{
    runNav(id) {
      console.log("Run nav running!")
      this.$router.push(`board/${id}`)
    }
  }
}
</script>
<style>
div.boardlist {
  margin:2em;
  padding:0 5% 0 5%;
}

.col {
  min-width:200px;
}

.col td {
  margin-left:10px;
}

a:hover {
  cursor: pointer;
}
</style>
