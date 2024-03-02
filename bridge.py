import re
import sys
import subprocess
from pathlib import Path

"""
bridge between django & react
"""
react_path = Path("frontend")


def bridge():
    """
    Synchronize React and Django when changes are made to React.
    stop your django server first.
    """
    if sys.argv[1] == "update":
        subprocess.run("rm -rf dist", shell=True, check=True, cwd=react_path)
        base_toggle()
        subprocess.run("npm run build", shell=True, check=True, cwd=react_path)
        base_toggle()
        subprocess.run("python manage.py collectstatic --noinput", shell=True, check=True, cwd=".")
        subprocess.run("python manage.py runserver", shell=True, check=True, cwd=".")

    elif sys.argv[1] == "build":
        """
        Build the react with correct base variable
        """
        base_toggle()
        subprocess.run("npm run build", shell=True, check=True, cwd=react_path)
        base_toggle()
        print("-------------------------\ncommand: 'build' SUCCESS\n-------------------------")
        

def base_toggle():
    """
    comment toggle on the `base` variable in `vite.config.js` for Django static file purposes.
    """
    file_path = react_path.joinpath('vite.config.js')
    with open(file_path, 'r') as file:
        lines = file.readlines()
    pattern = re.compile(r'^(\s*//)?(\s*base: .*)$')
    new_lines = []
    for line in lines:
        match = pattern.match(line)
        # Comment togle
        if match:
            if match.group(1): 
                # Uncomment
                new_line = match.group(2) + '\n'
            else:
                # Comment
                new_line = '//' + match.group(2) + '\n'
            new_lines.append(new_line)
        # just rewrite
        else:
            new_lines.append(line)

    # rewrite
    with open(file_path, 'w') as file:
        file.writelines(new_lines)
