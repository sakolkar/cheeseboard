const User = {
  name: 'User',
  template: `
    <div>
      <div class="user d-flex w-100 pl-3 py-2 align-items-center">
        <img :src="user.logo"/>
        <span class="mx-2"></span>
        <div>
          <p class="text-light-yellow m-0" v-text="user.display_name"></p>
        </div>
      </div>
    </div>
  `,
  props: [ 'user' ],
}

export { User }
