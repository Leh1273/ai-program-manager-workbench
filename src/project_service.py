from src.data_loader import load_json_file
from datetime import date

def get_projects(status=None):
    projects = load_json_file("projects.json")

    if status is None:
        return projects

    return [
        project
        for project in projects
        if project["status"] == status
    ]


def get_project(project_id):
    projects = get_projects()

    for project in projects:
        if project["project_id"] == project_id:
            return project

    return None

def get_risks(severity=None, status=None):
    risks = load_json_file("risks.json")

    if severity is not None:
        risks = [
            risk
            for risk in risks
            if risk["severity"] == severity
        ]

    if status is not None:
        risks = [
            risk
            for risk in risks
            if risk["status"] == status
        ]

    return risks

def get_actions(status=None, project_id=None):
    actions = load_json_file("actions.json")

    if status is not None:
        actions = [
            action
            for action in actions
            if action["status"] == status
        ]

    if project_id is not None:
        actions = [
            action
            for action in actions
            if action["project_id"] == project_id
        ]

    return actions

def get_overdue_actions():
    actions = get_actions(status="open")
    today = date.today()

    overdue_actions = []

    for action in actions:
        due_date = date.fromisoformat(action["due_date"])

        if due_date < today:
            overdue_actions.append(action)

    return overdue_actions

def get_milestones(status=None, project_id=None):
    milestones = load_json_file("milestones.json")

    if status is not None:
        milestones = [
            milestone
            for milestone in milestones
            if milestone["status"] == status
        ]

    if project_id is not None:
        milestones = [
            milestone
            for milestone in milestones
            if milestone["project_id"] == project_id
        ]

    return milestones

def get_dependencies(status=None, project_id=None):
    dependencies = load_json_file("dependencies.json")

    if status is not None:
        dependencies = [
            dependency
            for dependency in dependencies
            if dependency["status"] == status
        ]

    if project_id is not None:
        dependencies = [
            dependency
            for dependency in dependencies
            if dependency["project_id"] == project_id
        ]

    return dependencies

def get_upcoming_milestones(days=14):
    milestones = get_milestones()
    today = date.today()
    upcoming_milestones = []

    for milestone in milestones:
        target_date = date.fromisoformat(milestone["target_date"])
        days_until_due = (target_date - today).days

        if 0 <= days_until_due <= days:
            upcoming_milestones.append(milestone)

    return upcoming_milestones

def get_projects_with_high_open_risks():
    projects = get_projects()
    risks = get_risks(severity="high", status="open")

    high_risk_project_ids = {
        risk["project_id"]
        for risk in risks
    }

    return [
        project
        for project in projects
        if project["project_id"] in high_risk_project_ids
    ]

def get_projects_with_overdue_actions():
    projects = get_projects()
    overdue_actions = get_overdue_actions()

    overdue_project_ids = {
        action["project_id"]
        for action in overdue_actions
    }

    return [
        project
        for project in projects
        if project["project_id"] in overdue_project_ids
    ]

def get_projects_with_at_risk_milestones():
    projects = get_projects()
    milestones = get_milestones(status="at-risk")

    at_risk_project_ids = {
        milestone["project_id"]
        for milestone in milestones
    }

    return [
        project
        for project in projects
        if project["project_id"] in at_risk_project_ids
    ]

def get_projects_with_at_risk_dependencies():
    projects = get_projects()
    dependencies = get_dependencies(status="at-risk")

    at_risk_project_ids = {
        dependency["project_id"]
        for dependency in dependencies
    }

    return [
        project
        for project in projects
        if project["project_id"] in at_risk_project_ids
    ]

def get_project_health(project_id):
    project = get_project(project_id)

    if project is None:
        return None

    risks = [
        risk
        for risk in get_risks(status="open")
        if risk["project_id"] == project_id
    ]

    overdue_actions = [
        action
        for action in get_overdue_actions()
        if action["project_id"] == project_id
    ]

    at_risk_milestones = get_milestones(
        status="at-risk",
        project_id=project_id
    )

    at_risk_dependencies = get_dependencies(
        status="at-risk",
        project_id=project_id
    )

    return {
        "project_id": project["project_id"],
        "name": project["name"],
        "status": project["status"],
        "open_risks": len(risks),
        "overdue_actions": len(overdue_actions),
        "at_risk_milestones": len(at_risk_milestones),
        "at_risk_dependencies": len(at_risk_dependencies),
    }
