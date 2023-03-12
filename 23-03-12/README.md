march 12th, 2023

* divising a better (i.e. parsable) template for this
* trying out Fig for the command line
* running through the _Git Book_
* running through _Docker in Action_
* pin down projects' specs:
  * exploring random number generators
  * exploring git log statistics

# parsable template for ml-diaries

looking at the previous days - there's really no point in writing stuff directly in a jupyter notebook - no matter the ease-of-use: things are then hard to parse - and hence lost in the midst; (version control is not great;) most things I'd write are already implicitly separated between code experiments and high-level descriptions.

so — new template specs:

* every day is a folder - named clearly after the name
* every day contains a README.md
  * every topic is listed and then covered in README.md
* if a topic is explored with code,
  * then the corresponding code is to be placed in a [corresp.] named folder
  * the folder may contain a Makefile for easily running the experiments
  *

and we guess that's it...

e.g.: `./example_template`

# fig usage

fig seems very nice - the autocompletion is great, modern-IDE-style - it gives the docstrings and all.

it integrates with argparse and click for python - or so they say - example in `./fig-custom-cli`

* looks weird - not enough documentation, nor time to search it - couldn't make it work
* also, we guess not so useful, unless one is to ship for other people.

it allows one to easily create scripts... hum

temporarily porting all aliases and simple scripts there - it has a nice interface (with some very limited debugging and editing capabilities - but still, it gives a lot of functionality out of the box: easy cli's )

it lacks some transparency for me atm, but hey!

# git book

## some general takes

regarding the book, it seems very well structured, and freely online - I don't remember it being so nice for me some years ago - so I guess it lacked some better motivation/contextualization (wrt git mentions on the public arena! - namely, disambiguating the references to github), but that's not on them. I guess for arbitrary-background-newcomers, one stress the motivation behind tracking versions (as say, by referencing Word), and then move to collaboration.

the last chapter on git internals must be fun. other than that, the book takes an organized (as expected) approach: some basics, some specifics on branching, some specifics on communication protocols for git - and custom aswell as known providers -, some advanced git tooling, some sugar, and some internals (which we long for!) - from a high-level view, it seems pretty well covered.

it seems like it will be a good book for reference.

they wouldn't say yet, but apparently git is written in a host of languages: subcommands' interfaces use stuff like bash, perl, python, and tcl; the core is written in C and bash.

so - git is special with regards to perforce (and the like), in that: it makes use of distributed repos, not centralized; it uses (optimized) snapshot version control, not delta.

what would be the consequences of these options? - we'll see!

## git basics

git, being a file-tracker, when associated with a repo/folder [does] —

### high-view

* every file in the folder is in one of two self-descriptive states:
  * `untracked` - the default
  * `tracked` - after explicitly setting a file to be tracked... (or when cloning a repository with already tracked files) -:
    * `unmodified` - when the last snapshot of the file corresponds to the file contents,
    * `modified` - when any changes occur on a tracked and previously `unmodified` or `staged` file;
    * `staged` - when set to be so, in order to take a snapshot of the file version;
* a repo may be regarded as the set of tracked files in the folder
* the repo is organized (implicitly or explicitly) in branches:
  * the basic idea spurs out of a _separation of concerns_: such that

    * one can make changes to the same files in multiple directions - e.g., a team developing multiple features in parallel -,
    * in such a was that they can be merged later whilst safeguarding the conflicts
  * when created, a repo implicitly creates a main branch - conventionally called `main` or `master`
  * on request, it can create multiple other branches (TODO: fill-in)

### basic interface

* handling **repo-specific actions**:
  * `init`:
    * initialize git tracking on a folder - turning it into a _repo_
    * note this does not track by itself any files in the folder - it just initializes git meta info configs and the sort (by creating a `.git` sub-directory on the given folder)
  * `clone`:
    * make an almost-identical copy of a repository into another folder (including past history of tracked changes)
    * note that I have no idea what this _almost_-identical refers to
* visualizing **current and historical states**:
  * `status`:
    * get the current state:
      * which branch it is on
      * miss-match between *local* branch a _remote_ branch
      * list of `untracked`, `modified`, and `staged` files
    * with `-s | --short`, one gets a short status... - i.e., only the list of files
    * note that it ignores files listed in `.gitignore` (which uses standard glob syntax)
  * `log`
  * `history`
  * `diff`:
* handling **file-specific actions**:
  * `add`:
    * set file(s) as `staged` (be them originally `untracked`, or `modified`)
    * note that a file may be at the same time `staged` and `modified` (- if some version was `staged` and later `modified`...)
  *
