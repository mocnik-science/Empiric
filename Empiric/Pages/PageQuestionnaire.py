from xml.etree import ElementTree

from Empiric.internal.Print import COLORS, Print
from Empiric.internal.Statistics import VISUALIZATION
from Empiric.Pages.Page import Page

class PageQuestionnaire(Page):
  @staticmethod
  def _attrib(n, key, defaultValue=None):
    return n.attrib[key] if n.attrib and key in n.attrib else defaultValue
  def run(self, **settings):
    statistics = {}
    try:
      if 'questions' in settings:
        questions = ElementTree.fromstring('<root>' + settings['questions'] + '</root>')
        for n in questions:
          key = PageQuestionnaire._attrib(n, 'key')
          if not key or key in statistics:
            continue
          s = {'key': key}
          if n.tag == 'choice':
            s['visualization'] = VISUALIZATION.BAR_CHART
            s['options'] = list(map(lambda x: x.text, n))
            statistics[key] = s
          elif n.tag == 'slider':
            s['visualization'] = VISUALIZATION.BOX_PLOT
            s['min'] = PageQuestionnaire._attrib(n, 'min')
            s['max'] = PageQuestionnaire._attrib(n, 'max')
            s['min-label'] = PageQuestionnaire._attrib(n, 'min-label')
            s['center-label'] = PageQuestionnaire._attrib(n, 'center-label')
            s['max-label'] = PageQuestionnaire._attrib(n, 'max-label')
            statistics[key] = s
          elif n.tag == 'text':
            s['visualization'] = VISUALIZATION.TEXT_COLLECTION
            statistics[key] = s
    except Exception as e:
      Print.log('WARNING: Could not parse questionnaire')
    return super().run(defaultStatistics=statistics, **settings)

def pageQuestionnaire(m, title='', questions='', **kwargs):
  return PageQuestionnaire(m, 'pageQuestionnaire.html').run(title=title, questions=questions, **kwargs)
