from orchestrator.orchestrator import Orchestrator
from architect.architect import Architect
from coder_agents.coder_agent import CoderAgent
from qa_debugger_agent.qa_debugger import QADebuggerAgent
from devops_agent.devops import DevOpsAgent
from refactor_agent.refactor import RefactorAgent
from intelligent_command_environment.ice_interface import ICEInterface

def main():
    print("Initializing Agent-Driven Forge System...")

    # Initialize ICE for developer interaction
    ice = ICEInterface()
    ice.display_activity_stream("System: All agents initializing.")

    # Initialize agents
    orchestrator = Orchestrator()
    architect = Architect()
    # Example: Multiple coder agents
    coder_agent_1 = CoderAgent(agent_id="001_python_backend")
    coder_agent_2 = CoderAgent(agent_id="002_react_frontend")
    qa_debugger = QADebuggerAgent()
    devops_agent = DevOpsAgent()
    refactor_agent = RefactorAgent()

    ice.display_activity_stream("System: All agents initialized.")

    # Get initial high-level requirements from the developer via ICE
    # For now, we'll use a predefined requirement.
    # developer_prompt = ice.get_developer_command()
    developer_prompt = "Build a minimalist blogging platform using FastAPI and React with PostgreSQL for storage."
    ice.display_activity_stream(f"Developer: {developer_prompt}")

    # Orchestrator processes requirements
    ice.display_activity_stream("Orchestrator: Processing requirements.")
    orchestrator.process_requirements(developer_prompt)

    # Architect designs the system
    ice.display_activity_stream("Architect: Designing system architecture based on requirements.")
    system_design_brief = f"High-level requirements: {developer_prompt}" # Brief for the architect
    architecture = architect.design_system(system_design_brief)
    ice.display_activity_stream(f"Architect: System design complete. Tech stack: {architecture.get('tech_stack')}")

    # Orchestrator delegates tasks to Coder Agents (example)
    ice.display_activity_stream("Orchestrator: Delegating tasks to Coder Agents.")
    task1_specs = {"framework": "FastAPI", "endpoint": "/posts", "database": "PostgreSQL"}
    task1_description = "Create API endpoints for blog posts (CRUD operations)."
    ice.display_activity_stream(f"CoderAgent-{coder_agent_1.agent_id}: Received task: {task1_description}")
    generated_code_backend = coder_agent_1.write_code(task1_description, task1_specs)
    # In a real system, this code would be written to files specified by the Architect.
    ice.display_activity_stream(f"CoderAgent-{coder_agent_1.agent_id}: Completed task. Code generated (simulated).")

    task2_specs = {"library": "React", "component_name": "PostDisplayComponent"}
    task2_description = "Create React component to display a list of blog posts."
    ice.display_activity_stream(f"CoderAgent-{coder_agent_2.agent_id}: Received task: {task2_description}")
    generated_code_frontend = coder_agent_2.write_code(task2_description, task2_specs)
    ice.display_activity_stream(f"CoderAgent-{coder_agent_2.agent_id}: Completed task. Code generated (simulated).")

    # QA Agent analyzes and tests the code (example)
    # In a real system, QA would access the actual codebase.
    ice.display_activity_stream("QA_Debugger: Analyzing generated code.")
    qa_debugger.analyze_code(["simulated_backend_code.py", "simulated_frontend_component.js"])
    ice.display_activity_stream("QA_Debugger: Running tests.")
    test_results = qa_debugger.run_tests("all_feature_tests")
    ice.display_activity_stream(f"QA_Debugger: Test results - {test_results}")

    # Refactor Agent scans for improvements (example)
    ice.display_activity_stream("RefactorAgent: Scanning codebase for potential refactors.")
    refactor_suggestions = refactor_agent.scan_codebase("./") # Simulating scan on current dir
    ice.display_activity_stream(f"RefactorAgent: Suggestions - {refactor_suggestions}")

    # DevOps Agent prepares for deployment (example)
    ice.display_activity_stream("DevOpsAgent: Generating Dockerfile.")
    dockerfile_content = devops_agent.generate_dockerfile(architecture)
    ice.display_activity_stream("DevOpsAgent: Dockerfile generated (simulated).")

    ice.display_activity_stream("System: Initial workflow simulation complete.")
    print("\nAgent-Driven Forge System simulation finished.")

if __name__ == '__main__':
    main()
