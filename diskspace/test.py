from diskspace import bytes_to_readable, print_tree, show_space_list,subprocess_check_output
import unittest
<<<<<<< HEAD
import subprocess

class TestMethods(unittest.TestCase):
=======


class TestStringMethods(unittest.TestCase):
>>>>>>> b060faeaec42e12fc9ab72ea3a0f163b079b1ba4

    def test_bytes_to_readable(self):
        blocks = 10
        result = (blocks/2)
        result = str(format(result,'.2f'))+'Kb'
        self.assertEqual(bytes_to_readable(blocks),result)
<<<<<<< HEAD
    #def test_subprocess_check_output(self):
        #string = "/unittest tecprog"
        #result = subprocess.check_output(string.strip().split(' '))
        #self.assertEqual(result,['/unittest','tecprog'])
=======
    def test_subprocess_check_output(self):
        string = "/unittest tecprog"
        result = subprocess_check_output(string)
        self.assertEqual(result,['/unittest'])
>>>>>>> b060faeaec42e12fc9ab72ea3a0f163b079b1ba4
    
#    def test_print_tree(self):

 #       self.assertEqual()

 #   def test_show_space_list(self):
 #       self.assertEqual()
#class TestListMethods(unittest.TestCase):


if __name__ == '__main__':
    unittest.main()
