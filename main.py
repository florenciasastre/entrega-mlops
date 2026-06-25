"""UrbanPlan AI entrypoint.

This project is designed to be launched through Google ADK:

    uv run adk web src

The `root_agent` is defined in `src/urbanplan/agent.py`.
"""

from urbanplan.agent import root_agent


def main() -> None:
    print("UrbanPlan AI permit intelligence system is ready.")
    print("Run with: uv run adk web src")
    print(f"Loaded agent: {root_agent.name}")


if __name__ == "__main__":
    main()
