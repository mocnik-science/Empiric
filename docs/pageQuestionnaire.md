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

The keyword argument `questions` determines how the questionnaire looks like.  The string provided by this argument needs to be valid XML code (technically, a route element would be required).  In the following, the elements available are described.

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
  required="true"
>
  <option>yes, of course!</option>
  <option>maybe</option>
  <option>no</option>
</choice>
```

| Key | Mandatory | Default | Meaning |
| --- | --------- | ------- | ------- |
| `key` | x | | The key is used to identify this element, in particular in the results. |
| `text` | x | | Question to ask |
| `required` | | `false` | Marks this element as required.  Without providing a reply, the interviewee cannot proceed to the next page |

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
  required="true"
></slider>
```

| Key | Mandatory | Default | Meaning |
| --- | --------- | ------- | ------- |
| `key` | x | | The key is used to identify this element, in particular in the results. |
| `text` | x | | Question to ask |
| `min`, `max` | | `-2`, `2` | Minimum and maximum number of the answer.  These numbers are not shown but define the range to answer. |
| `center` | | `.5 * (max - min)` | Centre value; only used to determine where the centre label shall be displayed. |
| `min-label`, `center-label`, `max-label` | | 'null' | Labels to use for the minimum, centre, and maximum value respectively. |
| `required` | | `false` | Marks this element as required.  Without providing a reply, the interviewee cannot proceed to the next page |

If `min` and `max` are not provided, a 5-point Likert scale is used by default.

## Text

The element `text` renders as text box in which the interviewee can fill any text he or she wants.  For instance, the element can look like follows:
```xml
<text
  key="comments"
  text="Do you have any comments?"
  rows="6"
  required="true"
></text>
```

| Key | Mandatory | Default | Meaning |
| --- | --------- | ------- | ------- |
| `key` | x | | The key is used to identify this element, in particular in the results. |
| `text` | x | | Question to ask |
| `rows` | | `2` | Number of rows to display; this determines the vertical size of element |
| `required` | | `false` | Marks this element as required.  Without providing a reply, the interviewee cannot proceed to the next page |
