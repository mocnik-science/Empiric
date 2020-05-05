from Empiric.Page import Page

class PageQuestionnaire(Page):
  def run(self, **settings):
    return super().run(**settings)

def pageQuestionnaire(m, title='', questions='', **kwargs):
  return PageQuestionnaire(m, 'pageQuestionnaire.html').run(title=title, questions=questions, **kwargs)
