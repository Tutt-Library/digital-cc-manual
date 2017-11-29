#!/home/jpnelson/jpn-py3-env/bin/python
"""Script pulls latest changes from github and runs mkdocs build"""
import subprocess

if __name__ == '__main__':
    subprocess.run("git pull origin master")
    subprocess.run("mkdocs build")
