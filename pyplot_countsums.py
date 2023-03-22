import functools
import numpy
import matplotlib.pyplot
import timeit

def count_sums(a, t):
  @functools.cache
  def r(i, s):
    if i < 0:
      if s == 0:
        return 1
      else:
        return 0
    else:
      p = r(i - 1, s + a[i])
      m = r(i - 1, s - a[i])
      return p + m
  return r(len(a) - 1, t)

xs = numpy.linspace(10,210,num=20,dtype=int)
stmt = 'count_sums([1]*{}, 1)'
ys = [timeit.timeit(stmt.format(x), number=20, globals=globals()) for x in xs]
matplotlib.pyplot.plot(xs, ys, 'or')
matplotlib.pyplot.show()
