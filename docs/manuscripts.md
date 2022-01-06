[back to readme](../../../)

# Manuscripts

Mnauscripts describe the way an experiment is conducted.  This includes what information is shown to the interviewee and which experiments are conducted.  All these steps of the manuscript are called pages.  That is, a manuscript consists of several pages, which are presented to the reader one after another.  The order in which these are presented is defined in the manuscript, and so are the parameters that determine how a page looks like.

Manuscripts are usual Python methods.  This has the advantage that the order and parameters of a page can be adjusted during the experiment itself, depending on the results provided by the interviewee.  Accordingly, it is easily possible to divide the group of interviewees into several comparison groups and to dynamically adjust the pages presented to the interviewee depending on his or her performance and the answers provided.

## Parameters

The logo, the footer, and messages about required questions can be set like follows:
```python
def manuscript(m):
  m.setLogo('logo.svg')
  m.setFooter('Dr Franz-Benjamin Mocnik, University of X, 2022')
  m.setMessageTodo('Please provide answers to all required questions.')
```

## Pages

`Empiric!` currently includes these pages by default:
* [`PageInfo`](pageInfo.md)
* [`PageQuestionnaire`](pageQuestionnaire.md)
* [`PageMap`](pageMap.md)
* [`PageFinal`](pageFinal.md)

Such a page can easily be imported and added to the manuscript:
```python
from Empiric import pageX

def manuscript(m):
  pageX(m, ...)
```

Here, `pageX` has to be replaced by the corresponding name of the page, and parameters can be inserted instead of the `...` in method call of the page.  Some of the parameters available deal with the way the resulting information is analysed statistically.  Information on these parameters can be found in the [Section about statistics](statistics.md).  Further parameters are available and differ from page to page.  Accordingly, these are discussed in the documentation of the pages itself.

Besides these pages, further pages can be added.  More information can be found on the corresponding [**Section about how to create new pages**](creatingNewPages.md).

## Individual Experiments and Comparison Groups

It is easy to randomly divide the group of interviewees into two or more comparison groups.  It seems straight forward to achieve such a division by generating a random number between `0` and `n` in the manuscript:
```python
group = random.randint(0, n)
```
However, the design of the manuscript makes it mandatory to register such choices, as will be explained in the following.  This has two reasons.  First, the manuscript is run each time an interviewee interacts with the system.  When the interviewee opens the next page, or even reopens the browser, each page of the manuscript run checked again.  These pages that have been completed before, according to the log file, will be left out.  The first page that has not yet been completed will be used, accordingly.  If a group would randomly be assigned to the interviewee each time the manuscript is run, this would lead to confusion.  Secondly, it is helpful to know to which group an interviewee has been assigned, which is why such data should be stored in the logs.

The issues raised can easily be resolved.  `Empiric!` offers a method `register`, which makes possible to register such choices, to then store them in the logs and remember this decision whenever the manuscript is run again.  Practically, this would mean to execute the following code:
```python
group = register(m, lambda: random.randint(0, n))
```
The second parameter of `register` takes a method that returns the choice made, in this case, a random number.

In order to divide the group of interviewees into three comparison groups, the following code would be used:
```python
from Empiric import Experiment, register
import random

def manuscript(m):
  ...
  group = register(m, lambda: random.randint(0, 2))
  if group == 0:
    ...
  elif group == 1:
    ...
  elif group == 3:
    ...
```

In addition to such random decisions, in which it is mandatory to register the decision, it is also possible to dynamically react to the way the interviewee has performed in the experiment.  In this case, the result of a page, such as the answers provided to a questionnaire or the way an interviewee has interacted with a map, can be used easily:
```python
data = pageX(m, ...)
```
This variable `data` contains both the log of what the interviewee did when using this page, as well as the results finally provided.  (More information can be found in the [Section about the collected data](collectedData.md).)  Practically, which experiment is shown subsequently can depend on the choice an interviewee made in a questionnaire:
```python
from Empiric import Experiment, register

def manuscript(m):
  data = pageQuestionnaire(m, questions='''
    <choice
      key="mapUse"
      text="Have you ever used a map?"
    >
      <option>yes</option>
      <option>no</option>
    </choice>
  ''')
  if data['questionnaire']['mapUse'] == 'yes':
    ...
  else:
    ...
```

In the case of this example, the decision of how to proceed only depends on the results of the preceeding pages.  As the results of preceeding pages have already been registered automatically (the results of page is always registered), there is no need to register this decision.  It will always be made in the same way, because the preceeding pages have been finished already and their results have been memorized.

**In case of doubt about whether a decision includes some randomness (and accordingly needs to be registered), it is advised to register the decision.**
