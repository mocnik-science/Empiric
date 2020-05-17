[back to readme](../../../)

# Statistics

The data collected in the experiments can either be accessed as JSON files and analysed manually, or they can be statistically prepared and then visualized (see [Section about the collected data](collectedData.md)).  This Section discusses the latter possibility.

## Getting Started

The data collected is stored in the folder `collected-data/`.  When opening the statistics interface, the data collected are summarized from these files and displayed.  In order to get started with this interface, the manuscript needs to be modified slightly.  For each call of a page method, a key needs to be provided, which is used internally to identify the data.  If no such key is provided, the data will not be summarized and displayed in the statistics interface:
```python
pageX(m, statistics='key')
```
For each page, it is automatically determined by the type of the page which data are suitable for a statistical analysis.  For instance, the questionnaire is analysed and all questions of the manuscript are considered accordingly.

The data collected may include personal data.  This is why it is essential to keep the data safe and not share it publicly.  Thus, a password needs to provided when calling the `run` method fo the experiment:
```python
experiment = Experiment()
experiment.run(manuscript, statisticsPassword='abcabc')
```
This password needs to be used to authenticate when opening the statistics interface (`http://localhost:5000/statistics` by default).  Further information about this parameter can be found in the [Section about experiments](experiments.md).

It needs to be kept in mind that the configuration is extracted from the manuscript and is then written to `collected-data/settings.json`.  In case this file has already been created and the settings in the manuscript are adapted, it might be necessary to delete this file and let it be recreated.  In order to do so, you have to run the experiment again and delete the corresponding JSON file with the results manually.

## Configuration

The statistical analysis can be adapted in detail.  For each page, the following keyword arguments can be used:

| Key | Type | Mandatory | Default | Meaning |
| --- | ---- | --------- | ------- | ------- |
| `statistics` | `String \| Dictionary` | no | None | Key for the statistical analysis in case of a string, or a dictionary with an individual setting for the statistical analysis |
| `defaultStatistics` | `Dictionary` | no | `None` | This keyword argument is only meant to be used for defining the default statistical setting for a user-defined page.  |
| `appendToDefaultStatistics` | `Boolean` | no | `True` | Determines whether the setting for the statistical analysis provided via the keyword argument `statistics` shall be appended to the default setting, or wheter it should replace it. |
| `hideStatisticsByDefault` | `Boolean` | no | `True` | Determines whether a warning shall be rised when no keyword argument `statistics` is provided.  This keyword argument is only meant to be used when defining a user-defined page. |

For instance, additional the statistical analysis can be extended by further data when providing a corresponding setting to the page method:
```python
pageX(m, statistics={
  'title': 'Additional data to be analysed',
  ...
})
```
The structure of this dictionary to provide as a setting for the statistical analysis is outlined in the following.

### Setting for the Statistical Analysis

The dictionary containing the setting can, for instance, look like follows:
```python
{
  'key': 'doYouLikeEmpiric',
  'title': 'Do you like Empiric?',
  'data': {
    'selector': 'questionnaire.doYouLikeEmpiric',
    'aggregateByPage': 'first',
    'defaultValue': null,
  },
  'visualization': {
    'type': 'BAR_CHART',
    'options': [
      'yes, of course!',
      'maybe',
      'no',
    ],
  },
}
```

The following keys can be used for a dictionary that defines a statistical analysis:

