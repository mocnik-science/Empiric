#!/usr/bin/env python3

from flask import escape, Flask, jsonify, render_template, request

app = Flask(__name__)

DRAW_GEOMETRIES = 'DRAW_GEOMETRIES'
TRANSFORM_GEOMETRIES = 'TRANSFORM_GEOMETRIES'

@app.route('/')
def map():
  step = int(request.args.get('step', '0'))
  return render_template('map.html', step=step)

@app.route('/settings')
def settings():
  step = int(request.args.get('step', '0'))
  print(step)
  return jsonify({
    'task': TRANSFORM_GEOMETRIES,
    'transformTranslate': True,
    'transformResize': False,
    'transformResizeNonUniform': True,
    'transformRotate': True,
    'geometries': [
      'vienna_02_block_01.geojson',
      'vienna_02_block_02.geojson',
      {
        'filename': 'vienna_02_block_03.geojson',
        # 'rotate': .4,
        'translate': [0, 100],
        # 'scale': [2, 2],
      },
      'vienna_02_block_04.geojson',
      'vienna_02_block_05.geojson',
      'vienna_02_block_06.geojson',
    ],
    'geometriesColor': 'RED',
    'drawColor': 'BLUE',
    'drawCount': None,
    'backgroundImage': 'vienna_02.jpg',
    'backgroundImageSize': {'height': 1600, 'width': 2560},
    'waitAfterLastDraw': 2000,
    'waitBeforeNext': 1000,
  })

app.run(debug=True)
