<template>
  <div class="board">
    <h5 class="text-center">{{ board.name }}</h5>
    <h6 class="text-center">{{ board.description }}</h6>
    <div id="cy"></div>
  </div>
</template>

<script>
import cy from 'cytoscape';
import Symbol from '@/components/Symbol.vue'

export default {
  name: 'Board',
  data () {
    return {
      cytoscape: null,
      board: { name: "Test board", description: "testing 1 2 1 2", id: 1 },
      edges: [
        { id: 1, start: 1, end: 2 },
        { id: 2, start: 2, end: 3}
      ],
      nodes: [
        { id: 1, type: "Gate - and", description: "chrome and firefox"},
        { id: 2, type: "Event - basic", description: "500 message from server"},
        { id: 3, type: "Gate - or", description: "browser crash"}
      ]
    }
  },
  components: {
    Symbol
  },
  methods: {
    buildTree() {
      const cytoscape = cy({
        container: document.getElementById("cy"),
        elements: [
          {  
            data: { id: "a", type: "Event/intermediate", description: "Navigate to /about"}
          },
          {  
            data: { id: "b", type: "Gate/and", description:"Browser cache not cleared"}
          },
          {
            data: { id: "c", type: "Event/basic", description:"Error message displays"}
          },
          {
            data: { id: "d", type: "Transfer", description: "Transfer to separate tree"}
          },
          {  
            data: { id: "ab", source: "a", target: "b" }
          },
          {
            data: { id: "bc", source: "b", target: "c" }
          }, 
          {
            data: { id: "bd", source: "b", target: "d" }
          }
        ],
        layout: {
          name: 'breadthfirst',
          directed: 'true'
        },
        style: [ // the stylesheet for the graph
          {
            selector: 'node',
            style: {
              'height': '200px',
              'width': '200px',
              'label': 'data(description)'
            }
          },
        ]
      })
    }
  },
  mounted() {
    this.buildTree()
  }
}
</script>
<style scoped>
div#cy {
  min-height:600px;
}
</style>