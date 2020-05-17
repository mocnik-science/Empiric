[back to readme](../../../)

# Page ‘Info’

This page shows information to the interviewee and can be used for some introductory words, or information about the pages to come.  It can be used as follows:
```python
from Empiric import Experiment, pageInfo

def manuscript(m):
  pageInfo(m, title='Welcome', message='In the next half of an hour, you will participate in an empirical study.  In order to do so, follow the instructions on the screen.  To go to the next page, click on the green button in the top right corner.')
```

The following keyword arguments can be used:

| Key | Type | Mandatory | Default | Meaning |
| --- | ---- | --------- | ------- | ------- |
| `title` | `String` | no | `''` | Title to be shown |
| `message` | `String` | no | `''` | Message to be shown |

In addition to this, the keyword arguments as documented in the [Section on statistics](statistics.md) are available.
