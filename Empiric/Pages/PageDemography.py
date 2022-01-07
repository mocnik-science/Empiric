from Empiric.Pages.PageQuestionnaire import pageQuestionnaire

class ASPECT:
  GENDER = 'gender'
  AGE = 'age'
  EDUCATION = 'education'

def pageDemography(m, statistics='demography', aspects=[ASPECT.GENDER, ASPECT.AGE, ASPECT.EDUCATION], message='To better understand potential biases, we would appreciate if you share some demographic information.', textGender='What is your gender?', labelFemale='female', labelMale='male', labelNonBinary='non-binary', textAge='How old are you?', labelOrYounger='or younger', labelOrOlder='or older', textEducation='What is the highest level of education you have completed?', labelNoSchoolCompleted='no school completed', labelGraduatedFromHighSchool='graduated from high school', labelCollegeUniversityDegreeOrHigher='college/university degree or higher', labelPreferNotToAnswer='prefer not to answer', **kwargs):
  script = '<infobox>{message}</infobox>'.format(message=message)
  preferNotToAnswer = '<option>{labelPreferNotToAnswer}</option>'.format(labelPreferNotToAnswer=labelPreferNotToAnswer) if labelPreferNotToAnswer else ''
  for aspect in aspects:
    if aspect == ASPECT.GENDER:
      script += '''
<choice
  key="gender"
  text="{textGender}"
  required="1"
>
  <option>{labelFemale}</option>
  <option>{labelMale}</option>
  <option>{labelNonBinary}</option>
  {preferNotToAnswer}
</choice>'''.format(textGender=textGender, labelFemale=labelFemale, labelMale=labelMale, labelNonBinary=labelNonBinary, preferNotToAnswer=preferNotToAnswer)
    if aspect == ASPECT.AGE:
      script += '''
<choice
  key="age"
  text="{textAge}"
  required="1"
>
  <option>29 {labelOrYounger}</option>
  <option>30–39</option>
  <option>40–49</option>
  <option>50–59</option>
  <option>60 {labelOrOlder}</option>
  {preferNotToAnswer}
</choice>'''.format(textAge=textAge, labelOrYounger=labelOrYounger, labelOrOlder=labelOrOlder, preferNotToAnswer=preferNotToAnswer)
    if aspect == ASPECT.EDUCATION:
      script += '''
<choice
  key="education"
  text="{textEducation}"
  required="1"
>
  <option>{labelNoSchoolCompleted}</option>
  <option>{labelGraduatedFromHighSchool}</option>
  <option>{labelCollegeUniversityDegreeOrHigher}</option>
  {preferNotToAnswer}
</choice>'''.format(textEducation=textEducation, labelNoSchoolCompleted=labelNoSchoolCompleted, labelGraduatedFromHighSchool=labelGraduatedFromHighSchool, labelCollegeUniversityDegreeOrHigher=labelCollegeUniversityDegreeOrHigher, preferNotToAnswer=preferNotToAnswer)
  return pageQuestionnaire(m, statistics=statistics, questions=script, **kwargs)
