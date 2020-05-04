from Empiric.Page import Page

DRAW_GEOMETRIES = 'DRAW_GEOMETRIES'
TRANSFORM_GEOMETRIES = 'TRANSFORM_GEOMETRIES'

class PageMap(Page):
  def run(self, **settings):
    settings = {
      'task': DRAW_GEOMETRIES,
      'transformTranslate': False,
      'transformResize': True,
      'transformResizeNonUniform': False,
      'transformRotate': True,
      'geometries': [],
      'geometriesColor': 'RED',
      'drawColor': 'BLUE',
      'drawCount': None,
      'backgroundImageSize': {'width': 2560, 'height': 1600},
      'backgroundOpacity': .6,
      'waitAfterLastDraw': 2000,
      'waitBeforeNext': 1000,
      **settings,
    }
    if 'instruction' not in settings:
      if settings['task'] == DRAW_GEOMETRIES:
        if settings['drawCount'] == 1:
          settings['instruction'] = 'Draw one additional geometry'
        else:
          settings['instruction'] = 'Draw additional geometries'
      if settings['task'] == TRANSFORM_GEOMETRIES:
        settings['instruction'] = 'Transform the geometries'
    return super().run(**settings)

def pageMap(m, backgroundImage=None, **settings):
  if not backgroundImage:
    raise Exception('Please provide a background image')
  return PageMap(m, 'pageMap.html').run(backgroundImage=backgroundImage, **settings)