from Empirism.Page import Page

def pageQuestionaire(m, title='', message=''):
  return PageInfo(m, 'map.html').run(title=title, message=message)
