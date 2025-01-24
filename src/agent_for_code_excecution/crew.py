from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import CodeInterpreterTool
from pathlib import Path

from dotenv import load_dotenv
load_dotenv()


@CrewBase
class AgentForCodeExcecution():
	"""AgentForCodeExcecution crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'


	@agent
	def software_engineer(self) -> Agent:
		return Agent(
			config=self.agents_config['software_engineer'],
			tools=[CodeInterpreterTool(unsafe_mode=True)],
			verbose=True
		)


	@task
	def data_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['data_analysis_task'],
		)


	@crew
	def crew(self) -> Crew:
		"""Creates the AgentForCodeExcecution crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)
