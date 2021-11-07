[back to readme](../../../)

# Page Demography’

This page asks the interviewee to provide some demographic information.  It can be used as follows:
```python
from Empiric import Experiment, pageDemography

def manuscript(m):
  pageDemography(m)
```

The following keyword arguments can be used:

| Key | Type | Mandatory | Default | Meaning |
| --- | ---- | --------- | ------- | ------- |
| `aspects` | `ASPECT` | no | `[ASPECT.GENDER, ASPECT.AGE, ASPECT.EDUCATION]` | Aspects on which information is to be collected |

In addition to this, the keyword arguments as documented in the [Section on statistics](statistics.md) are available.
