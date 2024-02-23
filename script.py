import getpass
import os
import subprocess
import traceback

if __name__=="__main__":
    print('hello')
    print(getpass.getuser())

    try:
        subprocess.run(
            ["git", "rev-parse", "HEAD^@"], capture_output=True
        )
    except Exception as e:
        print(e.message)
        print(e)
        print(traceback.print_exc())