| Key | Type | Mandatory | Default | Meaning |
| --- | ---- | --------- | ------- | ------- |
| `key` | `String` | yes/no | computed from `title` | Key to be used internally for identifying this analysis or visualization.  Either a `key` or a `title` needs to be provided. |
| `title` | `String` | yes/no | computed from `key` | Title to be used for the analysis or visualization.  Either a `key` or a `title` needs to be provided. |
| `data` | `Dictionary` | yes | | This dictionary determines how the data contained resulting from the experiments shall be summarized and prepared for the visualization.  More information can be found in the [Section about preparing the data](#accessing-the-data). |
| `visualization` | `Dictionary` | yes | | This dictionary determines how the data summarized and prepared shall be visualized.  More information can be found in the [Section about accessing the data](#visualizing-the-data). |

If more than one analysis or visualization shall be added, these can be added under the key `substatistics`:
```python
{
  'title': 'Example',
  'substatistics': [
    {
      'key': 'doYouLikeEmpiric',
      'title': 'Do you like Empiric?',
      'data': {...},
      'visualization': {...},
    },
  ],
}
```
In this case, the dictionary contains a key `substatistics` but no key `data` or `visualization` itself.

The following keys can be used for a dictionary:

| Key | Type | Mandatory | Default | Meaning |
| --- | ---- | --------- | ------- | ------- |
| `key` | `String` | yes/no | computed from `title` | Key to be used internally for identifying this analysis or visualization.  Either a `key` or a `title` needs to be provided. |
| `title` | `String` | yes/no | computed from `key` | Title to be used for the analysis or visualization.  Either a `key` or a `title` needs to be provided. |
| `substatistics` | `List` | yes | | List of dictionaries that each define a statistical analysis and conform to the format discussed before. |

### Preparing the Data

The dictionary provided as a value for the key `data` defines how the data are prepared, based on the data collected from the experiments and stored in the JSON files in the path `data-collected/`.  A simple example of such a dictionary can be the following:
```python
{
  'selector': 'questionnaire.doYouLikeEmpiric',
  'aggregateByPage': 'first',
  'defaultValue': null
}
```
The expression provided as a value to the key `selector` conforms to the [JSONPath specification](https://pypi.org/project/jsonpath-ng/), but without the `$.` at the begin of the expression.  This expression is used to match the data collected.  As a result, a list of values is returned.  These can be aggregated accordingly.  In the case above, the first of these values is chosen for each page.  The resulting data contains only one number per interviewee, or, in case the selector matches to several pages, also several numbers.

In other cases, the data may not be aggregated by each page but by some key.  For instance, the same geometry can be shown several times and on different pages, but the results might be then aggregated per such geometry.  Several geometries are then analysed independently, but the same geometry occuring on several pages is analysed at once.  Consider the following example in the JSON files:
```JSON
...
  "geometries": [
    {
      "filename": "a.geojson"
    },
    {
      "filename": "b.geojson",
      "userRotate": 0.5187680133203525,
      "userScale": [1.2342342343243243, 2.1401869158878504]
    }
  ],
...
```
The corresponding setting to access the rotations is as follows:
```python
{
  'selector': 'geometries[*]',
  'aggregateByKey': 'filename',
  'value': 'userRotate',
  'defaultValue': 1,
}
```
The `selector` is used to find the data about the geometries, to which `aggregatorByKey` and `value` are then subsequently applied to identify the corresponding key to aggregate by, and the value to use.  In case several aspects shall be analysed or visualized, a dictionary can be provided for the `value` and the `defaultValue`:
```python
{
  'selector': 'geometries[*]',
  'aggregateByKey': 'filename',
  'value': {'x': 'userScale[0]', 'y': 'userScale[1]'},
  'defaultValue': {'x': 1, 'y': 1},
}
```

The following keys can be used for a dictionary in case, the data shall be aggregated by page:

| Key | Type | Mandatory | Default | Meaning |
| --- | ---- | --------- | ------- | ------- |
| `selector` | `JSONPath` (without `$.`) | yes | | This JSONPath expression is used to select the corresponding value to be analysed. |
| `aggregateByPage` | `String` | yes | | This string determines which aggregation method to use.  See the table below for possible aggregation methods. |
| `defaultValue` | `Any` | | `None` | Default value to be used in case the `selector` did not match any data.  If the value is `None`, this page is ignored, thus yielding to potentially less results than experiments. |

The following aggregation methods can be used:

| Method | Meaning |
| ------ | ------- |
| `COUNT` | Count the number of elements |
| `FIRST` | Take the first element |
| `MAX` | Take the maximal element |
| `MEAN` | Compute the average |
| `MIN` | Take the minimal element |
| `SUM` | Sum of the elements |
| `COLLECT` | List of all elements |

The following keys can be used for a dictionary in case, the data shall be aggregated by a key:

| Key | Type | Mandatory | Default | Meaning |
| --- | ---- | --------- | ------- | ------- |
| `selector` | `JSONPath` (without `$.`) | yes | | This JSONPath expression is used to select the corresponding data, i.e., a dictionary containing both the key and the value in some way. |
| `aggregateByKey` | `JSONPath` (without `$.`) | yes | | This expression is used to select the key for the aggregation from the data returned by `selector`. |
| `value` | `JSONPath` (without `$.`) `\| Dictionary` | yes | | This expression is used to select the value to be analysed from the data returned by `selector`. Instead of an expression, also a dictionary with several expressions as keys can be provided.  The JSONPath expressions are then replaced by their corresponding values. |
| `defaultValue` | `Any \| Dictionary` | | `None` | Default value to be used in case the `value` did not match any data.  If the value is `None`, this page is ignored, thus yielding to potentially less results. In case `value` is a dictionary, default values need to be provided as a dictionary accordingly. |

### Visualizing the Data

The data collected can be visualized.  The corresponding setting is provided in a dictionary, the specification of which differs for these visualizations.

#### Bar Chart

The following keys can be used for a dictionary:

| Key | Type | Mandatory | Default | Meaning |
| --- | ---- | --------- | ------- | ------- |
| `type` | `VISUALIZATION_TYPE` | yes | | This type needs to be `VISUALIZATION_TYPE.BAR_CHART` for this type of visualization. |

This type of visualization can be download as a PNG or an SVG file, the latter of which can easily be converted to a PDF file for a publication.  In addition, the specification of the visualization can be downloaded to be used with the library [Vega Lite](https://vega.github.io/vega-lite/).  Another option makes possible to even directly open this configuration in an interactive editor for further individual modification.

#### Box Plot

The following keys can be used for a dictionary:

| Key | Type | Mandatory | Default | Meaning |
| --- | ---- | --------- | ------- | ------- |
| `type` | `VISUALIZATION_TYPE` | yes | | This type needs to be `VISUALIZATION_TYPE.BOX_PLOT` for this type of visualization. |
| `min` | `Float` | no | minimum value of the data | Minimum value to show in the visualization |
| `center` | `Float` | no | maximal value of the data | Centre value to show in the visualization |
| `max` | `Float` | no | maximal value of the data | Maximum value to show in the visualization |
| `min-label` | `String` | no | `None` | Label for the minimum value |
| `center-label` | `String` | no | `None` | Label for the centre value |
| `max-label` | `String` | no | `None` | Label for the maximum value |

This type of visualization can be download as a PNG or an SVG file, the latter of which can easily be converted to a PDF file for a publication.  In addition, the specification of the visualization can be downloaded to be used with the library [Vega Lite](https://vega.github.io/vega-lite/).  Another option makes possible to even directly open this configuration in an interactive editor for further individual modification.

#### Text Collection

The following keys can be used for a dictionary:

| Key | Type | Mandatory | Default | Meaning |
| --- | ---- | --------- | ------- | ------- |
| `type` | `VISUALIZATION_TYPE` | yes | | This type needs to be `VISUALIZATION_TYPE.TEXT_COLLECTION` for this type of visualization. |

#### Map

The following keys can be used for a dictionary:

| Key | Type | Mandatory | Default | Meaning |
| --- | ---- | --------- | ------- | ------- |
| `type` | `VISUALIZATION_TYPE` | yes | | This type needs to be `VISUALIZATION_TYPE.MAP` for this type of visualization. |
| `backgroundImage` | `String` | yes | | Filename of the image to show in the background.  This can, e.g., be an aerial image or a map. The actual file must be placed in the folder `static/files/`. |
| `backgroundImageSize` | `Dictionary` | yes | | Size of the background image.  This needs to be changed in case the image loaded has another size. |
