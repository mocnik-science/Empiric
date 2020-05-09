from xml.etree import ElementTree

from Empiric.internal.Print import COLORS, Print
from Empiric.internal.Statistics import VISUALIZATION_TYPE
from Empiric.Pages.Page import Page

class PageQuestionnaire(Page):
  @staticmethod
  def _attrib(n, key, defaultValue=None):
    return n.attrib[key] if n.attrib and key in n.attrib else defaultValue
  def run(self, **settings):
    statistics = None
    if 'statistics' in settings and isinstance(settings['statistics'], str):
      statistics = {
        'title': settings['statistics'],
      }
      try:
        substatistics = {}
        if 'questions' in settings:
          questions = ElementTree.fromstring('<root>' + settings['questions'] + '</root>')
          for n in questions:
            key = PageQuestionnaire._attrib(n, 'key')
            if not key or key in statistics:
              continue
            s = {'key': key}
            if n.tag == 'choice':
              substatistics[key] = {
                **s,
                'title': PageQuestionnaire._attrib(n, 'text'),
                'data': {
                  'selector': f'questionnaire.{key}',
                  'aggregateByPage': 'first',
                },
                'visualization': {
                  'type': VISUALIZATION_TYPE.BAR_CHART,
                  'options': list(map(lambda x: x.text, n)),
                },
              }
            elif n.tag == 'slider':
              substatistics[key] = {
                **s,
                'title': PageQuestionnaire._attrib(n, 'text'),
                'data': {
                  'selector': f'questionnaire.{key}',
                  'aggregateByPage': 'first',
                },
                'visualization': {
                  'type': VISUALIZATION_TYPE.BOX_PLOT,
                  'options': list(map(lambda x: x.text, n)),
                  'min': PageQuestionnaire._attrib(n, 'min'),
                  'max': PageQuestionnaire._attrib(n, 'max'),
                  'min-label': PageQuestionnaire._attrib(n, 'min-label'),
                  'center-label': PageQuestionnaire._attrib(n, 'center-label'),
                  'max-label': PageQuestionnaire._attrib(n, 'max-label'),
                },
              }
            elif n.tag == 'text':
              substatistics[key] = {
                **s,
                'title': PageQuestionnaire._attrib(n, 'text'),
                'data': {
                  'selector': f'questionnaire.{key}',
                  'aggregateByPage': 'first',
                },
                'visualization': {
                  'type': VISUALIZATION_TYPE.TEXT_COLLECTION,
                },
              }
        statistics['substatistics'] = list(substatistics.values())
      except Exception as e:
        Print.log('WARNING: Could not parse questionnaire')
    return super().run(defaultStatistics=statistics, **settings)

def pageQuestionnaire(m, title='', questions='', **kwargs):
  return PageQuestionnaire(m, 'pageQuestionnaire.html').run(title=title, questions=questions, **kwargs)
