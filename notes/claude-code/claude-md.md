# CLAUDE.md, Auto memory

CLAUDE.md (or AGENTS.md for open standard) are instructions you write to give persistent context for agents. 

Auto memory are the notes claude writes itself based on corrections and preferences of the user. You can enable or disable auto memory and other settings at `/memory`

Both are loaded automatically in every session. Check `/context all` to show what claude has loaded. 
### Things to add

- Coding standards to follow
- Workflows for eg: how to invoke tests etc
- Project architecture 
- Project specific gotchas
### When to add to CLAUDE.md

- Claude makes repeated mistakes
- Learnings from a session you want to persist
- Context info required to get up to speed for a new member  

Since it's loaded on every run, it good idea to:
- keep it to facts
- should hold in every session, if not, you can create a skill
- have specific concrete instructions instead of being vague. for eg,
	- "Use 2 space indentation" instead of "Format code properly"
- review the changes periodically and ensure that no conflicting instructions are present. 