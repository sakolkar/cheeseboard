import { User } from './user.js'

let currentUser = Vue.observable({ currentUser: null })

Object.defineProperty(Vue.prototype, "$currentUser", {
  get() {
    return currentUser.currentUser
  },
  set(value) {
    currentUser.currentUser = value
  }
})

const UserList = {
  name: 'UserList',
  template: `
    <div>
      <div v-if="this.$currentUser != null && !this.$showPlayer" class="clear-user d-flex align-items-center justify-content-center" @click="clearUser">
        <h5 class="m-0 p-0">Click to go back to everyone</h5>
      </div>
      <div v-for="user in users" :key="user.twitch_id">
        <User v-if="showUser(user)" :key="user.twitch_id" :user="user">
        </User>
      </div>
    </div>
  `,
  components: {
    'User': User,
  },
  data: function() {
    return {
      users: [],
    }
  },
  created() {
    axios.get('/api/users')
      .then((res) => {
        this.users = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  },
  methods: {
    showUser: function(user) {
      if (!this.$showPlayer && this.$currentUser == null) {
        return true
      }
      if (this.$showPlayer && this.$currentClip.users.includes(user.display_name)) {
        return true
      }
      if (this.$currentUser != null && user == this.$currentUser) {
        return true
      }
      return false
    },
    clearUser: function() {
      this.$currentUser = null
    }
  }
}

export { UserList }
