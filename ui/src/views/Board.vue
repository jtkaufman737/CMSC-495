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
        userZoomingEnabled: false,
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
              'shape': 'round-rectangle',
              'border-width':'20px',
              'border-style':'solid',
              'border-color':'#104cfb',
              'border-opacity':'0.5',
              'background-color':'white',
              'height': '400px',
              'width': '400px',
              'label': 'data(description)',
              'text-wrap': 'wrap',
              'text-halign': 'center',
              'text-valign': 'center',
              'padding':'15px',
              'font-family':'-apple-system,BlinkMacSystemFont,Avenir,"Avenir Next","Segoe UI",Roboto,Oxygen,Ubuntu,Cantarell,"Fira Sans","Droid Sans","Helvetica Neue",sans-serif',
              'font-size':'3.5em',
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