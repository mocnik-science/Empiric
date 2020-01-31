from Empirism.Page import Page

class PageInfo(Page):
  pass

def pageInfo(m, title='', message=''):
  return PageInfo(m, 'pageInfo.html').run(title=title, message=message)
