import { App } from './app.js'

const MainTemplate = `
  <div>
    <App></App>
  </div>
`

new Vue({
  el: '#app',
  template: MainTemplate,
  components: {
    'App': App 
  }
})
