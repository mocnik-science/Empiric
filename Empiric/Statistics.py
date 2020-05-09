class AGGREGATE:
  COUNT = lambda xs: [len(x) for x in xs]
  FIRST = lambda xs: [x[0] for x in xs]
  MAX = lambda xs: [max(x) for x in xs]
  MEAN = lambda xs: [sum(x) / len(x) for x in xs]
  MIN = lambda xs: [min(x) for x in xs]
  SUM = lambda xs: [sum(x) for x in xs]
  @staticmethod
  def fromString(s):
    xs = {
      'COUNT': AGGREGATE.COUNT,
      'FIRST': AGGREGATE.FIRST,
      'MAX': AGGREGATE.MAX,
      'MEAN': AGGREGATE.MEAN,
      'MIN': AGGREGATE.MIN,
      'SUM': AGGREGATE.SUM,
    }
    if s.upper() in xs.keys():
      return xs[s.upper()]
    return None

class VISUALIZATION_TYPE:
  BAR_CHART = 'BAR_CHART'
  BOX_PLOT = 'BOX_PLOT'
  TEXT_COLLECTION = 'TEXT_COLLECTION'
