from Empiric.Page import Page

class PageAccessCode(Page):
  pass

def pageAccessCode(m, showErrorMessage=False, **kwargs):
  return PageAccessCode(m, 'pageAccessCode.html').render(showErrorMessage=showErrorMessage, **kwargs)
