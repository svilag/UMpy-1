# Git branches

## VS Code extensions

Install [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens).

## 1.0 Creation

:exclamation: If you were unable to make the meeting and want to replicate this exercise on your
own you will need to create your own test directory and test files since the `git_branches`
directory and `git_branches.md` and `topics.md` files used during the talk have since been added to
the umsi-arwhyte UMpy repo.

Open your terminal and navigate to your Git cloned UMpy directory. Perform a `git pull` against
the upstream umsi-arwhyte UMpy directory to ensure that your working directory has the latest
changes. Then issue a `git push` and update your personal fork.

```commandline
git pull umsi-arwhyte UMpy
git push <remote alias > UMpy (e.g. git push arwhyte UMpy)
```

:exclamation: if you are unable to pull from the upstream umsi-arwhyte UMpy repo you are probably
missing a remote. Do the following:

1. Check existing remotes.

   ```commandline
   git remote -v
   ```

   ```commandline
   arwhyte git@github.com:arwhyte/UMpy.git (fetch)
   arwhyte git@github.com:arwhyte/UMpy.git (push)
   umsi-arwhyte    git@github.com:umsi-arwhyte/UMpy.git (fetch)
   umsi-arwhyte    git@github.com:umsi-arwhyte/UMpy.git (push)
   ```

2. More than likely the "umsi-arwhyte" remote is missing from the list. Add it:

   ```commandline
   git remote add umsi-arwhyte git@github.com:umsi-arwhyte/UMpy.git
   ```

3. Optional: if your fork's remote alias is named "origin" you can rename it to your Github
   account name (or any name actually). I renamed mine to arwhyte as I find it a more congenial
   alias.

   ```commandline
   git remote rename origin < new name >
   ```

4. Pull from the upstream umsi-arwhyte UMpy repo then push the changes to your fork.

   ```commandline
   git pull umsi-arwhyte UMpy
   git push <remote alias > UMpy
   ```

Now back to the exercise.

### 1.1 Display existing branches

#### Local only

```commandline
git branch
```

```commandline
* main
(END)
```

#### Local and remote branches

```commandline
git branch -a
```

```commandline
* main
  remotes/arwhyte/HEAD -> arwhyte/main
  remotes/arwhyte/main
  remotes/umsi-arwhyte/main
(END)
```

:bulb: Press "Q" key to quit display.

### 1.2 Create and checkout a branch

#### Create branch

Command: `git branch < name >`

```commandline
git branch git_branches
```

```commandline
git branch

```

```commandline
* git_branches
  main
(END)
```

#### Checkout branch

```commandline
git checkout git_branches
```

```commandline
Switched to branch 'git_branches'
```

:bulb: Check the latest commit of the branch as well as the status of the branch:

```commandline
git log
git status
```

:bulb: You can also create and checkout a branch with the following command:
`git checkout -b < new branch name >`. I prefer this command to create and checkout new
branches.

```commandline
git checkout -b git_branches
```

## 2.0 Modification

### 2.1 Setup

Create file (terminal example).

```commandline
cd talks
touch git_branches.md
```

```commandline
ls -la
```

```commandline
total 16
drwxr-xr-x  10 arwhyte  staff   320 Aug  6 09:24 .
drwxr-xr-x  12 arwhyte  staff   384 May 28 10:21 ..
-rw-r--r--@  1 arwhyte  staff  6148 Aug  6 08:51 .DS_Store
drwxr-xr-x   6 arwhyte  staff   192 May 28 12:44 dict_comp
drwxr-xr-x   3 arwhyte  staff    96 May 28 10:03 generators
-rw-r--r--   1 arwhyte  staff     0 Aug  6 09:24 git_branches.md
. . . .
```

### 2.2 Stage (add) and commit file

:bulb: Content to be provided.

```commandline
git status
git add git_branches.md
git commit -m "Add Git branching notes."
```

```commandline
[git_branches 0781c61] Add Git branching notes.
 1 file changed, 107 insertions(+)
 create mode 100644 talks/git_branches.md
 ```

### 2.3 Checkout `main`

```commandline
git checkout main
```

```commandline
Switched to branch 'main'
Your branch is up to date with 'arwhyte/main'.
```

Check contents of `/talks` directory:

```commandline
ls -la
```

Note that the file `git_branches.md` is no longer visible because its associated commit is
associated with the branch named `git_branches` _not_ `main`.

### 2.4 Checkout `git_branches`

```commandline
git checkout git_branches
```

File is visible again.

