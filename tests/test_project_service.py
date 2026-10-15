from src.project_service import (
    get_projects,
    get_project,
    get_risks,
    get_actions,
    get_milestones,
    get_dependencies,
    get_project_health,
)


def test_get_projects_returns_all_projects():
    projects = get_projects()

    assert len(projects) == 6


def test_get_project_returns_correct_project():
    project = get_project("PRJ-001")

    assert project is not None
    assert project["name"] == "Cloud Platform Migration"


def test_get_project_returns_none_for_invalid_id():
    project = get_project("PRJ-999")

    assert project is None


def test_get_projects_can_filter_by_status():
    projects = get_projects(status="red")

    assert len(projects) == 1
    assert projects[0]["project_id"] == "PRJ-003"


def test_get_risks_can_filter_by_severity_and_status():
    risks = get_risks(severity="high", status="open")

    assert len(risks) > 0

    for risk in risks:
        assert risk["severity"] == "high"
        assert risk["status"] == "open"


def test_get_actions_can_filter_by_project():
    actions = get_actions(project_id="PRJ-003")

    assert len(actions) > 0

    for action in actions:
        assert action["project_id"] == "PRJ-003"


def test_get_milestones_can_filter_by_status():
    milestones = get_milestones(status="at-risk")

    assert len(milestones) > 0

    for milestone in milestones:
        assert milestone["status"] == "at-risk"


def test_get_dependencies_can_filter_by_project():
    dependencies = get_dependencies(project_id="PRJ-001")

    assert len(dependencies) > 0

    for dependency in dependencies:
        assert dependency["project_id"] == "PRJ-001"


def test_get_project_health_returns_expected_fields():
    health = get_project_health("PRJ-003")

    assert health is not None
    assert health["project_id"] == "PRJ-003"
    assert health["name"] == "SaaS Security Remediation"

    assert "status" in health
    assert "open_risks" in health
    assert "overdue_actions" in health
    assert "at_risk_milestones" in health
    assert "at_risk_dependencies" in health


def test_get_project_health_returns_none_for_invalid_project():
    health = get_project_health("PRJ-999")

    assert health is None
