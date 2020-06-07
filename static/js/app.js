import { Navbar } from './navbar.js'
import { ClipsGroup } from './clipsgroup.js'

const App = {
  name: 'App',
  template: `
    <div>
      <Navbar></Navbar>
      <br class="pt-5">
      <ClipsGroup :name="'Clips - Tier 1'"></ClipsGroup>
    </div>
  `,
  components: {
    'Navbar': Navbar,
    'ClipsGroup': ClipsGroup,
  },
}

export { App }
