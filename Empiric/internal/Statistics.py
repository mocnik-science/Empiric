import copy
import json
from jsonpath_ng import parse
import os

from Empiric.internal.GeneralSettings import GeneralSettings
from Empiric.internal.ManuscriptMemory import ManuscriptMemory
from Empiric.Statistics import AGGREGATE, VISUALIZATION_TYPE

class Tools:
  @staticmethod
  def _flatten(xss):
    return [x for xs in xss for x in xs]
  @staticmethod
  def apply(x, selector):
    for y in parse(selector).find(x):
      return y.value
    return None
  @staticmethod
  def find(x, selector, fFilter):
    return [match.value for match in parse(selector).find(x) if fFilter(match.value)]
  @staticmethod
  def filterFn(xs, f):
    return list(filter(f, xs))
  @staticmethod
  def map(xs, selector):
    return Tools.mapFn(xs, lambda x: [y.value for y in parse(selector).find(x)])
  @staticmethod
  def mapFn(xs, f):
    return [f(x) for x in xs]

class Statistics:
  @staticmethod
  def _flattenStatistics(statistics):
    def transform(s):
      if 'substatistics' not in s:
        return s
      result = []
      s2 = copy.deepcopy(s)
      del s2['substatistics']
      for sub in s['substatistics']:
        sub = GeneralSettings.fixKeyTitle(sub)
        if 'title' in sub:
          sub['subtitle'] = sub['title']
          del sub['title']
        if 'key' in sub:
          sub['subkey'] = sub['key']
          del sub['key']
        result.append({
          **s2,
          **sub,
        })
      return result
    result = {}
    for s in Tools._flatten([transform(s) for s in statistics.values()]):
      if s['key'] not in result:
       result[s['key']] = []
      result[s['key']].append(s)
    return result
  @staticmethod
  def _readData():
    data = []
    for filename in sorted(os.listdir(ManuscriptMemory._pathCollectedData)):
      if filename.endswith('.json'):
        with open(os.path.join(ManuscriptMemory._pathCollectedData, filename), 'r') as f:
          data.append(json.load(f))
    return data
  @staticmethod
  def _computeStatisticsKeys(data):
    statisticKeys = []
    statisticKeysAll = [list(enumerate([match.value for match in parse('$.memory.*.statistics').find(d)])) for d in data]
    statisticKeysAll = [[x for x in ska if x[1] is not None] for ska in statisticKeysAll]
    m = max(*[len(ska) for ska in statisticKeysAll]) + 1
    tmp = [[] for _ in range(m + 1)]
    for ska in statisticKeysAll:
      for i, s in ska:
        tmp[i].append(s)
    while len(tmp) > 0:
      tmp = [ska for ska in tmp if len(ska) > 0]
      if len(tmp) > 0:
        s = tmp[0][0]
        statisticKeys.append(s)
        tmp = [[x for x in ska if x != s] for ska in tmp]
    return statisticKeys
  @staticmethod
  def _prepareData(data, statisticsKeys, statistics):
    result = []
    for s in statisticsKeys:
      if s not in statistics:
        continue
      for s2 in statistics[s]:
        s2 = s2['data']
        if 'selector' not in s2 or not ('aggregateByPage' in s2 or ('aggregateByKey' in s2 and 'value' in s2)):
          continue
        xs = []
        for d in data:
          x = Tools.find(d, '$.memory.*', lambda v: v['statistics'] == s)
          x = Tools.mapFn(x, lambda v: v['result'])
          xs.extend(x)
        xs = Tools.map(xs, '$.' + s2['selector'])
        if 'aggregateByPage' in s2:
          if 'defaultValue' in s2:
            xs = [(x if len(x) > 0 else [s2['defaultValue']]) for x in xs]
          else:
            xs = Tools.filterFn(xs, lambda x: len(x) > 0)
          result.append((s, AGGREGATE.fromString(s2['aggregateByPage'])(xs), s2, None))
        elif 'aggregateByKey' in s2 and 'value' in s2:
          xs = Tools.filterFn(xs, lambda x: len(x) > 0)
          rs = {}
          print('---')
          for x in xs:
            for x2 in x:
              key = Tools.apply(x2, '$.' + s2['aggregateByKey'])
              value = Tools.apply(x2, '$.' + s2['value'])
              if 'defaultValue' in s2:
                value = value if value else s2['defaultValue']
              if value is not None:
                if key not in rs:
                  rs[key] = [value]
                else:
                  rs[key].append(value)
          for key, r in rs.items():
            result.append((s, r, s2, key))
    return result
  @staticmethod
  def _visualize(key, data, settings, key2=None):
    print(key, key2, data, settings)
  def runAnalysis(self, manuscript):
    statistics = GeneralSettings().get('statistics')
    statistics = Statistics._flattenStatistics(statistics)
    data = Statistics._readData()
    statisticsKeys = Statistics._computeStatisticsKeys(data)
    dataPrepared = Statistics._prepareData(data, statisticsKeys, statistics)
    for d in dataPrepared:
      Statistics._visualize(*d)
