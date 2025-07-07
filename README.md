
# Vision Wagon Project

This repository contains the technical implementation of the Vision Wagon ecosystem, an AI-powered business intelligence platform designed to automate the Software Development Life Cycle (SDLC) and connect SMEs with the digital economy.

## Project Structure

The project is organized into several key directories, each serving a specific purpose:

*   `agents/`: Contains the core AI agents that drive the Vision Wagon ecosystem.
    *   `executive/`: Executive agents responsible for high-level strategic tasks (e.g., `SecurityAgent`, `IntelligenceAgent`).
    *   `operational/`: Operational agents responsible for specific functional tasks (e.g., `CopywriterAgent`, `PsychologyAgent`, `AssemblyAgent`).
    *   `core/`: Core components and base classes for agents (e.g., `base_agent.py`).
*   `api/`: Houses the FastAPI application that exposes the Vision Wagon functionalities through a RESTful API.
*   `database/`: Contains database models (using SQLAlchemy) and related utilities (e.g., `database_models.py`).
*   `orchestrator/`: Manages workflows and task orchestration across different agents (e.g., `orchestrator.py`).
*   `security/`: Implements security-related functionalities, such as input validation and threat detection (e.g., `security_validator.py`).
*   `constructor/`: Contains the `ConstructorAgent` system, a meta-programming tool responsible for automating code generation and project scaffolding.
    *   `constructor_agent_system.py`: The core logic of the ConstructorAgent, including data models, code templates, and build tasks.
    *   `constructor_cli.py`: A command-line interface (CLI) for interacting with the ConstructorAgent.
*   `tests/`: Contains unit and integration tests for various components of the system.
    *   `agents/`: Tests for AI agents.
    *   `api/`: Tests for the API endpoints.
    *   `database/`: Tests for database models and operations.
*   `config/`: Stores configuration files for the application.
*   `blueprints/`: Contains YAML blueprint files used by the `ConstructorAgent` to define project structures and agent specifications.
*   `logs/`: Directory for application logs.
*   `docs/`: Project documentation.

## Getting Started

To set up the Vision Wagon project locally, follow these steps:

### 1. Clone the Repository

```bash
git clone <repository_url>
cd vision_wagon
```

### 2. Create a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Initialize Project Structure (using ConstructorAgent CLI)

The `ConstructorAgent` can help you set up the basic project structure and configuration files.

```bash
python constructor_cli.py init
```

This command will create necessary directories and initial configuration files like `requirements.txt` and `.gitignore`.

### 5. Running the API (Example)

To run the FastAPI application, navigate to the `api` directory and use `uvicorn`:

```bash
cd api
uvicorn main:app --reload
```

This will start the API server, typically accessible at `http://127.0.0.1:8000`.

## ConstructorAgent Usage

The `constructor_cli.py` provides several commands to interact with the `ConstructorAgent`:

*   **`init`**: Initializes the basic project structure and configuration files.
    ```bash
    python constructor_cli.py init
    ```

*   **`build --blueprint <path_to_blueprint.yml>`**: Builds project components based on a YAML blueprint file. Blueprints define agents, database models, API endpoints, and more.
    ```bash
    python constructor_cli.py build --blueprint blueprints/my_project_blueprint.yml
    ```

*   **`status`**: Displays the current project status and the build history.
    ```bash
    python constructor_cli.py status
    ```

*   **`validate --blueprint <path_to_blueprint.yml>`**: Validates a YAML blueprint file for correctness.
    ```bash
    python constructor_cli.py validate --blueprint blueprints/my_project_blueprint.yml
    ```

*   **`generate --type <blueprint|agent_spec> [--output <output_file>]`**: Generates template YAML files for blueprints or agent specifications.
    ```bash
    python constructor_cli.py generate --type blueprint --output blueprints/new_blueprint_template.yml
    python constructor_cli.py generate --type agent_spec
    ```

## Contributing

We welcome contributions to the Vision Wagon project. Please refer to the `CONTRIBUTING.md` (to be created) for guidelines on how to contribute.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.


