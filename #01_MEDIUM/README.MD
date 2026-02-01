
**The Advanced Text Editor Engine**

This folder contains a compact text-editor core implemented with a doubly-linked list and basic undo/redo batching.

**Folder structure**

- `main.py` — small runner / entry point to exercise the editor.
- `Engine/` — editor implementation and supporting models:
	- `editor_engine.py` — `TextEditor` class, internal helpers and undo/redo stacks.
	- `model.py` — `Node`, `Action`, and other data models used by the engine.

**Overview & goals**

- Purpose: provide a minimal, testable editor core that stores characters as nodes in a linked list, supports cursor-based insertion/removal, and records user edits for undo/redo with simple batching.
- Ideal for learning data-structure-backed text editing or as a base to expand into a more complete editor.

**How the engine works (concise)**

- Storage: each character is a `Node` in a doubly-linked list. Two sentinel nodes (`head` and `tail`) mark the list boundaries.
- Cursor: `cursor` references a node (initially `tail`) and represents the insertion point; inserting places new nodes immediately before the `cursor` node.
- Internal helpers:
	- `_insert_node(char, position_node)` — method that instantiates a `Node(char)`, links it into the list before `position_node`, and returns the new node.
	- `_remove_node(node)` — unlinks `node` from the list and returns its stored value.
	- `_handle_batching(action_type, char)` — groups nearby insert/delete characters into an `Action` (with a timestamp) and pushes it onto `undo_stack` for efficient undo operations.
- Undo/redo: actions are represented by `Action` objects and saved on `undo_stack`/`redo_stack`. Public `undo`/`redo` operations should pop / apply these actions and update the list accordingly.



**Operations**

-`WRITE <char>`: Insert character at current cursor position.

-`DELETE`: Delete character previous to cursor (Backspace).

-`MOVE <left|right>`: Move cursor position.

-`UNDO`: Revert last action (or batch).

-`REDO`: Redo last reverted action.

-`DISPLAY`: Show current text state and cursor position (e.g., Hello|World)



**Example usage**

- Insert a character (internal): `editor._insert_node('x', editor.cursor)` — inserts before cursor.
- Remove a node (internal): `editor._remove_node(editor.cursor.prev)` — removes the node before the cursor.

**Notes & next steps**

- The file currently exposes internal helpers (prefixed with `_`). Add public methods such as `insert(char)`, `delete()`, `move_cursor(direction)`, `undo()`, and `redo()` to provide a stable interface.
- Add tests that exercise insertion, deletion, cursor movement, and undo/redo batching.

**Run**

From the project root run:

```
python MEDIUM/main.py
```

