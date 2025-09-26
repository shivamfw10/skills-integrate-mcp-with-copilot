"""
Simple startup script for the Mergington High School Activities API
"""
import sys
import os
from pathlib import Path

# Add the src directory to the Python path
src_dir = Path(__file__).parent / "src"
sys.path.insert(0, str(src_dir))

try:
    from app import app
    import uvicorn
    
    print("🏫 Starting Mergington High School Activities API")
    print("📚 Available endpoints:")
    print("   - GET  /activities - View all activities")
    print("   - POST /activities/{activity_name}/signup?email=... - Sign up for activity")
    print("   - DELETE /activities/{activity_name}/unregister?email=... - Unregister from activity")
    print("   - GET  / - Web interface")
    print("   - GET  /docs - API documentation")
    print("\n🌐 Access the application at: http://localhost:8000")
    print("📖 API docs available at: http://localhost:8000/docs")
    print("\nPress Ctrl+C to stop the server\n")
    
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Make sure you're in the correct directory and have installed the requirements:")
    print("pip install -r requirements.txt")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error starting server: {e}")
    sys.exit(1)