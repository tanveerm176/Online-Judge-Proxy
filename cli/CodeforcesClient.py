import subprocess
import sys
import os

class CodeforcesClient:

    def submit(self, file, problemID):
        currentDir =  os.path.dirname(__file__)
        binaryPath = os.path.join(currentDir, "cf")
        print(binaryPath)
        subprocess.run([binaryPath, "submit", "-f", file, problemID])





