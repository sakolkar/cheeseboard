import { Clip } from './clip.js'

const ClipsGroup = {
  name: 'ClipsGroup',
  template: `
    <div>
      <div class="container col-12">
        <h2 class="text-light-yellow underline-yellow" v-text="name"></h2>
        <div class="d-flex flex-wrap justify-content-center">
          <Clip v-for="clip in clips" :key="clip.id" :clip="clip"
                class="ml-3 mt-3">
          </Clip>
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
      })
      .catch((err) => {
        console.log(err)
      })
  }
}

export { ClipsGroup }
