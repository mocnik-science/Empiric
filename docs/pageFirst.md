[back to readme](../../../)

# Page ‘First’

This page asks the interviewee for consent to conduct the experiment.  It is similar to [`PageInfo`](pageInfo.md) but provides an option to agree to the participation.  If the consent is not provided, `pageFinal` is called.  It can be used as follows:
```python
from Empiric import Experiment, pageFirst

def manuscript(m):
  pageFirst(m)
```

The following keyword arguments can be used:

| Key | Type | Mandatory | Default | Meaning |
| --- | ---- | --------- | ------- | ------- |
| `title` | `String` | no | `'Welcome'` | Title to be shown |
| `message` | `String` | no | `'Thank you for taking the time to participate in this survey.\n\nYour participation in this survey is entirely voluntary.  You can end your participation at any time by closing this website.\n\nBy clicking “Yes, I agree” below you indicate that you are at least 18 years old, have read and understood this consent form, and agree to participate in this research study.'` | Message to be shown |
| `message2` | `String` | no | `'Go to the next page by clicking the green button in the top right corner.'` | Message to be shown after the choice for consent |
| `buttonYes` | `String` | `'Yes, I agree <br/>and want to participate'` | Label of the button to confirm the participation |
| `buttonNo` | `String` | `'No, I do not <br/>want to participate'` | Label of the button to decline the participation |
| `titleNoConsent` | `String` | no | `'Thank you!'` | Title to be shown if no consent is provided |
| `messageNoConsent` | `String` | no | `'You have opted to not participate.  We wish you a nice day.\n\nYou may now close the browser window or tab.'` | Message to be shown if no consent is provided |

In addition to this, the keyword arguments as documented in the [Section on statistics](statistics.md) are available.
