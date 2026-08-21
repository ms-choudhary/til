# Agentic Engineering

Our engineering habits were built around the fact that writing code is hard. Writing code is cheap now. If AI writes the code, what's left to do? There's so much stuff: 
- figuring out what code to write
- every problem has many solutions, and each of them comes with it's own tradeoff

Good code still has a cost. Big part of the skill in building software is understanding what's possible & what isn't. Invest time in learning. Many of them small proof of concepts that demonstrate a key idea. Then combine few of them to build something new. 

### Tips on using agents
Give the agents right tools to solve the problem

Specify the problem in right level of detail

Give them examples of things you want them to do

Verify & iterate on the results, until you're confident that it solves the problem reliably

Agents can learn from past mistakes, provided we deliberately update instructions and tools harness to account for what we learn. 

If agents drop the quality of output, figure out what aspects of the process is hurting the quality and fix them. 

**Technical debt**: Doing things the right way will take too long, so work with the time constraints and hope that the project will survive long enough to pay the debt later. 

With AI agents, always avoid the technical debt, go to extra length. It's cheap now. 
- api refactor 
- poor inconsistent naming
- duplicate functionality
- 1000s of lines in function
Fire the prompt away, and decide later. Agents are good for these tasks. 

The best way to make confident tech choices, to prove it's fit for the purpose, is to make a working prototype. Wire up the simulation, run load test & see what breaks. 

The biggest anti-pattern: not reviewing the code. 

## Sources
- 
## Related
- [claude-code-workflow](/claude-code/claude-code-workflow.md)