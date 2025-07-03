class CoderAgent:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        print(f"Coder Agent {self.agent_id} initialized")

    def write_code(self, task_description, specifications):
        print(f"Coder Agent {self.agent_id} received task: {task_description}")
        print(f"Adhering to specifications: {specifications}")
        # TODO: Implement code generation based on task and specs
        generated_code = f"# Code for {task_description}\nprint('Hello from Coder Agent {self.agent_id}')"
        return generated_code

if __name__ == '__main__':
    coder1 = CoderAgent(agent_id="001")
    code = coder1.write_code(
        task_description="Build user authentication endpoint",
        specifications={"framework": "FastAPI", "endpoint": "/auth/login"}
    )
    print(f"Generated code by Coder 1:\n{code}")

    coder2 = CoderAgent(agent_id="002")
    code_react = coder2.write_code(
        task_description="Create the login React component",
        specifications={"library": "React", "component_name": "LoginComponent"}
    )
    print(f"Generated code by Coder 2:\n{code_react}")
