from Empirism.Page import Page

class PageInfo(Page):
  def run(self, **settings):
    self._settings = settings
    return super().run()

def pageInfo(m, title='', message=''):
  return PageInfo(m, 'pageInfo.html').run(title=title, message=message)
