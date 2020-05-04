from Empiric.Page import Page

class PageAccessCode(Page):
  pass

def pageAccessCode(m, showErrorMessage=False):
  return PageAccessCode(m, 'pageAccessCode.html').render(showErrorMessage=showErrorMessage)
