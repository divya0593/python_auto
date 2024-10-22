#======================= DO NOT ADD ANY THING HERE - START ====================
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir  = os.path.dirname(currentdir)
sys.path.append(parentdir)
#======================= DO NOT ADD ANY THING HERE - END ======================
from testCases.setup import testSetup
from parameterized  import parameterized
class logintest(testSetup):
    def test_1(self):
        pass

    def test_2(self):
        # invalid  user name & pass
        pass

    def test_3(self):
        # non registered  user name & pass
        pass

    #sample end to end test case  - SPIM API
#     @parameterized.expand([
#        ("negative", -1.5, -2.0)
#    ])
    def test_P1_first(self):
        a = [("test1", 1, 1, 2)]
            #  ("test2", 1, 1, 2),]
        for i in a:
            print("{}, {}, {}".format(i[0], i[1], i[2]))
        #test details to logged to klov reporter
        test = {
            'priority'   : "P1",                   #test case priority
            'id'         : i[0],          #test case zypher id
            'description': "spim e2e flow 1",      #test case description
            'author'     : "tester1"               #author
        }

        #log details to klov reporter
        self.testReporterObj.config(**test)
        # print("------------------->>>", i[0])
        # val = i[1] + i[2]
        # print("===========>> val: ", val)
        self.ui_assert(comparison="equal", actual=3, expected=2, testCaseObj=self, stopTest=False, klovReporterObj=self.testReporterObj, klovReporterMessage="step 1")

        
        # self.ui_assert(comparison="equal", actual=3, expected=2, testCaseObj=self, stopTest=False, klovReporterObj=self.testReporterObj, klovReporterMessage="step 1")
        # statement 1
        # statement 2
        # statement 3
        # self.ui_assert(comparison="equal", actual=4, expected=5, testCaseObj=self, stopTest=True, klovReporterObj=self.testReporterObj, klovReporterMessage="Step 2")
        # statement 1
        # statement 2
        # statement 3
        # self.ui_assert(comparison="equal", actual=6, expected=6, testCaseObj=self, stopTest=True, klovReporterObj=self.testReporterObj, klovReporterMessage="Step 3")

    def test_e2e2(self):
        #test details to logged to klov reporter
        test = {
            'priority'   : "P1",                   #test case priority
            'id'         : "SPC-TC-16",          #test case zypher id
            'description': "spim e2e flow 1",      #test case description
            'author'     : "tester1"               #author
        }

        #log details to klov reporter
        self.testReporterObj.config(**test)
        self.ui_assert(comparison="equal", actual=2, expected=2, testCaseObj=self, stopTest=True, klovReporterObj=self.testReporterObj, klovReporterMessage="step 1")
        self.ui_assert(comparison="equal", actual=3, expected=4, testCaseObj=self, stopTest=True, klovReporterObj=self.testReporterObj, klovReporterMessage="Step 2")
        self.ui_assert(comparison="equal", actual=6, expected=6, testCaseObj=self, stopTest=True, klovReporterObj=self.testReporterObj, klovReporterMessage="Step 3")
    
    
    def test_e2e3(self):
        #test details to logged to klov reporter
        test = {
            'priority'   : "P1",                   #test case priority
            'id'         : "SPC-TC-17",          #test case zypher id
            'description': "spim e2e flow 1",      #test case description
            'author'     : "tester1"               #author
        }

        #log details to klov reporter
        self.testReporterObj.config(**test)
        self.skipTest("another method for skipping")
        self.ui_assert(comparison="equal", actual=2, expected=2, testCaseObj=self, stopTest=True, klovReporterObj=self.testReporterObj, klovReporterMessage="step 1")
 
#============================== Test cases - END ==============================
if __name__ == '__main__':
    testSetup.main()