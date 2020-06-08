const Navbar = {
  name: 'Navbar',
  template: `
    <div>
      <nav class="navbar navbar-expand-lg navbar-dark shadow-yellow \
                  bg-gray-pri">

        <a class="navbar-brand d-flex" href="/">

          <img src="../img/chwToast.png" width="48" height="48"/>
          <img src="../img/chwF.png" width="48" height="48"/>
          <img src="../img/Clap.gif" width="48" height="48"/>

          <span class="mx-1"></span>

          <div class="d-flex align-content-center">
            <h1 class="font-playfair text-yellow">The</h1>
            <span class="mx-1"></span>
            <h1 class="mt-1 font-chewy text-yellow">Cheese</h1>
            <span class="mx-1"></span>
            <h1 class="font-playfair text-yellow">Board.</h1>
          <div>
        </a>

        <div class="mx-auto"></div>

        <a class="navbar-brand" href="https://twitch.tv/cheesewiz" target="_blank">
          <img src="../img/TwitchExtrudedWordmarkPurple.png" height="48"/>
        </a>
      </nav>
    </div>
  `,
}

export { Navbar }
