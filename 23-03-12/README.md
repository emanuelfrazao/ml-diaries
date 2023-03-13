march 12th, 2023

* divising a better (i.e. parsable) template for this
* trying out Fig for the command line
* running through the _Pro Git_ iot figure out some principles behind the tool
* running through _Docker in Action_ to finally get that b****'s internals!
* pin down projects' specs (perhaps not today - but it's good to dream):
  * exploring random number generators
  * exploring git log statistics
* note to self that I should start building stuff in rust - to give it a try! - say:
  * some basic cli's and api's
  * our random number generators' experiment
  * some data analysis/"science" projects: a chance to play with polars (it also has some torch bindings)
  *

# parsable template for ml-diaries

looking at the previous days - there's really no point in writing stuff directly in a jupyter notebook - no matter the ease-of-use: things are then hard to parse - and hence lost in the midst; (version control is not great;) most things I'd write are already implicitly separated between code experiments and high-level descriptions.

so — new template specs:

* every day is a folder - named clearly after the day
* every day contains a README.md
  * every topic is listed and then covered in README.md
* if a topic is explored with code,
  * then the corresponding code is to be placed in a [corresp.] named folder
  * the folder may contain a Makefile for easilys running the experiments - but I guess no need - couldn't we find an easier way? templating cli's and setuptools, or something

and we guess that's it...

e.g.: `./example_template`

# fig usage

fig seems very nice - the autocompletion is great, modern-IDE-style - it gives the docstrings and all.

it integrates with argparse and click for python - or so they say - example in `./fig-custom-cli`

* looks weird - not enough documentation, nor time to search it - couldn't make it work
* also, we guess not so useful, unless one is to ship for other people.

it allows one to easily create scripts... hum

