
## The Advanced Text Editor Engine

This folder contains a compact text-editor core implemented with a doubly-linked list and basic undo/redo batching.


**Folder structure**

```
Medium/
├── main.py                      
├── Engine/
|   ├── __init__.py
│   ├── editor_engine.py         
│   └── model.py       
└── README.md
```

- `main.py` — small runner / entry point to exercise the editor.
- `Engine/` — editor implementation and supporting models:
	- `editor_engine.py` — `TextEditor` class, internal helpers and undo/redo stacks.
	- `model.py` — `Node`, `Action`, and other data models used by the engine.


**How the engine works (concise)**

- **Storage**: each character is a `Node` in a doubly-linked list. Two sentinel nodes (`head` and `tail`) mark the list boundaries.
- **Cursor**: `cursor` references a node (initially `tail`) and represents the insertion point; inserting places new nodes immediately before the `cursor` node.
- Internal helpers:
	- `_insert_node(char, position_node)` — method that instantiates a `Node(char)`, links it into the list before `position_node`, and returns the new node.
	- `_remove_node(node)` — unlinks `node` from the list and returns its stored value.
	- `_handle_batching(action_type, char)` — groups nearby insert/delete characters into an `Action` (with a timestamp) and pushes it onto `undo_stack` for efficient undo operations.
- **Undo/redo**: actions are represented by `Action` objects and saved on `undo_stack`/`redo_stack`. Public `undo`/`redo` operations should pop / apply these actions and update the list accordingly.


**Data structures used**

- **Doubly Linked List**: To store the text characters (allows O(1) insertions/deletions at cursor).
- **Two Stacks**: `UndoStack` and `RedoStack` to manage history states.
- **Custom "Action" Object**: To store details needed for reversal (e.g., "Deleted 'x' at index 5").


**Operations**

-`WRITE <char>`: Insert character at current cursor position.

-`DELETE`: Delete character previous to cursor (Backspace).

-`MOVE <left|right>`: Move cursor position.

-`UNDO`: Revert last action (or batch).

-`REDO`: Redo last reverted action.

-`DISPLAY`: Show current text state and cursor position (e.g., Hello|World)



### Example 

```
> WRITE 'A'
> WRITE 'B'
> WRITE 'C'
Display: ABC|

> UNDO
Display: |
(Note: If batched, all ABC removed. If not, only C removed. Assume batched for this example)

> REDO
Display: ABC|

> MOVE left
Display: AB|C

> DELETE
Display: A|C

> UNDO
Display: AB|C
```


**Run**

From the project root run:

```
python MEDIUM/main.py
```

