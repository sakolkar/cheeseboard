import { ClipsGroup } from './clipsgroup.js'

const Tier2 = {
  name: 'Tier2',
  template: `
    <div>
        <ClipsGroup :name="'Clips - Tier 2'" :clipsEndpoint="'/api/tier2'"></ClipsGroup>
    </div>
  `,
  components: {
    'ClipsGroup': ClipsGroup,
  },
}

export { Tier2 }
