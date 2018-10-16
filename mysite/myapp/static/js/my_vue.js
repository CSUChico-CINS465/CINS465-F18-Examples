// var app = new Vue({
//   el: '#app',
//   data: {
//     message: 'Hello Vue!'
//   }
// })
//
// var app2 = new Vue({
//   el: '#app-2',
//   data: {
//     message: 'You loaded this page on ' + new Date().toLocaleString()
//   }
// })
//
// var app3 = new Vue({
//   el: '#app-3',
//   data: {
//     seen: true
//   }
// })

// var app4 = new Vue({
//   el: '#app-4',
//   data: {
//     todos: [
//       { text: 'Learn JavaScript' },
//       { text: 'Learn Vue' },
//       { text: 'Build something awesome' }
//     ]
//   }
// })
var app4 = new Vue({
  el: '#app-4',
  data: {
    suggestions: []
  },
  //Adapted from https://stackoverflow.com/questions/36572540/vue-js-auto-reload-refresh-data-with-timer
  created: function() {
        this.fetchSuggestionList();
        this.timer = setInterval(this.fetchSuggestionList, 3000);
  },
  methods: {
    fetchSuggestionList: function() {
        // $.get('/suggestions/', function(suggest_list) {
        //     this.suggestions = suggest_list.suggestions;
        //     console.log(suggest_list);
        // }.bind(this));
        axios
          .get('/suggestions/')
          .then(response => (this.suggestions = response.data.suggestions))
        console.log(this.suggestions)
    },
    cancelAutoUpdate: function() { clearInterval(this.timer) }
  },
  beforeDestroy() {
    clearInterval(this.timer)
  }

})
// new Vue({
//   el: '#app-4',
//   data () {
//     return {
//       suggestions: null
//     }
//   },
//   mounted () {
//     axios
//       .get('/suggestions/')
//       .then(response => (this.suggestions = response.data.suggestions))
//       // .then(response => console.log(this.suggestions))
//     setInterval(function () {
//       axios
//         .get('/suggestions/')
//         .then(response => (this.suggestions = response.data.suggestions))
//     }.bind(this), 1000);
//   }
//   //https://laracasts.com/discuss/channels/vue/how-to-periodically-poll-a-back-end-api-using-vuejs
// })
