import { Navbar } from './navbar.js'
import { Sidebar } from './sidebar.js'
import { ClipsGroup } from './clipsgroup.js'
import { UserList } from './userlist.js'
import { Tier1 } from './tier1.js'
import { Tier2 } from './tier2.js'
import { ClipPlayer } from './clipplayer.js'

const App = {
  name: 'App',
  template: `
    <div>
      <Navbar></Navbar>
      <Sidebar></Sidebar>
      <br class="pt-5">
      <div class="appcontent">
        <Tier1></Tier1>
        <Tier2 class="mt-5"></Tier2>
        <ClipPlayer v-if="this.$showPlayer"></ClipPlayer>
      </div>
    </div>
  `,
  components: {
    'Navbar': Navbar,
    'Sidebar': Sidebar,
    'ClipsGroup': ClipsGroup,
    'UserList': UserList,
    'Tier1': Tier1,
    'Tier2': Tier2,
    'ClipPlayer': ClipPlayer
  },
}

export { App }
