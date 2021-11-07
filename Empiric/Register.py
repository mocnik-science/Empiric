from Empiric.internal.Step import Step

class Register(Step):
  pass

def register(m, valueFn, **kwargs):
  result = None
  r = Register(m)
  try:
    result = r.run(raiseError=True, **kwargs)
  except:
    result = r.save({'value': valueFn()})
  return result['value']
