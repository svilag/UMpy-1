# UMpy

## 1.0 Study group repo

The umpy repo houses assets related to study group meetings and conversations.

## 2.0 Git LFS

Github enforces limits on individual file size (currently 100 MB) that can be stored in repos. Git
LFS permits large file storage; the extension replaces large files with text pointers in Git while
storing the file contents on a remote server (in our case managed by Github).

The umpy repo utilizes [Git Large File Storage](https://git-lfs.github.com/) (Git LFS) for managing
the storage requirements of certain assets (e.g., `*.csv`). After you fork and clone the UMpy repo
to your working directory you must download and install the Git LFS extension.

You can download the Git LFS binary from [Git Large File Storage](https://git-lfs.github.com/) site.
You can also install the extension using [Homebrew](https://brew.sh) or
[Chocolatey](https://chocolatey.org/).

### [Homebrew](https://formulae.brew.sh/formula/git-lfs) (macOS)

```commandline
brew install git-lfs
```

### [Chocolatey](https://community.chocolatey.org/packages/git-lfs.install) (Windows)

```commandline
choco install git-lfs.install
```

## 2.1 Git LFS Setup

Once you've installed Git LFS, open a terminal and issue the following command for your user
account:

```commandline
git lfs install
```

Your forked/cloned instance of the umsi-arwhyte/umpy repo is already set up for Git LFS with
specific file types under LFS listed in the `.gitattributes` file.

There is no change to the standard `git add` - `git commit` - `git push` workflow.

## 2.2 Checking files under Git LFS management

You can return a list of files under Git LFS by issuing the following command:

```commandline
git lfs ls-files
```

## 2.3 Retrieving files

You can retrieve files under Git LFS management, either singly or in bulk by issuing the following
commands:

### All files

```commandline
git lfs pull
```

### Single file

```commandline
git lfs pull --include=< filename >
```

## 2.4 Additional reading

See the following tutorial in order to enhance your knowledge of Git LFS.

Alija Sabic, ["git-lfs tutorial"](https://sabicalija.github.io/git-lfs-intro/).
