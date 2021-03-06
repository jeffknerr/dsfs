
import os.path
import sys
sys.path.append("../linearalgebra")
from vectors import *

from collections import Counter
from matplotlib import pyplot as plt
import math

# from Joel's repo

num_friends = [100,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

daily_minutes = [1,68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,54.01,38.79,47.59,49.1,27.66,41.03,36.73,48.65,28.12,46.62,35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,20.45,21.93,26.02,27.34,23.49,46.94,30.5,33.8,24.23,21.4,27.94,32.24,40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,26.97,36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,36.07,28.66,29.08,37.28,15.28,24.17,22.31,30.17,25.53,19.85,35.37,44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,28.77,24.26,31.98,25.73,24.86,16.28,34.51,15.23,39.72,40.8,26.06,35.76,34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,14.18,35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,27.61,27.21,26.61,29.77,20.59,27.53,13.82,33.2,25,33.1,36.65,18.63,14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,19.42,29.79,32.8,35.99,28.32,27.79,35.88,29.06,36.28,14.1,36.63,37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,32.51,25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,20.42,27.32,18.23,35.35,28.48,9.08,24.62,20.12,35.26,19.92,31.02,16.49,12.16,30.7,31.22,34.65,13.13,27.51,33.2,31.57,14.1,33.42,17.44,10.12,24.42,9.82,23.39,30.93,15.03,21.67,31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]

def make_friend_counts_histogram(num_friends):
  """bar plot of list"""
  friend_counts = Counter(num_friends)
  print(friend_counts)
  xs = list(range(num_friends[0] + 1))
  ys = [friend_counts[x] for x in xs]
  print(xs)
  print(ys)
  plt.bar(xs,ys)
  plt.axis([0,101,0,25])
  plt.title("Histogram of Friend Counts")
  plt.xlabel("# of friends")
  plt.ylabel("# of people")
  plt.show()

#make_friend_counts_histogram(num_friends)

def mean(L):
  """return mean of a list"""
  return sum(L)/len(L)


def median(L):
  """find middle value of list"""
  n = len(L)
  sortedL = sorted(L)
  mid = n//2
  if n%2 == 1:
    return sortedL[mid]
  else:
    return (sortedL[mid-1] + sortedL[mid])/2.0

def quantile(L,p):
  """return value that p% of data is less than"""
  index = int(p*len(L))
  return sorted(L)[index]

def mode(L):
  """return most-common value"""
  counts = Counter(L)
  maxc = max(counts.values())
  mlist = []
  for i,count in counts.items():
    if count == maxc:
      mlist.append(i)
  return mlist

def data_range(L):
  """return max minus min"""
  return max(L) - min(L)

def de_mean(L):
  """subtract mean from all of L, so new list has mean of 0"""
  x_bar = mean(L)
  return [x-x_bar for x in L]

def variance(L):
  """how a single variable deviates from the mean"""
  # assumes L has at least 2 items
  n = len(L)
  deviations =de_mean(L)
  result = sum_of_squares(deviations)/(n-1)
  return result

def standard_deviation(L):
  return math.sqrt(variance(L))

def interquartile_range(L):
  """diff between 75th and 25th percentile"""
  return quantile(L,0.75) - quantile(L,0.25)

def covariance(L1,L2):
  """how two variables vary in tandem from their means"""
  n = len(L1)
  return dot(de_mean(L1), de_mean(L2)) / (n-1)

def correlation(x,y):
  """1 means perfect correlation, -1 means perfect anit-correlation"""
  stdx = standard_deviation(x)
  stdy = standard_deviation(y)
  if stdx>0 and stdy>0:
    return covariance(x,y) / stdx / stdy
  else:
    return 0

#############################################################

import unittest

class TestStats(unittest.TestCase):

    def test_mean(self):
        m = mean(num_friends)
        self.assertAlmostEqual(m,7.33333,places=5)

    def test_median(self):
        m = median(num_friends)
        self.assertAlmostEqual(m,6.00000,places=5)
        m = median([1,2,3])
        self.assertAlmostEqual(m,2.0,places=1)
        m = median([1,2,3,4])
        self.assertAlmostEqual(m,2.5,places=1)

    def test_quantile(self):
        q = quantile(num_friends,.10)
        self.assertEqual(q,1)
        self.assertEqual(quantile(num_friends,.25),3)
        self.assertEqual(quantile(num_friends,.75),9)
        self.assertEqual(quantile(num_friends,.90),13)

    def test_mode(self):
        self.assertEqual(mode(num_friends),[6,1])
        self.assertEqual(mode([2,2,2,3]),[2])
        L = [1,2,3,4]
        self.assertEqual(mode(L),L)
        L = [1,4,2,3,4]
        self.assertEqual(mode(L),[4])
        self.assertEqual(mode([1]),[1])

    def test_range(self):
        self.assertEqual(data_range(num_friends),99)
        self.assertEqual(data_range([1]),0)
        self.assertEqual(data_range([1,2]),1)

    def test_variance(self):
        self.assertAlmostEqual(variance(num_friends),81.54,places=2)
        self.assertAlmostEqual(standard_deviation(num_friends),9.03,places=2)
        self.assertEqual(interquartile_range(num_friends),6)

    def test_covariance(self):
        self.assertAlmostEqual(covariance(num_friends,daily_minutes),22.43,places=2)
    def test_correlation(self):
        self.assertAlmostEqual(correlation(num_friends,daily_minutes),0.25,places=2)
        # remove the outlier
        L1 = num_friends.copy()
        L1.pop(0)
        L2 = daily_minutes.copy()
        L2.pop(0)
        self.assertAlmostEqual(correlation(L1,L2),0.57,places=2)

if __name__ == '__main__':
    unittest.main()

#############################################################
