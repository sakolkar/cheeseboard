import { Clip } from './clip.js'

const ClipsGroup = {
  name: 'ClipsGroup',
  template: `
    <div>
      <div class="container col-12">
        <div class="d-flex flex-wrap justify-content-center">
          <div v-for="clip in clips" :key="clip.id">
            <Clip v-if="showClip(clip)" :clip="clip" class="ml-3 mt-3"></Clip>
          </div>
        </div>
      </div>
    </div>
  `,
  components: {
    'Clip': Clip,
  },
  props: [
    'name',
    'clipsEndpoint'
  ],
  data: function() {
    return {
      clips: [],
    }
  },
  created() {
    axios.get(this.clipsEndpoint)
      .then((res) => {
        this.clips = res.data
        var history = localStorage.getItem('history')
        var watchedClips = new Array()
        if (history != null) {
          watchedClips = history.split('|')
        }
        for (let c of this.clips) {
          if (watchedClips.includes(c.slug)) {
            c.watched = true
          }
        }
      })
      .catch((err) => {
        console.log(err)
      })
  },
  methods: {
    showClip: function(clip) {
      if (this.$currentUser == null) {
        return true
      }
      if (clip.users.includes(this.$currentUser.display_name)) {
        return true
      }
      return false
    }
  }
}

export { ClipsGroup }
