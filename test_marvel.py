#!/usr/bin/env python3
"""
Test script for Marvel Comics application
Tests the authentication hash generation logic
"""

import hashlib
import time
from marvel_comics import MarvelComicsAPI


def test_auth_hash_generation():
    """Test that the MD5 hash is generated correctly"""
    
    PUBLIC_KEY = "c9b342b95e7fdb1c01efcea39f8e65e7"
    PRIVATE_KEY = "9d15e7cf75996f595ce74aa89ebc089fb19b9e34"
    
    # Create API client
    api = MarvelComicsAPI(PUBLIC_KEY, PRIVATE_KEY)
    
    # Test hash generation
    params = api._generate_auth_params()
    
    print("Testing Marvel API Authentication...")
    print(f"Timestamp: {params['ts']}")
    print(f"API Key: {params['apikey']}")
    print(f"Hash: {params['hash']}")
    
    # Verify the hash is 32 characters (MD5)
    assert len(params['hash']) == 32, "Hash should be 32 characters (MD5)"
    
    # Verify API key is correct
    assert params['apikey'] == PUBLIC_KEY, "API key should match"
    
    # Verify hash calculation manually
    hash_input = params['ts'] + PRIVATE_KEY + PUBLIC_KEY
    expected_hash = hashlib.md5(hash_input.encode('utf-8')).hexdigest()
    assert params['hash'] == expected_hash, "Hash should match expected value"
    
    print("\n✓ All authentication tests passed!")
    print("\nHash generation formula verified:")
    print(f"  MD5({params['ts']} + {PRIVATE_KEY} + {PUBLIC_KEY})")
    print(f"  = {params['hash']}")
    
    return True


def test_mock_display():
    """Test display function with mock data"""
    
    PUBLIC_KEY = "c9b342b95e7fdb1c01efcea39f8e65e7"
    PRIVATE_KEY = "9d15e7cf75996f595ce74aa89ebc089fb19b9e34"
    
    api = MarvelComicsAPI(PUBLIC_KEY, PRIVATE_KEY)
    
    # Mock data similar to Marvel API response
    mock_data = {
        "data": {
            "results": [
                {
                    "title": "Iron Man (2020) #1",
                    "description": "Tony Stark is Iron Man, technological visionary, wealthy playboy, unparalleled engineer, and armored Avenger.",
                    "images": [
                        {
                            "path": "http://i.annihil.us/u/prod/marvel/i/mg/6/60/5e3d7536c8ada",
                            "extension": "jpg"
                        }
                    ]
                },
                {
                    "title": "Iron Man (2020) #2",
                    "description": "The armored Avenger continues his adventures!",
                    "images": []
                }
            ]
        }
    }
    
    print("\n\nTesting comic display with mock data...")
    print("-" * 80)
    api.display_comics(mock_data)
    print("-" * 80)
    print("✓ Display function works correctly!")
    
    return True


if __name__ == "__main__":
    print("="*80)
    print("Marvel Comics Python Application - Test Suite")
    print("="*80 + "\n")
    
    try:
        test_auth_hash_generation()
        test_mock_display()
        
        print("\n" + "="*80)
        print("All tests passed successfully! ✓")
        print("="*80)
        print("\nNote: Actual API calls cannot be tested in this environment")
        print("due to network restrictions, but the code logic is verified.")
        
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        exit(1)
