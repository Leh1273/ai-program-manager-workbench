# AI Program Manager Workbench

## Overview

AI Program Manager Workbench is a Python portfolio project that turns simulated enterprise project data into actionable program-management insights. It analyzes risks, action items, milestones, dependencies, and project health.

**Phase 1 is complete:** the JSON data foundation, Python service layer, and 10 passing automated tests are in place. The project is designed to use the Model Context Protocol (MCP); MCP implementation begins in Phase 2.

## Architecture

### Current Phase 1 Architecture

```text
JSON data files → Python data loader → Python service layer → Project insights
```

`data_loader.py` reads local JSON files. `project_service.py` provides retrieval, filtering, and program-management business logic. Tests validate the service layer independently of an AI client.

### Future Architecture

```text
User ↔ AI client ↔ MCP server ↔ Python service layer ↔ JSON / external APIs
```

The planned MCP server will expose service-layer capabilities to an AI client. External integrations will follow in later phases; neither MCP nor an AI client is implemented in Phase 1.

## Project Structure

```text
ai-program-manager-workbench/
├── data/
│   ├── projects.json
│   ├── risks.json
│   ├── actions.json
│   ├── milestones.json
│   └── dependencies.json
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   └── project_service.py
├── tests/
│   └── test_project_service.py
├── requirements.txt
└── README.md
```

## Phase 1

Completed capabilities:

- JSON-based project data and a reusable Python data loader.
- Service-layer functions to retrieve and filter projects, risks, actions, milestones, and dependencies.
- Overdue action detection for open actions with due dates before today.
- Upcoming milestone detection within a configurable window (14 days by default).
- Identification of projects with high open risks, overdue actions, at-risk milestones, or at-risk dependencies.
- `get_project_health()` to combine project status with counts of open risks, overdue actions, at-risk milestones, and at-risk dependencies.
- Automated testing with pytest: **10 tests passing**.

## Running the Tests

From the repository root, install the project dependencies and run the test suite:

```bash
python3 -m pip install -r requirements.txt
python3 -m pytest -q
```

Phase 1 runtime code uses the Python standard library. Development and test dependencies are listed in `requirements.txt`.

## Example using get_project_health()

Run this Python code from the repository root:

```python
from pprint import pprint

from src.project_service import get_project_health

health = get_project_health("PRJ-003")
pprint(health)
```

The result includes `project_id`, `name`, `status`, `open_risks`, `overdue_actions`, `at_risk_milestones`, and `at_risk_dependencies`. Open risks include all severities, and overdue action counts depend on the current date. An unknown project ID returns `None`.

## Roadmap

| Phase | Focus | Status / planned outcome |
| --- | --- | --- |
| Phase 1: Python + JSON | Data loading, service logic, and automated tests | **Complete** |
| Phase 2: MCP Server | Expose service-layer capabilities through MCP | **Next** |
| Phase 3: AI Client | Connect an AI client for natural-language project queries | Planned |
| Phase 4: External Integration | Connect external project-management data sources and APIs | Planned |
| Phase 5: Advanced PM Intelligence | Expand cross-project analysis and decision support | Planned |

## Purpose / Skills Demonstrated

This project demonstrates translating technical program-management needs into testable software: Python development, JSON data modeling, separation of data access and business logic, date-based analysis, and automated testing with pytest. Its phased design provides a foundation for future MCP, AI client, and API integration work.