temporarily porting all aliases and simple scripts there - it has a nice interface (with some very limited debugging and editing capabilities - but still, guess I'm enjoying seeing them in a GUI)

it lacks some transparency for me atm, but hey!

# pro git book

## some general takes

regarding the book, it seems very well structured, and it is free - I don't remember it being so nice for me some years ago - so I guess it lacks some better motivation/contextualization (wrt git mentions on the public arena! - namely, disambiguating the references to github), but that's not on them - in other words: I lacked the maturity to appreciate the problem it was trying to solve. I guess for arbitrary-background-newcomers, one may stress the motivation behind tracking versions (as say, by referencing Word), and then move to stressing collaboration - in a how-would-one fashion.

the last chapter on git internals must be fun - meanwhile 'took a look, and it is indeed fun: he goes into what he calls _plumbing_, the low-level API - the rest of the book being about _porcelain_, the high-level API.

they do not go much in-depth into the _plumbing_, but they do give some picture of the (what I'd take to be the) main-sufficient functionalities for building the high-level functionality one uses normally. in the meanwhile, one gets some intuition on how git stores and manages the information - which would be useful to debug it, one guesses. plus, they describe give a syntethic view of the main objects git manages: blobs, trees, commits, and tags.

other than that, the book takes an organized (as expected) approach: some basics, some specifics on branching, some specifics on communication protocols for git - custom aswell as known providers -, some best practices for cooperating with multiple agents on small to big projects, some advanced git tooling, some sugar, and some internals (which we long for!) - from a high-level view, it seems pretty well covered.

it seems like it will be a good book for reference.

they wouldn't say yet, but apparently git is written in a host of languages: subcommands' interfaces use stuff like bash, perl, python, and tcl; the core is written in C and bash.

so - git is special with regards to perforce (and the like), in that: it makes use of distributed repos, not centralized; it uses (optimized) snapshot version control, not delta.

what would be the consequences of these options? - we'll see if we get to understand (!)

## git basics

some structuring of git

### basic high-view

* every file in the folder is in one of two self-descriptive states:
  * `untracked` - the default
  * `tracked` - after explicitly setting a file to be tracked... (or when cloning a repository with already tracked files) -:
    * `unmodified` - when the last snapshot of the file corresponds to the file contents,
    * `modified` - when any changes occur on a tracked and previously `unmodified` or `staged` file;
    * `staged` - when set to be so, in order to take a snapshot of the file version;
* a repo may be regarded as the set of tracked files in the folder
* the repo is organized (implicitly or explicitly) in branches:
  * the basic idea spurs out of a _separation of concerns_: such that

    * one can make changes to the same files' version(s) in multiple directions - e.g., a team developing multiple features in parallel -,
    * in such a way that the alterations can be merged later, whilst safeguarding the conflicts
  * when a repo is created, git automatically creates a branch (- conventionally called `main` or `master` -) and sets it as default
  * one can then create any number of branches afterwards (e.g., one per feature, one per problem to be fixed, one per developer) (TODO: fill-in)
  * (so, one can imagine that each branch may be regarded as a repo - or can't one?)
* furthermore, git provides a communication protocol between repositories following a local-remote logic:
  * `local` refers to one [developer]'s local repository (to make it very circular)
  * `remote` refers to an intermediate (say, more than a "central" one) repository (even if in one's machine - but usually on some internet-accessible server) through which many ones [developers] may cooperate (i.e., read-write)
  * the 2 agents behave with different and complementary interfaces
  * their mode of interaction is many-to-many:
    * a `local` repo may have multiple `remote` ones, and a `remote` - by serving as an intermediary repo - obsiously serves multiple `local` ones
* there are some important notes with regards to how git **stores data**:
  * git stores data as a  series of snapshots - that may actually be equated to a hyper-tree-like structure of dependencies
  * a commit node contains pointers to:
    * commit info:
      * the snapshot of the staged content (to be committed)
      * it's author's name and email
      * the message
      * the SHA code
    * commit parents, such that:
      * the initial commit has no parent (is the root)
      * a _normal_ commit (within repo/branch) has a single parent (the previous commit node)
      * a _branch/repo merging_ commit has multiple parents (the previous commit nodes that it's merging)
  * each committed snapshot is also stored as a tree following the directory structure (files are stored in so-called _blobs_)
* banking on that, when branching - under the hood - git _simply_ creates a (lightweight) pointer to a commit node

### basic high-level interface (aka porcelain)

*a note on vs-code's git interface being so clean and nice*

* handling **repo-specific actions**:
  * `init`:
    * initialize git tracking on a folder - turning it into a _repo_
    * note this does not track by itself any files in the folder - it just initializes git meta info configs and the sort (by creating a `.git` sub-directory on the given folder)
  * `clone`:
    * make an almost-identical copy of a repository into another folder (including past history of tracked changes)
    * note that I have no idea what this _almost_-identical refers to
* visualizing **current and historical states**:
  * current:
    * `status`:
      * get the current state:
        * which branch it is on
        * miss-match between *local* branch a _remote_ branch
        * list of `untracked`, `modified`, and `staged` files
      * with `-s | --short`, one gets a short status... - i.e., only the list of files
      * note that it ignores files listed in `.gitignore` (which uses standard glob syntax)
  * past:
    * `log`:
      * get commit history [in reverse chron. order]:

        * for each commit, by default, one gets the SHA code, the author, the date, and the commit message
      * one can filter the output with:

        * `-<n>`, for limiting the number of commits shown (by `n`)
        * `--since=<date>` and `--until=<date>`
        * `--author=<name>` for filtering on the author
        * `--grep=<pattern>` for filtering on the pattern
      * with `--patch | -p`, one can also see the differences for each file commited
      * with `--stat`, one can get some statistics on the number of changes per file commited
      * with `--pretty`, one can format the log strings for each commit:

        * `--pretty=oneline` for a single line with (SHA, msg)
        * `--pretty=format:<format>` for formatting the log at will - e.g.: `--pretty=format:"%h - %an, %ar : %s"` - with specifiers:

          * `%H` : commit hash
          * `%h` : abbrv. commit hash
          * `%s` : subject / message
          * ...
          * `%an`: author name
          * `%ae`: author email
          * `%ad`: author date
          * `%ar`: author relative date
          * `%cn`: commiter name
          * `%ce`: commiter email
          * `%cd`: commiter date
          * `%cr`: commiter relative date
      * with `-S <string>` one can search for commits where string is contained in the newly added file's name, or any new lines
      * with `-- <path>` (notice the black space), one can ask for the history on a specific folder location
  * comparison (current vs past, local vs remote, branch vs branch):
    * `diff`:
      * get the differences between file versions
      * note that it's really better to use one's IDE directly for this.
* handling **file-specific actions**:
  * staging alterations, additions, and removals:
    * `add`:
      * set file(s) as `staged` (be them originally `untracked`, or `modified`)
      * note that a file may be at the same time `staged` and `modified` (- if some version was `staged` and later `modified`...)
    * `rm`:
      * remove the file as with shell's `rm`, with the extra feature of already placing the file deletion as a staged action
      * with `--cached <file>`, it does not remove the actual file - just removes it from staging area
    * `mv`:
      * rename a file
      * note that git does not keep track of actual file movements (whatever this means)
  * saving staged actions:
    * `commit`:
      * save staged actions...
      * specify `-m <msg>` or let some tool prompt you with a way to specify a message - _one should_ always do it - thou shalt!
      * with `--amend <file>`, one can add another file change/add to the previous commit
  * undoing stuff:
    * `rebase`:
    * `reset`:
  * tagging _nodes_:
    * `tag`:
      * manage tags: create, list, delete, and verify tags - for software versions, mostly (for one day)
* handling **local-remote communication**:
  * `remote`:
    * manage `remote` repos from `local` - it is a command with many sub-commands/actions:
      * by itself (and with `-v` for verbose), it lists the `remote` repos associated, with their name (and ref)
      * `show`:
        * get some general info on sync state between `local` and `remote`
      * `add`, `rm`, `rename`:
        * add, remove, or rename `remote` repo
      * `get-url`, `set-url`:
        * get-set url to `remote` repo
      * etc (some func. on remote head branch, and tracking remote branches)
  * `push`:
    * update `remote` repo with `local` contents
    * with `-d`, delete a remote branch/ref
  * `pull`:
    * update `local` repo with `remote`/other contents
* handling **branches**:
  * `branch`:
    * manage local branches: list , create, remove (`--delete | -d`)
      * `git branch <name> [commit ref]` to create a branch from last commit, or some referenced one
      * `git branch <name> <remote>:<branch>` to create a local branch from a remote one
    * with `--remotes | -r`, list remote branches
  * `checkout`:
    * change current branch
    * with `-b`, create a new branch and switch [current branch] to it
* handling **configuration settings**:
