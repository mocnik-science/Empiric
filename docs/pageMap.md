[back to readme](../../../)

# Page ‘Map’

This page shows a map, the geometries of which can be edited and to which new geometries can be added.  It can be used as follows:
```python
from Empiric import Experiment, pageMap, TASK

def manuscript(m):
  pageMap(m, task=TASK.TRANSFORM_GEOMETRIES, backgroundImage='vienna_01.jpg', geometries=['a.geojson', 'b.geojson', 'c.geojson'])
```

The following keyword arguments can be used:

| Key | Type | Mandatory | Default | Meaning |
| --- | ---- | --------- | ------- | ------- |
| `backgroundImage` | `String` | yes | | Filename of the image to show in the background.  This can, e.g., be an aerial image or a map. The actual file must be placed in the folder `static/files/`. |
| `backgroundImageSize` | `Dictionary` | no | `{'width': 2560, 'height': 1600}` | Size of the background image.  This needs to be changed in case the image loaded has another size. |
| `backgroundOpacity` | `Number` | no | `.6` | Opacity of the background image |
| `task` | `TASK` | no | `TASK.DRAW_GEOMETRIES` | The task the interviewee shall perform.  This can either be to draw new geometries (`TASK.DRAW_GEOMETRIES`) or to transform depicted geometries (`TRANSFORM_GEOMETRIES`) |
| `transformTranslate` | `Boolean` | no | `False` | Determines whether the geometries can be translated.  This applies only if the `task` is `TASK.DRAW_GEOMETRIES`. |
| `transformResize` | `Boolean` | no | `True` | Determines whether the geometries can be resized without distortion, i.e., with the same scale in all directions.  This applies only if the `task` is `TASK.DRAW_GEOMETRIES`. |
| `transformResizeNonUniform` | `Boolean` | no | `False` | Determines whether the geometries can be translated in a non-uniform way, i.e., differently in two directions.  This applies only if the `task` is `TASK.DRAW_GEOMETRIES`. |
| `transformRotate` | `Boolean` | no | `True` | Determines whether the geometries can be rotated.  This applies only if the `task` is `TASK.DRAW_GEOMETRIES`. |
| `geometries` | `Array` | no | `[]` | This array of filenames defines, which geometries shall be displayed on top of the background image.  Instead of a filename, also a dictionary about how the geometry shall be transformed initially be provided  (see the [Section about geometries](#geometries)).  The actual files must represent the geometries according to the GeoJSON standard and be placed in the folder `static/files/`. |
| `geometriesColor` | `String` | no | `RED` | The color of the geometries to be initially displayed.  The colour string can either be a HTML compatible representation, or one of the colours defined below (see the [Section about colours](#colours)). |
| `drawColor` | `String` | no | `BLUE` | The color of the geometries to be drawn by the interviewee.  The colour string can either be a HTML compatible representation, or one of the colours defined below (see the [Section about colours](#colours)). |
| `drawCount` | `Integer` | no | `None` | The number of geometries to draw.  When the number of geometries has been reached, the next page will be opend automatically.  If `drawCount` is `None`,  the interviewee is able to proceed to the next page after having drawn one geometry, but he or she can add as many geometries as wanted. |
| `waitAfterLastDraw` | `Number` | no | `2000` | Timespan in milliseconds to still display the map (before hiding it) after the number of geometries drawn by the interviewee equals `drawCount`.  This argument is only relevant if `drawCount` is not `None`. |
| `waitBeforeNext` | `Number` | no | `1000` | Timespan in milliseconds to show only the background before proceeding to the next page.  This argument is only relevant if `drawCount` is not `None`. |

In addition to this, the keyword arguments as documented in the [Section on statistics](statistics.md) are available.

## Geometries

The geometries that shall be displayed on top of the background image need to be stored as GeoJSON files in the folder `static/files/`.  The keyword argument `geometries` is used to provide the list of corresponding filenames (without the path), or a dictionary including the filename and properties of how to transform this geometry.  Filenames and dictionaries can be mixed, for instance:
```python
import math

geometries = [
  'a.geojson',
  {
    'filename': 'b.geojson',
    'translate': [0, 100],
    'scale': [2, 1],
    'rotate': math.pi / 2,
  },
  'c.geojson']

pageMap(m, task=TASK.DRAW_GEOMETRIES, backgroundImage='background.jpg', geometries=geometries)
```

The following keys can be used for a dictionary:

| Key | Type | Mandatory | Default | Meaning |
| --- | ---- | --------- | ------- | ------- |
| `filename` | `String` | yes | | The filename of the geometry |
| `translate` | `[Float, Float]` | no | `[0, 0]` | Translation of the geometry in x and y direction |
| `scale` | `[Float, Float] \| Float` | no | `[1, 1]` | Resize of the geometry in x and y direction.  If only one number `s` is provided, this is equal to `[s, s]`. |
| `rotate` | `Float` | no | `0` | Rotation of the geometry in radians |

## Colours

The following colours are available to be used for the geometries (keyword arguments `geometriesColor` and `drawColor`):

| | NAME |
| - | ---- |
| ![](images/RED.svg) | `RED` |
| ![](images/PURPLE.svg) | `PURPLE` |
| ![](images/BLUE.svg) | `BLUE` |
| ![](images/GREEN.svg) | `GREEN` |
| ![](images/YELLOW.svg) | `YELLOW` |
| ![](images/ORANGE.svg) | `ORANGE` |
| ![](images/GRAY.svg) | `GRAY` |
