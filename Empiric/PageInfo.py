from Empiric.Page import Page

class PageInfo(Page):
  pass

def pageInfo(m, title='', message='', **kwargs):
  return PageInfo(m, 'pageInfo.html').run(title=title, message=message, **kwargs)
