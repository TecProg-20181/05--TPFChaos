from diskspace import bytes_to_readable, print_tree, show_space_list,subprocess_check_output
import unittest
import subprocess
import os

class TestMethods(unittest.TestCase):

    def test_bytes_to_readable(self):
        result = ['512.00','128.00','256.00','512.00']
        blocks = [1,256,524288,1073741824]
        datatype = ['B','Kb','Mb','Gb']
        counter = 0
        for block in blocks:
           result[counter] = result[counter]+(datatype[counter])
           self.assertEqual(bytes_to_readable(block),result[counter])
           counter= counter +1
    
    def test_subprocess_check_output(self):
        depth = -1
        abs_directory = os.path.abspath('.')
        string = 'du '
        if depth != -1:
            string += '-d {} '.format(depth)
        
        string += abs_directory
        result = subprocess.check_output(string.strip().split(' '))
        self.assertEqual(subprocess_check_output(string),result)
    
            
    #def test_print_tree(self):
        
    #    self.assertEqual()

    #def test_show_space_list(self):

    #    self.assertEqual()

if __name__ == '__main__':
    unittest.main()
