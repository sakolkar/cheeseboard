const Clip = {
  name: 'Clip',
  template: `
    <div>
      <div class="clip" @click="clicked">
        <div class="col p-0">
          <div class="clip-underlay bg-yellow"></div>
          <img class="clip-thumbnail" :src="clip.thumbnail" width="350" height="200"/>
          <div class="clip-overlay d-flex align-items-center justify-content-center">
            <img src="../img/play.png" width="50" height="50"/>
          </div>
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
      this.$currentClip = this.clip
      this.$showPlayer = true
    }
  }
}

export { Clip }
