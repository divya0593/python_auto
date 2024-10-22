# import unittest
from testCases.setup import testSetup

class testname1(testSetup):
    def test_P1_abc(self):
        test = {
            'priority'   : "P1",                   #test case priority
            'id'         : "SPC-TC-17",          #test case zypher id
            'description': "spim e2e flow 1",      #test case description
            'author'     : "tester1"               #author
        }
        #log details to klov reporter
        self.testReporterObj.config(**test)
        
        print("hello world")

    def test_P2_abc(self):
        test = {
            'priority'   : "P2",                   #test case priority
            'id'         : "test_P2_abc",          #test case zypher id
            'description': "spim e2e flow 1",      #test case description
            'author'     : "tester1"               #author
        }
        #log details to klov reporter
        self.testReporterObj.config(**test)
        print("hello world")

    def test_P3_abc(self):
        test = {
            'priority'   : "P3",                   #test case priority
            'id'         : "test_P3_abc",          #test case zypher id
            'description': "spim e2e flow 1",      #test case description
            'author'     : "tester1"               #author
        }
        #log details to klov reporter
        self.testReporterObj.config(**test)
        print("hello world")