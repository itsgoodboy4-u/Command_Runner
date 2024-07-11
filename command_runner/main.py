import subprocess

commands = list(input("Enter the list of commands in sequence to execute: "))
dir_to_save = input("Enter the directory where to save: ")
if (len(dir_to_save) < 2):
    print("Your file will be saved in the same direcotry where this python file is present.")



def make_script_executable(script_path):
    """Make the shell script executable."""
    try:
        subprocess.run(['chmod', '+x', script_path], check=True)
        print(f"Made {script_path} executable.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while changing script permissions: {e}")

def run_shell_script(script_path):
    """Run a shell script from the specified path."""
    try:
        result = subprocess.run(['bash', script_path], check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running the script: {e}")
        print(e.stderr)


if __name__ == '__main__':
    script_path = './example.sh'
    make_script_executable(script_path)
    run_shell_script(script_path)
