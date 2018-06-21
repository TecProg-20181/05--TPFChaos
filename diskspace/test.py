from diskspace import bytes_to_readable, print_tree, show_space_list,subprocess_check_output
import unittest
import subprocess
import os

class TestMethods(unittest.TestCase):

    def test_bytes_to_readable(self):
        blocks = 10
        result = (blocks/2)
        result = str(format(result,'.2f'))+'Kb'
        self.assertEqual(bytes_to_readable(blocks),result)
    
    def test_subprocess_check_output(self):
        depth = -1
        abs_directory = os.path.abspath('.')
        string = 'du '
        if depth != -1:
            string += '-d {} '.format(depth)
        
        string += abs_directory
        result = subprocess.check_output(string.strip().split(' '))
        self.assertEqual(subprocess_check_output(string),result)
    
            
#    def test_print_tree(self):

 #       self.assertEqual()

 #   def test_show_space_list(self):
 #       self.assertEqual()
#class TestListMethods(unittest.TestCase):


if __name__ == '__main__':
    unittest.main()
