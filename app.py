import sys
from pipeline import run_pipeline


def main():
    env = sys.argv[1] if len(sys.argv) > 1 else "dev"
    run_pipeline(env)


if __name__ == "__main__":
    main()