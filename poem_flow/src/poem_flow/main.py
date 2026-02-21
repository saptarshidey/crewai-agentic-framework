#!/usr/bin/env python

from random import randint
from pydantic import BaseModel
from crewai.flow import Flow, listen, start
from crews.poem_crew.poem_crew import PoemCrew

class PoemState(BaseModel):
    sentence_count: int = 1
    poem: str = ""

class PoemFlow(Flow[PoemState]):

    @start()
    def generate_sentence_count(self, crewai_trigger_payload: dict = None):
        print("Generating sentence count")

        if crewai_trigger_payload:
            self.state.sentence_count = crewai_trigger_payload.get('sentence_count', randint(4, 10))
            print(f"Using trigger payload: {crewai_trigger_payload}")
        else:
            self.state.sentence_count = randint(4, 10)

    @listen(generate_sentence_count)
    def generate_poem(self):
        print("Generating poem")

        inputs = {
            'topic': 'Summer Holidays',
            'sentence_count': self.state.sentence_count
        }

        try:
            result = PoemCrew().crew().kickoff(inputs=inputs)
            print("Poem generated")
            self.state.poem = result.raw
        except Exception as e:
            raise Exception(f"An error occurred while running the crew: {e}")

    @listen(generate_poem)
    def save_poem(self):
        print("Saving poem")
        with open("poem.txt", "w") as f:
            f.write(self.state.poem)

def kickoff():
    poem_flow = PoemFlow()
    poem_flow.kickoff()

def plot():
    poem_flow = PoemFlow()
    poem_flow.plot()

if __name__ == "__main__":
    kickoff()
