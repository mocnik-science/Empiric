from Empiric.Pages.Page import Page

class Redirect(Page):
  pass

def redirect(m, url, state='redirect', **kwargs):
  m.saveState(state)
  return Redirect(m, 'redirect.html').run(url=url, **kwargs)
