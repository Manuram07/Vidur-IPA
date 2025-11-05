"""
Example test file for RAM-IPA project.
This demonstrates how to structure tests.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

def test_example():
    """Basic test example."""
    # This is a placeholder test
    # Replace with actual tests for your code
    assert True, "This test should pass"

def test_basic_math():
    """Example of a simple assertion test."""
    result = 2 + 2
    assert result == 4, "Basic math should work"

if __name__ == "__main__":
    print("Running example tests...")
    test_example()
    test_basic_math()
    print("All tests passed!")
