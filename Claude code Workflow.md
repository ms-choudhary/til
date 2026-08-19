---
title: AI Workflow
date: 2026-05-23
tags:
  - ai
share: true
---

### Potential use cases

- Implement features
- Refactor this subsystem
- Research this library
- Set up this service 
- Write tests, run them, fix failures
- Compare approaches , and propose a plan
- troubleshoot issues and fix them

### Skills

- [Caveman](https://github.com/juliusbrussee/caveman)
- [spec-kit](https://github.github.com/spec-kit/)
- For larger features, enable  CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
	- 1 reviewer
	- 1 QE agent writes tests
- [diffity](https://github.com/nilbuild/diffity)

### Research

> read this folder in depth, understand how it works deeply, what it does and all its specificities. when that’s done, write a detailed report of your learnings and findings in research.md


I want to build a static website (on github pages) for my learnings, suggest a way to do so. I use obsidian to take notes. Take inspiration from similar examples: https://github.com/simonw/til, https://github.com/jbranchaud/til
### Plan

> I want to build a new feature [name and description] that extends the system to perform [business outcome]. write a detailed plan.md document outlining how to implement this. include code snippets

I want to change how envelopes are selected in ui. 
By default, it should show all envelopes for the current month (same as today). Instead of combobox, make it a drop down select, when an envelope is selected, start date is auto set to the start of transaction for that envelope. end date is always today. Date can be changed later though. For eg usecase, select default, shows all transactions in default envelope from start till today, then user can change the date to select last month to drill down into specific dates. Ensure that ui is mobile friendly (iphone). write a detailed plan.md document outlining how to implement this. include code snippets. 
### Annotate

>I added a few notes to the document, address all the notes and update the document accordingly. don’t implement yet


### Add a todo list (for longer tasks)

> add a detailed todo list to the plan, with all the phases and individual tasks necessary to complete the plan - don’t implement yet

### Implement

#### With todo

> implement it all. when you’re done with a task or phase, mark it as completed in the plan document. do not stop until all tasks and phases are completed. do not add unnecessary comments or jsdocs, do not use any or unknown types. continuously run typecheck to make sure you’re not introducing new issues.

#### Without todo

> implement it all. do not stop until all tasks and phases are completed. do not add unnecessary comments or jsdocs, do not use any or unknown types. continuously run typecheck to make sure you’re not introducing new issues.


## Sources
- 
## Related
- [](%5D)