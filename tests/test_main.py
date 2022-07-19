#!/usr/bin/env python3

import yapps.main as yapps

def test_the_goog():
    assert yapps.main('google.com') == '172.217.4.78'

def test_valid_ip():
    assert yapps.main('192.168.0.1') == '192.168.0.1'

def test_non_existent_domain():
    assert yapps.main('frkejlahasdfjkhasjkfhasdlkjbflksjdhafvlkjdshfklsjavdsfajfh.com') == 'Name frkejlahasdfjkhasjkfhasdlkjbflksjdhafvlkjdshfklsjavdsfajfh.com not recognized. Aborting.'