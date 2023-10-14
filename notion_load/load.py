import argparse

from dotenv import load_dotenv

from notion_load.utils.load_util import ntfy_notification
from notion_load.utils.qdrant_util import load_qdrant


def cli():
    # https://realpython.com/command-line-interfaces-python-argparse/#handling-how-your-cli-apps-execution-terminates
    parser = argparse.ArgumentParser(prog="load.py", description="Load data into vector database")
    parser.add_argument("source",
                        choices=['notion'],
                        help="source can only be 'notion'")
    parser.add_argument("target",
                        choices=['qdrant'],
                        help="target can only be 'qdrant'")
    parser.add_argument("-v", "--verbose",
                        help="verbose logging",
                        action="store_true")
    parser.add_argument("-r", "--reset",
                        help="this will reset collection before loading",
                        action="store_true")

    args = parser.parse_args()

    # print(args)

    if args.verbose:
        print("  - verbose on")
    else:
        print("  - verbose off")

    print(f"  - fetching documents from: {args.source}")
    print(f"  - loading processed documents into: {args.target}")
    print(f"  - reset collection before loading: {args.reset}")
    print()
    return args


if __name__ == '__main__':
    load_dotenv()

    args = cli()

    try:
        if args.target == 'qdrant':
            load_qdrant(args)
        elif args.target == 'local':
            print("Loading locally not implemented yet")
            exit(1)
        else:
            print(args)
            print(f"Invalid target: {args.target}")

        ntfy_notification("Load successful for load.py")
    except Exception as e:
        ntfy_notification("Load successful for load.py", title='Error', tags='error')
        print("LOAD FAILED")
        print(e)
        exit(1)
