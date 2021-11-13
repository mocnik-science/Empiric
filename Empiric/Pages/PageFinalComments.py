from Empiric.Pages.PageQuestionnaire import PageQuestionnaire

def pageFinalComments(m, statistics='finalComments', title='Final Comments', message='Is there anything related to this questionnaire you would like to say?', **kwargs):
  data = PageQuestionnaire(m, 'pageQuestionnaire.html').run(statistics=statistics, title=title, questions='''
<text
  key="finalComments"
  text="{message}"
  rows="5"
></text>
  '''.format(message=message), **kwargs)
  return data
