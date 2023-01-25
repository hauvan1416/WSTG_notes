import subprocess

def launch_tools():
    url = input("Enter the URL: ")
    with open("Result.json", "w") as outfile:
        subprocess.run(["nuclei", "-t", url], stdout=outfile)
        subprocess.run(["naabu", "-d", url], stdout=outfile)
        subprocess.run(["subfinder", "-d", url], stdout=outfile)

launch_tools()