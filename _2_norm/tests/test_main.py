#!/bin/python3

import unittest

class Test(unittest.TestCase):
    

    def setUp(self):
        from src.main import get_config
        self.config = get_config()

    def test_config(self):
        self.assertIsInstance(self.config, dict)

        self.assertIn('paths', self.config )
        self.assertIsInstance(self.config['paths'], dict)
        paths = self.config['paths']

        self.assertIn('data/input', paths['input_dir'])
        self.assertIn('data/output', paths['output_dir'])
        self.assertIn('logs', paths['log_dir'])

        self.assertIn('logging', self.config)
        self.assertIsInstance(self.config['logging'], dict)
        self.assertIn('INFO', self.config['logging']['level'])

        self.assertIn('excel', self.config)
        self.assertIsInstance(self.config['excel'], dict)
        self.assertIn('default_extension', self.config['excel'])
        # Use assertEqual for value comparison. assertIs checks object identity
        # (the same object), which is not guaranteed for strings even if they
        # have the same contents.
        self.assertEqual('.xlsx', self.config['excel']['default_extension'])
    
        
if __name__ == '__main__':
    unittest.main()
