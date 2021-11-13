[back to readme](../../../)

# Page ‘Questionnaire’

This page shows a questionnaire, which can be answered by the interviewee.  It can be used as follows:
```python
from Empiric import Experiment, pageQuestionnaire

def manuscript(m):
  pageQuestionnaire(m, questions='''
    <choice
      key="doYouLikeEmpiric"
      text="Do you like Empiric?"
    >
      <option>yes, of course!</option>
      <option>maybe</option>
      <option>no</option>
    </choice>
    <text
      key="comments"
      text="Do you have any comments?"
    ></text>
  ''')
```

The following keyword arguments can be used:

| Key | Type | Mandatory | Default | Meaning |
| --- | ---- | --------- | ------- | ------- |
| `questions` | `XML formatted String` | yes | | The keyword argument `questions` determines how the questionnaire looks like.  The string provided by this argument needs to be valid XML code (technically, a route element would be required).  The elements available are described below. |

In addition to this, the keyword arguments as documented in the [Section on statistics](statistics.md) are available.

## Infodebug

The element `infodebug` renders as a debug text in case the debug mode is switched on.  For instance, the element can look like follows:
```xml
<infodebug>This is information only for the purpose of debugging.  In production mode, it is hidden.</infodebug>
```

## Gap

The element `gap` renders a vertical space.  For instance, the element can look like follows:
```xml
<gap size="3rem"></gap>
```

The following properties can be used:

| Key | Mandatory | Default | Meaning |
| --- | --------- | ------- | ------- |
| `size` | yes | | Size of the vertical gap |

## Wait

The element `wait` lets the interviewee wait until he or she can proceed.  To proceed, the interviewee has either to wait until the remainder of the questionnaire is shown automatically (in case `proceed-automatically` is `true`) or to confirm actively by clicking the caption (in case `proceed-automatically` is `false`).  For instance, the element can look like follows:
```xml
<wait
  seconds="5"
  proceed-automatically="true"
  caption="Read the information box carefully<br/>and wait at least {seconds} before proceeding."
></wait>
```

The following properties can be used:

| Key | Mandatory | Default | Meaning |
| --- | --------- | ------- | ------- |
| `seconds` | no | 5 | Number of seconds to wait before the interviewee can proceed.  If this value is `0`, the interviewee can proceed directly.  A value of `0` makes only sense if `proceed-automatically` is set to `false`. |
| `proceed-automatically` | no | true | Determines whether the remainder of the questionnaire is shown after `seconds`, or whether the interviewee has to actively click on the caption. |
| `caption` | no | `'Read the information box carefully<br/>and wait at least {seconds} before proceeding.'` | Caption to be shown when waiting.  The string `{s}` is replaced by the number of seconds, and `{seconds}` by `{s} second(s)`. |
| `caption-ready` | no | `'Click to confirm that you have read the information box<br/>and would like to proceed.'` | Caption to be shown when the interviewee can proceed |

## Infotext

The element `infotext` renders as an information text.  For instance, the element can look like follows:
```xml
<infotext>The subsequent questions are about personal information.  They are not mandatory.</infotext>
```

## Infoimage

The element `infobox` renders as an image.  For instance, the element can look like follows:
```xml
<infoimage
  img="image1.jpg"
  img-copyright="(c) 2021 by ABC"
></infobox>
<infoimage
  img="http://xyz.org/test.jpg"
  img-copyright="(c) 2021 by XYZ"
></infobox>
```

The following properties can be used:

| Key | Mandatory | Default | Meaning |
| --- | --------- | ------- | ------- |
| `img` | yes | | URLs of the images to be loaded.  The URLs are separated by `\|`.  If a URL is not absolute, it refers to the folder `static/files/` |
| `img-copyright` | no | `''` | Copyright information for the image.  If an empty copyright string is provided, no copyright is shown. |

## Infobox

