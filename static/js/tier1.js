import { ClipsGroup } from './clipsgroup.js'

const Tier1 = {
  name: 'Tier1',
  template: `
    <div>
        <ClipsGroup :name="'Clips - Tier 1'" :clipsEndpoint="'/api/tier1'"></ClipsGroup>
    </div>
  `,
  components: {
    'ClipsGroup': ClipsGroup,
  },
}

export { Tier1 }
