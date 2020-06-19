#!/usr/bin/python

import sys
import os
import optparse

# Tool to zip repos from command line with following command
# ./zip-repos_simple.py -l <login_name>:<password> -all -b <branch-suffix>

def zip (project, repos, zip_name, login_str, branch):
    cloneHTTPS = "git clone http://"
    github ="github.com/00qnavry00/"

    # if there is only one repo in the repos list, there is no need to create a project directory
    if len(repos) == 1:
        repo = repos[0]
        print "\n Cloning " + repo + " repo, branch " + branch + "\n"

        os.system(cloneHTTPS + login_str + github + project + '/' + repo + '.git -b' + branch)
        if os.path.exists(repo):
            os.system('rm -rf %s/.git' % repo)
            os.system('zip -r9 %s.zip %s' % (zip_name, repo))
            os.system('rm -rf %s' % repo)

    else:
        os.makedirs(zip_name)
        os.chdir(zip_name)

        for repo in repos:
            print "\n Cloning " + repo + " repo, branch " + branch + "\n"
            os.system(cloneHTTPS + login_str + bitbucket + project + '/' + repo + '.git -b' + branch)
            if os.path.exists(repo):
                os.system('rm -rf %s/.git' % repo)

        os.chdir('../')
        os.system('zip -r9 %s.zip %s' % (zip_name, zip_name))
        os.system('rm -rf %s' % zip_name)
    

## Assuming that xx.x branch value is only reserved for release branches
## If not float value is entered, entered value is assumed to be an existing branch name (Ex.: master, develop)
def full_branch_name(branch, char):
    branch_name = branch
    try:
    	float(branch)
        branch_name = 'release' + char + branch
    	return branch_name
    except ValueError:
    	return branch_name

def main(argv=None):

    if argv is None:
        argv = sys.argv[1:]

    try:

        if not "-l" in argv:
            print "\nPlease add '-l <login_name>:<password>' as argument to this script for authentication.\n"

            sys.exit()
        else:
            i = argv.index("-l")
            login = argv[i+1]
            
            if not len(login) or not ':' in login:
                print "\nPlease provide login info in the following format: -l <login_name>:<password>\n"
                sys.exit()

        if not "-b" in argv:
            print "\nSince '-b <branch_name>' is not specified, we will zip master branch.\n"
            branch = 'master'
        else:
            i = argv.index("-b")
            branch = argv[i+1]

        repo_list = ""
        if "-repo" in argv:
            i = argv.index("-repo")
            repo_list = argv[i+1].lower()
        else:
            print "\nPlease include '-repo <repo names>' separated by white spaces as the script arguments."

        if "-all" in argv or 'application1' in repo_list:
            # Create zip file with application1 repo
            zip('project_name1', ['application1'], 'zip_name1', login, full_branch_name(branch, '/'))

        if "-all" in argv or 'application2' in repo_list:
            # Create zip file with application2 repo
            zip('project_name2', ['application2'], 'zip_name2', login, full_branch_name(branch, '-'))

    except Exception, err:
        print err

if __name__ == "__main__":
    sys.exit(main())

