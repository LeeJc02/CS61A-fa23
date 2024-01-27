test = {
  'name': 'Dictionaries',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> pokemon = {'pikachu': 25, 'dragonair': 148, 'mew': 151}
          >>> pokemon['pikachu']
          cb65f2ff357d7368f6d293aaf0bbd356
          # locked
          >>> len(pokemon)
          74689fcda5421388b764b40ec8de8ccd
          # locked
          >>> 'mewtwo' in pokemon
          ac667055c8e3c84ad7260b0fefa2e007
          # locked
          >>> 'pikachu' in pokemon
          4975a2633e94dd9ea1ce929c1df08a3b
          # locked
          >>> 25 in pokemon
          ac667055c8e3c84ad7260b0fefa2e007
          # locked
          >>> 148 in pokemon.values()
          4975a2633e94dd9ea1ce929c1df08a3b
          # locked
          >>> 151 in pokemon.keys()
          ac667055c8e3c84ad7260b0fefa2e007
          # locked
          >>> 'mew' in pokemon.keys()
          4975a2633e94dd9ea1ce929c1df08a3b
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
