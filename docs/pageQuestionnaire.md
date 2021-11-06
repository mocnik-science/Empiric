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

## Infoimage

The element `infobox` renders as an image.  For instance, the element can look like follows:
```xml
<infoimage img="image1.jpg|image2.jpg|http://xyz.org/test.jpg"></infobox>
```

The following properties can be used:

| Key | Mandatory | Default | Meaning |
| --- | --------- | ------- | ------- |
| `img` | yes | | URLs of the images to be loaded.  The URLs are separated by `\|`.  If a URL is not absolute, it refers to the folder `static/files/` |

## Infobox

The element `infobox` renders as an information text.  For instance, the element can look like follows:
```xml
<infobox>The subsequent questions are about personal information.  They are not mandatory.</infobox>
```

## Choice

The element `choice` renders as a question with several predefined options to answer the question.  For instance, the element can look like follows:
```xml
<choice
  key="doYouLikeEmpiric"
  text="Do you like Empiric?"
  required
>
  <option>yes, of course!</option>
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

## Slider

The element `slider` renders as a question with a slider to answer the question.  The slider can, thereby, be adapted to represent a Likert scale.  For instance, the element can look like follows:
```xml
<slider
  key="comments"
  text="Do you like questions?"
  min="0"
  max="10"
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
| `required` | no | not present | If `required` is present, this element needs a mandatory reply.  Without providing a reply, the interviewee cannot proceed to the next page |
