import { UserList } from './userlist.js'

const Sidebar = {
  name: 'Sidebar',
  template: `
    <div>
      <div>
        <div class="sidebar-underlay shadow-purple bg-gray"></div>
        <div class="sidebar bg-gray">
          <UserList></UserList>
        </div>
      </div>
    </div>
  `,
  components: {
    'UserList': UserList
  }
}

export { Sidebar }
