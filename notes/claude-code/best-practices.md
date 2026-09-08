# Best Practices

The most critical resource when working with agents is context window. It holds entire conversation, every message, every file claude reads, every command output. It fills up quite fast. And performance starts degrading after that, with symptoms like forgetting earlier work or making mistakes. 

- Use `/clear` to clear context when starting unrelated/new work. 
- Use subagents
- Add statusline via `/statusline` to always show model name and context
- Use `/insights` to generate a html detailing things that work, that needs improvement in your CC usage
### Use Right Model

- Sonnet - good with coding
- Opus - use for complex architectural decisions, and planning

Hooks - run specific command at steps in claude code. 