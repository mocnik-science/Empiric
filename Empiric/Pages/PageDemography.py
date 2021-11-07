from Empiric.Pages.PageQuestionnaire import pageQuestionnaire

class ASPECT:
  GENDER = 'gender'
  AGE = 'age'
  EDUCATION = 'education'

def pageDemography(m, statistics='demography', aspects=[ASPECT.GENDER, ASPECT.AGE, ASPECT.EDUCATION], **kwargs):
  script = '<infobox>To better understand potential biases, we would appreciate if you share some demographic information.</infobox>'
  for aspect in aspects:
    if aspect == ASPECT.GENDER:
      script += '''
<choice
  key="gender"
  text="What is your gender?"
  required="1"
>
  <option>female</option>
  <option>male</option>
  <option>non-binary</option>
  <option>prefer not to answer</option>
</choice>'''
    if aspect == ASPECT.AGE:
      script += '''
<choice
  key="age"
  text="How old are you?"
  required="1"
>
  <option>20 or younger</option>
  <option>21–30</option>
  <option>31–40</option>
  <option>41–50</option>
  <option>51–60</option>
  <option>61 or older</option>
  <option>prefer not to answer</option>
</choice>'''
    if aspect == ASPECT.EDUCATION:
      script += '''
<choice
  key="education"
  text="What is the highest level of education you have completed?"
  required="1"
>
  <option>no school completed</option>
  <option>graduated from high school</option>
  <option>collge/university degree or higher</option>
  <option>prefer not to answer</option>
</choice>'''
  return pageQuestionnaire(m, statistics=statistics, questions=script, **kwargs)