### 2.5 Move file to new directory talks/git_branches

```commandline
mkdir git_branches
ls -la
```

```commandline
total 24
drwxr-xr-x  11 arwhyte  staff   352 Aug  6 09:59 .
drwxr-xr-x  12 arwhyte  staff   384 May 28 10:21 ..
-rw-r--r--@  1 arwhyte  staff  6148 Aug  6 08:51 .DS_Store
drwxr-xr-x   6 arwhyte  staff   192 May 28 12:44 dict_comp
drwxr-xr-x   3 arwhyte  staff    96 May 28 10:03 generators
drwxr-xr-x   2 arwhyte  staff    64 Aug  6 09:59 git_branches
-rw-r--r--   1 arwhyte  staff  1777 Aug  6 09:56 git_branches.md
. . . .
```

```commandline
mv git_branches.md git_branches/
cd git_branches
ls -la
```

```commandline
total 8
drwxr-xr-x   3 arwhyte  staff    96 Aug  6 10:01 .
drwxr-xr-x  10 arwhyte  staff   320 Aug  6 10:01 ..
-rw-r--r--   1 arwhyte  staff  1777 Aug  6 09:56 git_branches.md
```

### 2.5 Stage and commit file

```commandline
git status
git add git_branches.md
git commit -m "Move notes to git_branches directory."
```

:wink: Checkout `main` and note that the file `talks/git_branches/git_branches.md` is not
listed. Then checkout `git_branches` again.

## 3.0 Remote branches

### 3.1 Push branch to remote repo

Command: `git push < remote alias > < branch name >`

```commandline
git status
git push arwhyte git_branches
git branches -a
```

## 4.0 Merging/Rebasing

### 4.1 Setup

Checkout `main` and create the following file: `talks/topics.md`.

```commandline
cd talks
touch topics.md
```

:memo: Add 3-5 future topics to file. Then stage and commit the file and push it to
your upstream remote repo.

```commandline
git add topics.md
git commit -m "Add future topics list"
git push < remote alias > main (e.g. git push arwhyte main)
```

Checkout `git_branches`. The file `topics.md` is not associated with the branch and is not included
in the checkout. Let's incorporate the new commit in `main` into `git_branches`.

:bulb: You can either _merge_ `main` into `git_branches` OR _rebase_ the commits in
`git_branches` by reapplying them over the `main` commits.

### 4.2 Merging

You can _merge_ the `main` branch into `git_branches` using the `git merge < source branch >` command.
Each merge that you perform adds a merge commit to your branch history.

:exclamation: Frequent merging from an active branch (e.g., `main`) into a "feature"
branch (e.g., `git_branches`) can result in a branch history full of merge commits that may prove
hard to follow.

From the "target" branch, in this case, `git_branches` issue the following command:

```commandline
git merge main
```

### 4.3 Rebasing

An alternative approach to combining the changes from one branch with another is to _rebase_
or reapply the changes in the target branch (e.g., `git_branches`) on top off the changes
in the source branch (e.g., `main`). In other words, all `git_branches` commits will be
placed ahead of all `main` commits in the commit history. Unlike merging, rebasing will
rewrite the branch history by creating new commits for each commit moved ahead of the
`main` commits.

```commandline
git rebase main
```

:bulb: you can also perform rebasing interactively (i.e., one commit at a time) using the `-i` flag. For a short
tutorial see Quintessa Anderson, ["Tutorial on Interactive Rebasing"](https://medium.com/swlh/tutorial-on-interactive-rebasing-e3f49505b2ce) (Medium, May 2019).

:exclamation: Never rebase a public branch (e.g., `main` in our case). Rewriting the
commit history is a local operation intended for local branches that are not intended
to be shared with others. If you rebase `main` you will rewrite the commit history
of the branch which will require additional merge commits to resync it with the
now diverged commit histories of other developers working off the branch.

### 5.0 Deletion

### 5.1 Deleting local branches

Command: `git branch -d < name >`

:Exclamation: Git will decline to delete the branch if it finds uncommitted changes in the branch.
You can override this behavior by using the `-D` flag.

Command: `git branch -D < name >`

```commandline
git branch -d git_branches
```

### 5.2 Deleting remote branches

Unlike deleting a local branch you must perform a `git push` to delete a remote branch.

Commands

* `git push < remote alias > --delete < branch >`
* `git push < remote alias > :< branch >` (preferred by me)

```commandline
git push arwhyte :git_branches

or

git push arwhyte --delete git_branches

```
