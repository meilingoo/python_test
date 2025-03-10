利用python进行测试时，测试用例的加载方式有2种：
  一种是通过unittest.main()来启动所需测试的测试模块；
  一种是添加到testsuite集合中再加载所有的被测试对象，而testsuit里存放的就是所需测试的用例，下面分别列出3种方法的具体使用方式：
## 1、通过unittest.main()来执行测试用例的方式：

```
import unittest 

class UCTestCase(unittest.TestCase):
    def setUp(self):
        #测试前需执行的操作
        .....      
    def tearDown(self):
        #测试用例执行完后所需执行的操作
        .....      
    # 测试用例1
    def testCreateFolder(self):
        #具体的测试脚本
        ......      
    # 测试用例2
    def testDeleteFolder(self):
        #具体的测试脚本
        ......       
if __name__ == "__main__":
    unittest.main()
```

## 2、通过testsuit来执行测试用例的方式：

```
import unittest 
# 执行测试的类
class UCTestCase(unittest.TestCase):
    def setUp(self):
        #测试前需执行的操作
        .....       
    def tearDown(self):
        #测试用例执行完后所需执行的操作
        .....
       
    # 测试用例1
    def testCreateFolder(self):
        #具体的测试脚本
        ......      
    # 测试用例2
    def testDeleteFolder(self):
        #具体的测试脚本
        ......       
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(UC7TestCase("testCreateFolder"))
    suite.addTest(UC7TestCase("testDeleteFolder")) 
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
```

## 3、通过testLoader方式：

```
import unittest 
class TestCase1(unittest.TestCase):
    #def setUp(self):
    #def tearDown(self):
    def testCase1(self):
        print 'aaa'      
    def testCase2(self):
        print 'bbb'
  
class TestCase2(unittest.TestCase):
    #def setUp(self):
    #def tearDown(self):
    def testCase1(self):
        print 'aaa1'  
    def testCase2(self):
        print 'bbb1'
        
if __name__ == "__main__":
    #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestCase1) 
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2) 
    suite = unittest.TestSuite([suite1, suite2]) 
    unittest.TextTestRunner(verbosity=2).run(suite)
 ```

### 下面针对上述脚本中应用到的unittest模块下的几个成员进行简单的介绍，以便于理解上述代码：
 **TestCase**：所有测试用例的基本类，给一个测试方法的名字，就会返回一个测试用例实例；
 **TestSuit**：组织测试用例的实例，支持测试用例的添加和删除，最终将传递给  testRunner进行测试执行；
 **TextTestRunner**：进行测试用例执行的实例，其中Text的意思是以文本形式显示测试结果。测试的结果会保存到TextTestResult实例中，包括运行了多少测试用例，成功了多少，失败了多少等信息；
 **TestLoader**：用来加载TestCase到TestSuite中的，其中有几个  loadTestsFrom__()方法，就是从各个地方寻找TestCase，创建它们的实例，然后add到TestSuite中，再返回一个TestSuite实例；

 

原文：http://www.51testing.com/html/10/448910-3648852.html
