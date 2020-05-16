[back to readme](../../../)

# Page ‘Final’

This page indicates to the interviewee that the experiment has been completed.  It is similar to [`PageInfo`](pageInfo.md) but has different default values and shows a symbol indicating that the experiment has successfully been conducted.  It can be used as follows:
```python
from Empiric import Experiment, pageFinal

def manuscript(m):
  pageFinal(m)
```

The following keyword arguments are available:

| Key | Mandatory | Default | Meaning |
| --- | --------- | ------- | ------- |
| `title` | no | `'Thank you!'` | Title to be shown |
| `message` | no | `'You have helped us a lot!  We highly appreciate that.'` | Message to be shown |

In addition to this, the keyword arguments as documented in the [Section on statistics](statistics.md) are available.
