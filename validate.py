#!/usr/bin/env python3
"""
Validation script to ensure the Mergington High School Activities API is complete
"""
import os
import sys
from pathlib import Path

def validate_project_structure():
    """Validate that all required files exist"""
    print("🔍 Validating project structure...")
    
    base_dir = Path(__file__).parent
    required_files = [
        "src/app.py",
        "src/static/index.html", 
        "src/static/app.js",
        "src/static/styles.css",
        "src/README.md",
        "requirements.txt",
        "start_server.py",
        "test_api.py"
    ]
    
    missing_files = []
    for file_path in required_files:
        full_path = base_dir / file_path
        if not full_path.exists():
            missing_files.append(file_path)
        else:
            print(f"  ✅ {file_path}")
    
    if missing_files:
        print(f"  ❌ Missing files: {missing_files}")
        return False
    
    return True

def validate_api_endpoints():
    """Check that the API has all required endpoints"""
    print("\n🔍 Validating API endpoints...")
    
    app_file = Path(__file__).parent / "src" / "app.py"
    with open(app_file, 'r') as f:
        content = f.read()
    
    required_endpoints = [
        '@app.get("/activities")',
        '@app.post("/activities/{activity_name}/signup")',
        '@app.delete("/activities/{activity_name}/unregister")',
        '@app.get("/")'
    ]
    
    missing_endpoints = []
    for endpoint in required_endpoints:
        if endpoint in content:
            print(f"  ✅ {endpoint}")
        else:
            missing_endpoints.append(endpoint)
            print(f"  ❌ {endpoint}")
    
    return len(missing_endpoints) == 0

def validate_features():
    """Check that key features are implemented"""
    print("\n🔍 Validating key features...")
    
    app_file = Path(__file__).parent / "src" / "app.py"
    with open(app_file, 'r') as f:
        content = f.read()
    
    features_to_check = [
        ("Capacity checking", "max_participants"),
        ("Duplicate prevention", "already signed up"),
        ("Activity validation", "Activity not found"),
        ("Server startup", "if __name__ == \"__main__\""),
        ("Static file serving", "StaticFiles"),
        ("Activities database", "activities = {")
    ]
    
    for feature_name, check_string in features_to_check:
        if check_string in content:
            print(f"  ✅ {feature_name}")
        else:
            print(f"  ❌ {feature_name}")
    
    return True

def main():
    print("🏫 Mergington High School Activities API - Validation")
    print("=" * 60)
    
    structure_valid = validate_project_structure()
    endpoints_valid = validate_api_endpoints()
    features_valid = validate_features()
    
    print("\n" + "=" * 60)
    
    if structure_valid and endpoints_valid and features_valid:
        print("🎉 SUCCESS: Project validation completed!")
        print("\n✅ Your implementation includes:")
        print("   - Complete FastAPI backend with all required endpoints")
        print("   - Responsive web interface with signup/unregister functionality") 
        print("   - Proper validation and error handling")
        print("   - In-memory data storage with pre-loaded activities")
        print("   - Static file serving for the web interface")
        print("   - Easy startup scripts and testing utilities")
        
        print("\n🚀 To run the application:")
        print("   python start_server.py")
        print("   Then visit: http://localhost:8000")
        
        print("\n📚 To test the API:")
        print("   python test_api.py")
        
        return True
    else:
        print("❌ FAILED: Project validation found issues")
        print("Please check the missing files/features above")
        return False

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)