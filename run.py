#!/usr/bin/env python3

from Empirism import Experiment, pageInfo, pageMap, DRAW_GEOMETRIES, TRANSFORM_GEOMETRIES

def manuscript(m):
  # print('a', pageInfo(m, 'a'))

  geometries01 = [
    'vienna_01_block_01.geojson',
    'vienna_01_block_02.geojson',
    'vienna_01_block_03.geojson',
    'vienna_01_block_04.geojson',
    'vienna_01_block_05.geojson',
    'vienna_01_block_06.geojson',
  ]
  geometries02 = [
    'vienna_02_block_01.geojson',
    'vienna_02_block_02.geojson',
    {
      'filename': 'vienna_02_block_03.geojson',
      'translate': [0, 100],
      'scale': [2, 1],
      'rotate': 3.1415 / 2,
    },
    'vienna_02_block_04.geojson',
    'vienna_02_block_05.geojson',
    'vienna_02_block_06.geojson',
  ]

  print('b', pageMap(m, task=TRANSFORM_GEOMETRIES, backgroundImage='vienna_01.jpg', geometries=geometries01))
  print('b', pageMap(m, task=DRAW_GEOMETRIES, backgroundImage='vienna_02.jpg', geometries=geometries02))
  print('c', pageInfo(m, 'c'))

experiment = Experiment(debug=True, openBrowser=False)
experiment.run(manuscript)
