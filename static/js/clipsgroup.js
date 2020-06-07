import { Clip } from './clip.js'
import { ShowMore } from './showmore.js'

const ClipsGroup = {
  name: 'ClipsGroup',
  template: `
    <div>
      <div class="container col-12">
        <h2 v-text="name"></h2>
        <div class="d-flex flex-wrap justify-content-center">
          <Clip v-for="clip in clips" :key="clip.id" :clip="clip"
                class="ml-3 mt-3">
          </Clip>
          <ShowMore class="ml-3 mt-3"></ShowMore>
        </div>
      </div>
    </div>
  `,
  components: {
    'Clip': Clip,
    'ShowMore': ShowMore,
  },
  props: [
    'name'
  ],
  data: function() {
    return {
      clips: [
        {id:  1, slug: 'TenderSolidElephantTBTacoRight'},
        {id:  2, slug: 'TenderSolidElephantTBTacoRight'},
        {id:  3, slug: 'TenderSolidElephantTBTacoRight'},
        {id:  4, slug: 'TenderSolidElephantTBTacoRight'},
        {id:  5, slug: 'TenderSolidElephantTBTacoRight'},
        //{id:  6, slug: 'TenderSolidElephantTBTacoRight'},
        //{id:  7, slug: 'TenderSolidElephantTBTacoRight'},
        //{id:  8, slug: 'TenderSolidElephantTBTacoRight'},
        //{id:  9, slug: 'TenderSolidElephantTBTacoRight'},
        //{id: 10, slug: 'TenderSolidElephantTBTacoRight'},
      ],
      style: {
      },
    }
  }
}

export { ClipsGroup }
