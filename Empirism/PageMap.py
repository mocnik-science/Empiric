from Empirism.Page import Page

DRAW_GEOMETRIES = 'DRAW_GEOMETRIES'
TRANSFORM_GEOMETRIES = 'TRANSFORM_GEOMETRIES'

class PageMap(Page):
  def run(self, **settings):
    self._settings = {
      'task': DRAW_GEOMETRIES,
      'transformTranslate': False,
      'transformResize': False,
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
    return super().run()

def pageMap(m, backgroundImage=None, **settings):
  if not backgroundImage:
    raise Exception('Please provide a background image')
  return PageMap(m, 'pageMap.html').run(backgroundImage=backgroundImage, **settings)
