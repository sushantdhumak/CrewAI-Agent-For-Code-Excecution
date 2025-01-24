#!/usr/bin/env python
import sys
import warnings
from pathlib import Path
from crew import AgentForCodeExcecution

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """

    directory = Path(__file__).parent
    file_path = str(directory) + "/County_Health_Rankings.csv"

    inputs = {
        'file_path': file_path
    }

    results = AgentForCodeExcecution().crew().kickoff(inputs=inputs)

    print(results)


if __name__ == "__main__":
    run()
