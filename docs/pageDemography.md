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
| `message` | `String` | no | `'To better understand potential biases, we would appreciate if you share some demographic information.'` |  |
| `textGender` | `String` | no | `'What is your gender?'` | Question related to the gender |
| `labelFemale` | `String` | no | `'female'` | Answer ‘female’ |
| `labelMale` | `String` | no | `'male'` | Answer ‘male’ |
| `labelNonBinary` | `String` | no | `'non-binary'` | Answer ‘non-binary’ |
| `textAge` | `String` | no | `'How old are you?'` | Question related to the age |
| `labelOrYounger` | `String` | no | `'or younger'` | Answer ‘... or younger‘ |
| `labelOrOlder` | `String` | no | `'or older'` | Answer ‘... or older‘ |
| `textEducation` | `String` | no | `'What is the highest level of education you have completed?'` | Question related to the educational level |
| `labelNoSchoolCompleted` | `String` | no | `'no school completed'` | Answer ‘no school completed‘ |
| `labelGraduatedFromHighSchool` | `String` | no | `'graduated from high school'` | Answer ‘graduated from high school‘ |
| `labelCollegeUniversityDegreeOrHigher` | `String` | no | `'college/university degree or higher'` | Answer ‘college/university degree or higher‘ |
| `labelPreferNotToAnswer` | `String` or `None` | no | `'prefer not to answer'` | Answer ‘prefer not to answer‘, or `None` if this option should not be offered |

In addition to this, the keyword arguments as documented in the [Section on statistics](statistics.md) are available.
