import argparse
from matrixserver.config import Config
from matrixserver.program import Program


def main(args):
  config = Config.parse(args.config)
  program = Program(config)
  program.start()


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-c", "--config", required=True)
  args = parser.parse_args()
  main(args)