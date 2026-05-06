import json

from src.utils.last_run_tracker import (
    check_and_skip_if_same_issue,
    update_last_run_info,
)


def test_last_run_tracker_uses_env_path_for_reads(monkeypatch, tmp_path):
    state_file = tmp_path / "state" / "last_run_info.json"
    state_file.parent.mkdir()
    state_file.write_text(
        json.dumps(
            {
                "nodeweekly": {
                    "full_url": "https://nodeweekly.com/issues/622",
                }
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("LAST_RUN_INFO_PATH", str(state_file))

    should_skip = check_and_skip_if_same_issue(
        "nodeweekly",
        "issues/622",
        "https://nodeweekly.com",
    )

    assert should_skip is True


def test_last_run_tracker_uses_env_path_for_writes(monkeypatch, tmp_path):
    state_file = tmp_path / "state" / "last_run_info.json"
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("LAST_RUN_INFO_PATH", str(state_file))

    update_last_run_info(
        "javascriptweekly",
        {"full_url": "https://javascriptweekly.com/issues/784"},
    )

    payload = json.loads(state_file.read_text(encoding="utf-8"))
    assert payload["javascriptweekly"]["full_url"] == "https://javascriptweekly.com/issues/784"
