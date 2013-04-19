# -*- coding: utf-8 -*-

from retry import retry, RetryExceededError
from unittest import TestCase, main

class RetryTest(TestCase):

    def setUp(self):
        self.current_try = 0

    def test_retry(self):
        @retry(errors=(ZeroDivisionError, KeyError), tries=3)
        def f():
            self.current_try += 1
            if self.current_try == 1:
                return 1 / 0
            elif self.current_try == 2:
                return dict()['key']
            else:
                return "Got it on last try!"
        self.assertEquals(f(), "Got it on last try!")
        self.assertEquals(self.current_try, 3)

    def test_retry_exceeded(self):
        @retry(errors=(ZeroDivisionError, ), tries=3)
        def f():
            return 1 / 0

        self.assertRaises(RetryExceededError, f)

if __name__ == "__main__":
    main()
