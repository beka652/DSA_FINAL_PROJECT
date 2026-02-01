from Engine.editor_engine import TextEditor


def main():
    editor = TextEditor()
    print("Text Editor Engine (Type 'EXIT' to quit)")
    print("Commands: WRITE 'char', DELETE, MOVE left/right, UNDO, REDO, DISPLAY")

    while True:
        cmd_input = input("> ").strip().split(maxsplit=1)
        if not cmd_input:
            continue

        cmd = cmd_input[0].upper()

        if cmd == "WRITE" and len(cmd_input) > 1:
            text_to_write = cmd_input[1].strip("'")
            for char in text_to_write:
                editor.write(char)
        elif cmd == "DELETE":
            editor.delete()
        elif cmd == "MOVE" and len(cmd_input) > 1:
            editor.move_cursor(cmd_input[1].lower())
        elif cmd == "UNDO":
            editor.undo()
        elif cmd == "REDO":
            editor.redo()
        elif cmd == "DISPLAY":
            editor.display()
        elif cmd == "EXIT":
            break
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
