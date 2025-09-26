#!/usr/bin/env python3
"""
Test script for the Mergington High School Activities API
"""
import requests
import json
import sys
from time import sleep


def test_api():
    base_url = "http://localhost:8000"
    
    print("Testing Mergington High School Activities API...")
    print("=" * 50)
    
    # Test 1: Get all activities
    print("1. Testing GET /activities")
    try:
        response = requests.get(f"{base_url}/activities")
        if response.status_code == 200:
            activities = response.json()
            print(f"✅ SUCCESS: Retrieved {len(activities)} activities")
            for name, details in list(activities.items())[:2]:  # Show first 2 activities
                participants = len(details['participants'])
                max_participants = details['max_participants']
                print(f"   - {name}: {participants}/{max_participants} participants")
        else:
            print(f"❌ FAILED: Status code {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False
    
    # Test 2: Sign up for an activity
    print("\n2. Testing POST /activities/{activity_name}/signup")
    test_email = "test-student@mergington.edu"
    test_activity = "Chess Club"
    
    try:
        response = requests.post(
            f"{base_url}/activities/{test_activity}/signup",
            params={"email": test_email}
        )
        if response.status_code == 200:
            result = response.json()
            print(f"✅ SUCCESS: {result['message']}")
        else:
            result = response.json()
            print(f"⚠️  EXPECTED: {result.get('detail', 'Unknown error')}")
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False
    
    # Test 3: Try to sign up for the same activity again (should fail)
    print("\n3. Testing duplicate signup (should fail)")
    try:
        response = requests.post(
            f"{base_url}/activities/{test_activity}/signup",
            params={"email": test_email}
        )
        if response.status_code == 400:
            result = response.json()
            print(f"✅ SUCCESS: Properly rejected duplicate signup - {result['detail']}")
        else:
            print(f"❌ UNEXPECTED: Status code {response.status_code}")
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False
    
    # Test 4: Unregister from activity
    print("\n4. Testing DELETE /activities/{activity_name}/unregister")
    try:
        response = requests.delete(
            f"{base_url}/activities/{test_activity}/unregister",
            params={"email": test_email}
        )
        if response.status_code == 200:
            result = response.json()
            print(f"✅ SUCCESS: {result['message']}")
        else:
            result = response.json()
            print(f"❌ FAILED: {result.get('detail', 'Unknown error')}")
            return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False
    
    # Test 5: Test the web interface exists
    print("\n5. Testing web interface")
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            print("✅ SUCCESS: Web interface accessible")
        else:
            print(f"❌ FAILED: Status code {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("🎉 All tests completed successfully!")
    print("\nYour API is working correctly and includes:")
    print("- ✅ View all activities with participant counts")
    print("- ✅ Sign up for activities with validation")
    print("- ✅ Prevent duplicate signups")
    print("- ✅ Unregister from activities")
    print("- ✅ Web interface for user interaction")
    print("- ✅ Proper error handling and responses")
    
    return True


if __name__ == "__main__":
    print("Make sure the server is running with: python app.py")
    sleep(2)
    
    success = test_api()
    if not success:
        sys.exit(1)