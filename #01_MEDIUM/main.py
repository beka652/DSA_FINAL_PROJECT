from Engine.editor_engine import TextEditor


def main():
    editor = TextEditor()
    print("Text Editor Engine (Type 'EXIT' to quit)")

    while True:
        cmd_input = input("> ").strip().split()
        if not cmd_input:
            continue

        cmd = cmd_input[0].upper()

        if cmd == "WRITE" and len(cmd_input) > 1:
            char = cmd_input[1].replace("'", "")
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
