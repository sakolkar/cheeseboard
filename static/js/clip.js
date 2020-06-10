import { setClip, setShowPlayer } from './clipplayer.js'

const Clip = {
  name: 'Clip',
  template: `
    <div>
      <div class="clip" @click="clicked">
        <div class="col p-0">
          <div class="clip-underlay bg-yellow"></div>
          <img :src="clip.thumbnail" width="350" height="200"/>
        </div>
        <h5 class="mt-2 mb-0 text-light-yellow" v-text="clip.title"></h5>
        <p class="m-0 text-light-yellow">{{ clip.broadcaster }}</p>
        <p class="m-0 text-light-yellow">Clipped by {{ clip.curator }}</p>
      </div>
    </div>
  `,
  props: [ 'clip' ],
  methods: {
    clicked: function() {
      setClip(this.clip)
      setShowPlayer(true)
    }
  }
}

export { Clip }
