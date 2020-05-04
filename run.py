#!/usr/bin/env python3

from Empiric import Experiment, pageFinal, pageInfo, pageMap, pageQuestionaire, DRAW_GEOMETRIES, TRANSFORM_GEOMETRIES
import math

def manuscript(m):
  pageInfo(m, title='Welcome', message='In the next half of an hour, you will participate in an empirical study.  In order to do so, follow the instructions on the screen.  To go to the next page, click on the green button in the top right corner.')
  pageQuestionaire(m, questions='''
    <choice
      key="changeOfMappingBehaviour"
      text="Did your mapping behaviour change over time?"
      required
    >
      <option>yes</option>
      <option>maybe</option>
      <option>no</option>
    </choice>
    <choice
      key="test2"
      text="Did your mapping behaviour change over time??"
    >
      <option>yes</option>
      <option>of course</option>
      <option>no</option>
    </choice>
    <infobox>In the following, we have some questions about your general understanding of how to map.</infobox>
    <slider
      key="awarenessOfContext"
      text="The way existing geometries were added are important to me?"
      min="0"
      max="10"
      min-label="unimportant"
      center-label="undecided"
      max-label="important"
      required
    />
    <slider
      key="awarenessOfContext2"
      text="The way existing geometries were added are important to me?"
      min-label="unimportant"
      max-label="important"
      required
    />
    <text
      key="comments"
      text="Do you have any comments?"
      rows="6"
    />
  ''')

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
      'rotate': math.pi / 2,
    },
    'vienna_02_block_04.geojson',
    'vienna_02_block_05.geojson',
    'vienna_02_block_06.geojson',
  ]

  for i in [1, 2, 3]:
    pageMap(m, task=TRANSFORM_GEOMETRIES, backgroundImage='vienna_01.jpg', geometries=geometries01[i:i+2])

  pageMap(m, task=TRANSFORM_GEOMETRIES, backgroundImage='vienna_01.jpg', geometries=geometries01)
  pageMap(m, task=DRAW_GEOMETRIES, backgroundImage='vienna_02.jpg', geometries=geometries02)
  pageFinal(m)

experiment = Experiment(debug=True, openBrowser=False)
experiment.run(manuscript, useAccessCodes=False)
