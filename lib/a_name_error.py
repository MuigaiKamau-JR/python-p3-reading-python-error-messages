#!/usr/bin/env python3

def test_name_error(self):
    '''
    checks if the function "my_function" is defined
    '''
    runpy.run_path('lib/a_name_error.py')
    assert 'my_function' in locals()
