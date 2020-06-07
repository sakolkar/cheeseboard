const ShowMore = {
  name: 'ShowMore',
  template: `
    <div>
      <div class="d-inline-block">
        asdf
      </div>
    </div>
  `,
  props: [ 'clip' ],
  data: function() {
    return {
      css: `
      @scope div {
        background-color: '#d2d2e6';
        height: 270px;
        width: 480px;
        border-radius: 5px;
      }
      div:hover {
        background-color: '#8295b4';
      }
      `,
    }
  },
  mounted() {
    let style = document.createElement('style')
    style.type = 'text/css';
    style.appendChild(document.createTextNode(this.css))
    this.$el.appendChild(style)
  }
}

export { ShowMore }
