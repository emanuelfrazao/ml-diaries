**March 13, 2023**

# plan of the day

* starting on docker fundamentals - following Docker in Action, which seems very nice: well-structured, tackling the fundamentals, a good reference for them, bla bla - with a thoughful pedagogical approach (or so it seems!)

# docker in action

* before delving into the book (- tomorrow?), some questions to try and answer properly:
  * what's the problem Docker was built to solve?
  * what are the fundamental constituents of the solution?
  * what are the main design choices behind Docker's solution?
  * how does it differ from previous/alternative solutions?
* in trying to answer:
  * one wants to run software on its machine - and there has been an historical tendency (with good reasons, one imagines!; and with notable exceptions) to write machine-specific software: initially, it was highly specific on the hardware, as it needed to - with little interface design, program hierarchies, and universal protocols -; then the community uniformized _that_ to a big extent - whilst making it, on sufficient instances to be noticeable, to still be specific on the OS.
  * then came virtual machines - which I guess are pretty much an OS - simulated/virtualized on top of some other OS (which may very well be of the same type).
    * these had the advantages of:
      * letting one run OS-specific software, regardless of its installation/brand,
      * uniformizing software builds for teams of PC-users (developers, tool-users, wtv), iot avoid hassles
      * and more, one imagines
    * they also have a major draw-back for many situations:
      * virtual machines make heavy use of computer resources - if complying with their goal - for they emulate a full OS on top of an already running OS
      * so, when one wants to run a specific program, without the need of a full-fledged OS - one would rather have a _lighter_ tool
* enter containers:
  * some way to _containarize_ a program [, a piece of software]: give it everything it needs to run (and _ship_ to someone else), and nothing else
  * we can try and imagine what would be the requirements for such a system - i.e., the container for the program, and the environment it runs on:
    * having a way to specify the exact dependency-programs of the program
      * one guesses 'as other containers - turtles all the way down? - or with some way to specify _pure containers_, i.e. without dependencies
    * having thus a hub of containers, from which one select the ones required to build its own
    * having a way to specify the internal/external interface of the program (- in other words: having some protocol-oriented syntax) for:
      * accessing machine resources and the like
        * accessing peripherals
        * communicating with other machines through network routing
      * accessing other running programs: be it _normal_ programs in the OS, or other containers running
    * having some class-object relation to the containers: i.e. some way to have a container template from which one can run container instances
    * and we guess more - that we'll find out!
* how does docker solve this? - that's what we'll learn ehe
* and then some comparisons and alternatives! - if they're really alternatives (!)
