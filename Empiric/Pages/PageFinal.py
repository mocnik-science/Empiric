from Empiric.Pages.Page import Page

class PageFinal(Page):
  pass

def pageFinal(m, title='Thank you for completing this questionnaire!', message='Your participation in this study helps us.  This is highly appreciated.\n\nYou may now close the browser window or tab.', **kwargs):
  return PageFinal(m, 'pageFinal.html').run(hideStatisticsByDefault=True, title=title, message=message, **kwargs)
