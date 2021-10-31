### Github workflow 

#### Installing git 

Before working with Github, you will need to install git on your machine. Directions depending on operating system can be found [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). 

#### Getting the project 

To get the project, you will need to download the code as a zip file and unzip it, or use the command line. 

```
git clone https://github.com/jtkaufman737/CMSC-495.git # creates a folder with the code 
cd CMSC-495                                            # enters the folder 
```

#### Workflow basics 

When you begin working on a new piece of code, the first thing you want to do is make sure you are on the main branch, and pull the latest updates from github. 

```
git pull origin main
```

You then will check out a "feature branch", conceptually this is like a separate folder for you to do your work without interrupting the main code base. 

```
git checkout -b new-feature
```

When you make changes and are ready for the code to be synced to the main branch that is kind of our pristine reference copy of all the working code, you are going to _commit_ your code changes (save them), _push_ your branch up to Github, where we will use a _pull request_ to combine your new code with what is in the main branch. 

```
git add .                                                # tells git to include all changes for the save
git commit -m "a message about what change I just made"  # committing = saving 
git pull --rebase origin main                            # get the latest from main one last time 
git push origin new-feature                              # this pushes your "branch" or folder to Github
```

From here, you can go to Github in the browser and will see a banner message at the top of the screen saying that your new branch was pushed up x minutes ago, with a green button to open a pull request.

When you open a pull request, tag the other project members to let them review and test the code. One or both group members will approve the code and merge it into the main branch again. 

**Because there are a few of us, this is why it is very important to do a git pull before beginning your work, so you always have the latest stuff!** 
