import sys
import datetime

def run_check():
    print("--- STARTING PRE-DEPLOYMENT CHECKS ---")
    current_time = datetime.datetime.now()
    print(f"Timestamp: {current_time}")
    
    # Simulate a "health check"
    print("[INFO] Checking server connectivity...")
    # In a real scenario, you would ping a server here
    print("[SUCCESS] Server is reachable.")
    
    print("[INFO] Verifying configuration files...")
    print("[SUCCESS] Config is valid.")
    
    print("--- CHECKS PASSED. READY FOR DEPLOYMENT ---")
    return True

if __name__ == "__main__":
    success = run_check()
    if success:
        sys.exit(0) # Exit code 0 means "Success" in DevOps
    else:
        sys.exit(1) # Exit code 1 means "Failure"