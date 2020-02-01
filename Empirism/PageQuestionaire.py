from Empirism.Page import Page

class PageQuestionaire(Page):
  def run(self, **settings):
    return super().run(**settings)

def pageQuestionaire(m, title='', questions=''):
  return PageQuestionaire(m, 'pageQuestionaire.html').run(title=title, questions=questions)
