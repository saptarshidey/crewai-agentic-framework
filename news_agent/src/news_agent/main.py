#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import NewsAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    inputs = {
        'topic': 'BITS Pilani',
        'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    }

    try:
        NewsAgent().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


run()
