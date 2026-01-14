import subprocess
from dotenv import dotenv_values
config = dotenv_values(".env")

def execute_remote_python(script_path: str, args: list) -> bool:
    try:
        cmd = f"sudo {config['LIGHT_SERVER_REPO_PATH']}/.venv/bin/python3 {script_path} {' '.join(args)} > /dev/null 2>&1 &"
        subprocess.run(["ssh", f"{config['LIGHT_SERVER_USER']}@{config['LIGHT_SERVER_HOST']}", "sudo pkill -9 python"])
        subprocess.run(["ssh", f"{config['LIGHT_SERVER_USER']}@{config['LIGHT_SERVER_HOST']}", cmd], timeout=10)
        return True
            
    except subprocess.TimeoutExpired:
        print("Remote execution timed out")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
