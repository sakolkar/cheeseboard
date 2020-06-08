const Clip = {
  name: 'Clip',
  template: `
    <div>
    <!--
      <iframe
        :style="style"
        :src="'https://clips.twitch.tv/embed?clip=' \
              + clip.slug \
              + '&parent=cheeseboard.satyen.dev' \
              + '&autoplay=false' \
              + '&muted=true'"
        preload="metadata"
        height="270"
        width="480"
        frameborder="0"
        scrolling="no"
        allowfullscreen="true">
      </iframe>
      -->
    </div>
  `,
  props: [ 'clip' ],
  data: function() {
    return {
      style: {
        'border-radius': '5px'
      },
    }
  }
}

export { Clip }
