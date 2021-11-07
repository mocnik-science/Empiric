from Empiric.Pages.Page import Page
from Empiric.Pages.PageFinal import pageFinal
from Empiric.Pages.PageQuestionnaire import PageQuestionnaire

class PageFirst(Page):
  pass

def pageFirst(m, statistics='consent', title='Welcome', message='Thank you for taking the time to participate in this survey.\n\nYour participation in this survey is entirely voluntary.  You can end your participation at any time by closing this website.\n\nBy clicking “Yes, I agree” below you indicate that you are at least 18 years old, have read and understood this consent form, and agree to participate in this research study.', message2='Go to the next page by clicking the green button in the top right corner.', titleNoConsent='Thank you!', messageNoConsent='You have opted to not participate.  We wish you a nice day.\n\nYou may now close the browser window or tab.', **kwargs):

  data = PageQuestionnaire(m, 'pageQuestionnaire.html').run(statistics=statistics, title=title, questions='''
<infotext>{message}</infotext>
<choice
  key="consent"
  required="1"
  noListItem="1"
>
  <option onClick="$('.nextStepButton i').addClass('pulsate')">Yes, I agree <br/>and want to participate</option>
  <option onClick="$('.nextStepButton i').addClass('pulsate')">No, I do not <br/>want to participate</option>
</choice>
<gap size="3rem"></gap>
<infotext>{message2}</infotext>
  '''.format(message=message, message2=message2), showLogo=True, **kwargs)

  if data['questionnaire']['consent'] != 'Yes, I agree and want to participate':
    pageFinal(m, state='noConsent', title=titleNoConsent, message=messageNoConsent)

  return data
