const Clip = {
  name: 'Clip',
  template: `
    <div>
      <div class="clip" @click="clicked">
        <div class="col p-0">
          <div class="clip-underlay bg-yellow"></div>
          <img class="clip-thumbnail" :src="c.thumbnail" width="350" height="200"/>
          <div class="clip-overlay d-flex align-items-center justify-content-center">
            <img src="../img/play.png" width="50" height="50"/>
          </div>
          <div v-if="watched">
            <div class="clip-watched d-flex align-items-center justify-content-center">
              <img src="../img/chwToast.png" width="32" height="32" style="margin-top: 16px"/>
              <img src="../img/chwWow.png" width="48" height="48"/>
            </div>
          </div>
        </div>
        <h5 class="mt-2 mb-0 text-light-yellow" v-text="c.title"></h5>
        <p class="m-0 text-light-yellow">{{ c.broadcaster }}</p>
        <p class="m-0 text-light-yellow">Clipped by {{ c.curator }}</p>
      </div>
    </div>
  `,
  props: [ 'clip' ],
  data: function() {
    return {
      c: this.clip,
      watched: this.clip.watched
    }
  },
  methods: {
    clicked: function() {
      this.$currentClip = this.c
      this.$showPlayer = true
      this.watched = true
      var history = localStorage.getItem('history')
      if (history == null) {
        history = this.c.slug
        localStorage.setItem('history', history)
      } else {
        var watchedClips = history.split('|')
        if (!watchedClips.includes(this.c.slug)) {
          watchedClips.push(this.c.slug)
          history = watchedClips.join('|')
          localStorage.setItem('history', history)
        }
      }
    }
  }
}

export { Clip }
