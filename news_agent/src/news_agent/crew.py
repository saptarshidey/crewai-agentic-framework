from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileWriterTool
from typing import List
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class NewsAgent():

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def news_site_retriever(self) -> Agent:
        return Agent(
            config=self.agents_config['news_site_retriever'],
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def website_scraper(self) -> Agent:
        return Agent(
            config=self.agents_config['website_scraper'],
            tools=[ScrapeWebsiteTool()],
            verbose=True
        )

    @agent
    def news_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['news_writer'],
            verbose=True
        )

    @agent
    def file_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['file_writer'],
            tools=[FileWriterTool(overwrite=True)],
            verbose=True
        )

    @task
    def news_site_retriever_task(self) -> Task:
        return Task(
			config=self.tasks_config['news_site_retriever_task'],
		)

    @task
    def website_scraper_task(self) -> Task:
        return Task(
			config=self.tasks_config['website_scraper_task'],
		)

    @task
    def news_writer_task(self) -> Task:
        return Task(
			config=self.tasks_config['news_writer_task'],
		)

    @task
    def file_writer_task(self) -> Task:
        return Task(
			config=self.tasks_config['file_writer_task'],
		)

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True
        )
