[back to readme](../../../)

# Redirect

This method can be used to redirect to another website.  Technically, it is a page that redirects after it has been opened.  It can be used as follows:
```python
from Empiric import Experiment, redirect

def manuscript(m):
  redirect(m, 'http://localhost')
```

The following keyword arguments can be used:

| Key | Type | Mandatory | Default | Meaning |
| --- | ---- | --------- | ------- | ------- |
| `url` | `String` | yes | | Url to be redirected to |
| `state` | `String` | no | `'redirect'` | State to be saved |

In addition to this, the keyword arguments as documented in the [Section on statistics](statistics.md) are available.
