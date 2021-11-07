[back to readme](../../../)

# Page ‘Final’

This page indicates to the interviewee that the experiment has been completed.  It is similar to [`PageInfo`](pageInfo.md) but has different default values and shows a symbol indicating that the experiment has successfully been conducted.  It can be used as follows:
```python
from Empiric import Experiment, pageFinal

def manuscript(m):
  pageFinal(m)
```

The following keyword arguments can be used:

| Key | Type | Mandatory | Default | Meaning |
| --- | ---- | --------- | ------- | ------- |
| `title` | `String` | no | `'Thank you for completing this questionnaire!'` | Title to be shown |
| `message` | `String` | no | `'Your participation in this study helps us.  This is highly appreciated.<br/>You may now close the browser window or tab.'` | Message to be shown |

In addition to this, the keyword arguments as documented in the [Section on statistics](statistics.md) are available.
