test = {
  'name': 'List Mutation',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # If nothing would be output by Python, type Nothing
          >>> # If the code would error, type Error
          >>> s = [6, 7, 8]
          >>> print(s.append(6))
          9e7a96d3ae4b4ef7cb85e10bcc434b41
          # locked
          >>> s
          c4bbc3dc6e6b445909d57e603979c422
          # locked
          >>> s.insert(0, 9)
          >>> s
          854155d2c2aa943f6ff2e49321d93294
          # locked
          >>> x = s.pop(1)
          >>> s
          1b0bafb718774317e839aa2a0185f888
          # locked
          >>> s.remove(x)
          >>> s
          0fa97a39619b4dac8ce87e3473e9ba24
          # locked
          >>> a, b = s, s[:]
          >>> a is s
          ede6df328b7c3fa6304f7eb1608d9dc4
          # locked
          >>> b == s
          ede6df328b7c3fa6304f7eb1608d9dc4
          # locked
          >>> b is s
          a559f517e8f86de30b928d7e29ec2331
          # locked
          >>> s = [3]
          >>> s.extend([4, 5])
          >>> s
          d034c74c513f5152a47b306749ba7f3d
          # locked
          >>> s.extend([s.append(9), s.append(10)])
          >>> s
          21137e8a512912c68b0beef99b500328
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
