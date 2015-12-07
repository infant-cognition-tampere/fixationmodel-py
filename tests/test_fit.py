# -*- coding: utf-8 -*-
from tests import fixtures
import fixationmodel
import unittest2 as unittest  # to support Python 2.6

class TestFit(unittest.TestCase):

    def test_run(self):
        '''
        should run and give correct answers in trivial case
        '''
        X = fixtures.load('synthetic_fixation')
        r = fixationmodel.fit(X)
        self.assertEqual(r['centroid'], [0.0, 0.0])
        self.assertEqual(r['mean_squared_error'], 0.0)

    def test_centroid(self):
        '''
        should give correct answers in nontrivial case
        '''
        X = fixtures.load('synthetic_microsaccade')
        r = fixationmodel.fit(X)
        self.assertEqual(r['centroid'], [0.4, 0.4])
        self.assertAlmostEqual(r['mean_squared_error'], 3.68)

    def test_gaps(self):
        '''
        should ignore [None, None] points
        '''
        X = fixtures.load('synthetic_gapped')  # Gaps added to microsaccade
        r = fixationmodel.fit(X)
        self.assertEqual(r['centroid'], [0.4, 0.4])
        self.assertAlmostEqual(r['mean_squared_error'], 3.68)

if __name__ == '__main__':
    unittest.main()
