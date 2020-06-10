let currentClip = Vue.observable({ currentClip: null })
let showPlayer = Vue.observable({ showPlayer: false })

Object.defineProperty(Vue.prototype, "$currentClip", {
  get() {
    return currentClip.currentClip
  },
  set(value) {
    currentClip.currentClip = value
  }
})

Object.defineProperty(Vue.prototype, "$showPlayer", {
  get() {
    return showPlayer.showPlayer
  },
  set(value) {
    showPlayer.showPlayer = value
  }
})

let setClip = function(clip) {
  currentClip.currentClip = clip
}

let setShowPlayer = function(show) {
  showPlayer.showPlayer = show
}

const ClipPlayer = {
  name: 'ClipPlayer',
  template: `
    <div>
      <div ref="player" v-if="this.$showPlayer" class="clipplayer d-flex align-items-center justify-content-center" v-on:keyup.esc="close" @click.stop="close" tabindex="0">
        <iframe
          class="shadow-purple"
          :src="'https://clips.twitch.tv/embed?clip=' \
                + this.$currentClip.slug \
                + '&parent=cheeseboard.satyen.dev' \
                + '&autoplay=true' \
                + '&muted=false'"
          preload="metadata"
          height="596.25"
          width="1096"
          frameborder="0"
          scrolling="no"
          allowfullscreen="true">
        </iframe>
      </div>
    </div>
  `,
  mounted() {
    this.$refs.player.focus()
  },
  watch: {
    $currentClip () {
      console.log("currentClip has changed")
    },
    $showPlayer () {
      console.log("showPlayer has changed")
    }
  },
  methods: {
    close: function() {
      this.$showPlayer = false
    }
  }
}

export { setClip, setShowPlayer, ClipPlayer }
