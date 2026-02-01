# DSA Final Project

A collection of **Data Structures & Algorithms** projects of varying difficulty. Each subproject demonstrates core data structures (stacks, linked lists, queues, heaps) in practical applications.

## Overview

This repository contains three standalone projects:

| Directory | Project | Brief description |
|-----------|---------|-------------------|
| **`#33_EASY/`** | Bracket Syntax Validator | CLI tool that validates balanced brackets `()`, `[]`, `{}` using a **stack**. |
| **`#01_MEDIUM/`** | Advanced Text Editor Engine | Text-editor core with a **doubly-linked list**, cursor-based editing, and undo/redo batching. |
| **`#02_HARD/`** | Hierarchical Task Processor | Multi-level **feedback queue** scheduler (Queues A/B/C) with custom **LinkedQueue** and **PriorityQueue**. |

## Learn More About Each Project

Each subproject has its own documentation and structure. **Navigate to the directory and read its README** for:

- Detailed overview and goals  
- Requirements and setup  
- How to run and use it  
- Implementation notes and examples  

| Go to | README |
|-------|--------|
| **[#33_EASY/](#33_EASY/)** | [#33_EASY/README.md](#33_EASY/README.md) — Bracket validator usage, behavior, and Stack usage. |
| **[#01_MEDIUM/](#01_MEDIUM/)** | [#01_MEDIUM/README.MD](#01_MEDIUM/README.MD) — Text editor engine, folder structure, and operations. |
| **[#02_HARD/](#02_HARD/)** | [#02_HARD/README.md](#02_HARD/README.md) — Task processor, scheduling algorithm, and commands. |

## Requirements

- **Python** 3.x (see [pyproject.toml](pyproject.toml) for the exact version).
- No external dependencies; each project uses custom or local implementations.

## Quick Start

From the project root you can run each project’s entry point:

```bash
# #33_EASY — Bracket validator
python "#33_EASY/validator.py" validate "<your_bracket_string>"

# #01_MEDIUM — Text editor demo
python "#01_MEDIUM/main.py"

# #02_HARD — Hierarchical task processor (interactive CLI)
python "#02_HARD/main.py"
```

For full usage, examples, and behavior, see the README in the corresponding directory.
