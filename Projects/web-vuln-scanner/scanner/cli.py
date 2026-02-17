import argparse
from .core import Scanner

def main():
    parser = argparse.ArgumentParser(description="Web Vulnerability Scanner")
    parser.add_argument("targets", nargs="+")
    args = parser.parse_args()

    scanner = Scanner(args.targets)
    reports = scanner.run()

    print(reports)