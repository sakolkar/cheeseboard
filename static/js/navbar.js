const Navbar = {
  name: 'Navbar',
  template: `
    <div>
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark shadow">
        <a class="navbar-brand d-flex" href="" :style="style">
          <img src="../img/chwToast.png" width="48" height="48"/>
          <img src="../img/chwF.png" width="48" height="48"/>
          <span class="mx-1"></span>
          <h1>The Cheese Board</h1>
        </a>

        <div class="mx-auto"></div>

        <a class="navbar-brand" href="https://twitch.tv/cheesewiz" target="_blank">
          <img src="../img/TwitchExtrudedWordmarkPurple.png" height="48"/>
        </a>
      </nav>
    </div>
  `,
  data: function() {
    return {
      style: {
        'font-family': 'Chewy',
        'font-size': 'x-large',
      },
    }
  }
}

export { Navbar }