The element `infobox` renders as an information box with a text and, potentially, images.  For instance, the element can look like follows:
```xml
<infobox
  img="image1.jpg|image2.jpg|image3.jpg"
  img-copyright="(c) 2021 by ABC|(c) 2021 by XYZ"
  img-position="bottom"
>The subsequent questions are about personal information.  They are not mandatory.</infobox>
```

The following properties can be used:

| Key | Mandatory | Default | Meaning |
| --- | --------- | ------- | ------- |
| `img` | no | `''` | URLs of the images to be loaded.  The URLs are separated by `\|`.  If a URL is not absolute, it refers to the folder `static/files/`. |
| `img-copyright` | no | `''` | Copyright information for the images.  The strings are separated by `\|`.  If an empty copyright string is provided, no copyright is shown.  If less copyright strings than image URLs are provided, no copyright information is shown for the last images. |
| `img-position` | no | `'bottom'` | Determines whether the image is positioned before or after the text.  Can be either `'top'` or `'bottom'`. |

## Choice

The element `choice` renders as a question with several predefined options to answer the question.  For instance, the element can look like follows:
```xml
<choice
  key="doYouLikeEmpiric"
  text="Do you like Empiric?"
  required
>
  <option onClick="console.log('hurray')">yes, of course!</option>
  <option>maybe</option>
  <option>no</option>
</choice>
```

The following properties can be used:

| Key | Mandatory | Default | Meaning |
| --- | --------- | ------- | ------- |
| `key` | yes | | The key is used to identify this element, in particular in the results. |
| `text` | yes | | Question to ask |
| `required` | no | not present | If `required` is present, this element needs a mandatory reply.  Without providing a reply, the interviewee cannot proceed to the next page |
| `size` | no | `'normal'` | Adapts the size of the visual appearance.  Can be either `'normal'`, `'small'`, or `'compact'`. |

The following properties can be used for each `option`:

| Key | Mandatory | Default | Meaning |
| --- | --------- | ------- | ------- |
| `onClick` | no | '' | Code to execute after this choice has been selected. |

## Slider

The element `slider` renders as a question with a slider to answer the question.  The slider can, thereby, be adapted to represent a Likert scale.  For instance, the element can look like follows:
```xml
<slider
  key="comments"
  text="Do you like questions?"
  min="0"
  max="10"
  step="false"
  min-label="no"
  center-label="undecided"
  max-label="yes"
  required
></slider>
```

The following properties can be used:

| Key | Mandatory | Default | Meaning |
| --- | --------- | ------- | ------- |
| `key` | yes | | The key is used to identify this element, in particular in the results. |
| `text` | yes | | Question to ask |
| `min`, `max` | no | `-2`, `2` | Minimum and maximum number of the answer.  These numbers are not shown but define the range to answer. |
| `center` | no | `.5 * (max - min)` | Centre value; only used to determine where the centre label shall be displayed. |
| `step` | no | `true` | If `step` is `true`, steps are shown; otherwise they are hidden |
| `min-label`, `center-label`, `max-label` | no | `null` | Labels to use for the minimum, centre, and maximum value respectively. |
| `required` | no | not present | If `required` is present, this element needs a mandatory reply.  Without providing a reply, the interviewee cannot proceed to the next page |

If `min` and `max` are not provided, a 5-point Likert scale is used by default.

## Text

The element `text` renders as text box in which the interviewee can fill any text he or she wants.  For instance, the element can look like follows:
```xml
<text
  key="comments"
  text="Do you have any comments?"
  rows="6"
  required
></text>
```

The following properties can be used:

| Key | Mandatory | Default | Meaning |
| --- | --------- | ------- | ------- |
| `key` | yes | | The key is used to identify this element, in particular in the results. |
| `text` | yes | | Question to ask |
| `rows` | no | `2` | Number of rows to display; this determines the vertical size of element |
| `logging` | no | `false` | If `true`, each character will be logged.  Otherwise, only the end result is saved. |
| `required` | no | not present | If `required` is present, this element needs a mandatory reply.  Without providing a reply, the interviewee cannot proceed to the next page |
