#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import SimpleAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    inputs = {
        'topic': 'Global Warming',
        'current_year': str(datetime.now().year)
    }

    try:
        SimpleAgent().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


run()
