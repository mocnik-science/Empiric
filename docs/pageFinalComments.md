[back to readme](../../../)

# Page ‘FinalComments’

This page asks the interviewee about final comments.  It can be used as follows:
```python
from Empiric import Experiment, pageFinalComments

def manuscript(m):
  pageFinalComments(m)
```

The following keyword arguments can be used:

| Key | Type | Mandatory | Default | Meaning |
| --- | ---- | --------- | ------- | ------- |
| `title` | `String` | no | `'Final Comments'` | Title to be shown |
| `message` | `String` | no | `'Is there anything related to this questionnaire you would like to say?'` | Message to be shown |

In addition to this, the keyword arguments as documented in the [Section on statistics](statistics.md) are available.
