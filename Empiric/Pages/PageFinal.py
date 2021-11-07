from Empiric.Pages.Page import Page

class PageFinal(Page):
  pass

def pageFinal(m, state='complete', title='Thank you for completing this questionnaire!', message='Your participation in this study helps us.  This is highly appreciated.\n\nYou may now close the browser window or tab.', **kwargs):
  m.saveState(state)
  return PageFinal(m, 'pageFinal.html').run(hideStatisticsByDefault=True, title=title, message=message, **kwargs)
