import { User } from './user.js'

const UserList = {
  name: 'UserList',
  template: `
    <div>
      <div>
        <User v-for="user in users" :key="user.twitch_id" :user="user">
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
  }
}

export { UserList }
