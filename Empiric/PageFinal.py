from Empiric.Page import Page

class PageFinal(Page):
  pass

def pageFinal(m, title='Thank you!', message='You have helped us a lot!  We highly appreciate that.', **kwargs):
  return PageFinal(m, 'pageFinal.html').run(title=title, message=message, **kwargs)
