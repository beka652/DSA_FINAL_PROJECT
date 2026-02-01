from Stack.Stack import Stack
import argparse


def validate(syntax):

    stack = Stack()
    o_c_dict = {"(": ")", "{":"}", "[": "]"}

    supported_pairs = "{[()]}"

    for i, char in enumerate(syntax):

        char = syntax[i]
        
        if char not in supported_pairs:
            continue
        
        # for opening symbol
        if char in "([{":
            stack.push((char,i))
        else: # closing symbol
            opening = stack.pop()
            if opening is None:
                print(f"Unclosed {char} at index {i}")
                return 
    
            expected_closing = o_c_dict[opening[0]]
            if expected_closing != char:
                print(f"Error: Expected {expected_closing}, found {char} at index {i} ")
                return 

    if not stack.isEmpty():
        x = stack.pop()
        print(f"Error: unclosed opening -> {x[0]} at index {x[1]}")
    else:
        print("valid")

def main():
    parser = argparse.ArgumentParser(
        prog="validator",
        description="Validate bracket syntax"
    )

    subparsers = parser.add_subparsers(dest="command")

    # validate command
    validate_parser = subparsers.add_parser(
        "validate",
        help='Validate a syntax string (e.g. "[][]")'
    )
    validate_parser.add_argument(
        "syntax",
        help='String to validate'
    )

    args = parser.parse_args()

    # If no command is given, show help
    if args.command is None:
        parser.print_help()
        return

    # Only supported command
    if args.command == "validate":
        validate(args.syntax)


if __name__ == "__main__":
    main()

