import json

from src.utils.last_run_tracker import (
    check_and_skip_if_same_issue,
    load_last_run_info,
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


def test_last_run_tracker_migrates_legacy_file_to_env_path(monkeypatch, tmp_path):
    state_file = tmp_path / "outputs" / "last_run_info.json"
    legacy_file = tmp_path / "last_run_info.json"
    legacy_file.write_text(
        json.dumps(
            {
                "reactweekly": {
                    "full_url": "https://react.statuscode.com/issues/472",
                }
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("LAST_RUN_INFO_PATH", str(state_file))

    data = load_last_run_info()

    assert data["reactweekly"]["full_url"] == "https://react.statuscode.com/issues/472"
    assert json.loads(state_file.read_text(encoding="utf-8")) == data


def test_last_run_tracker_reads_backup_when_primary_is_corrupt(monkeypatch, tmp_path):
    state_file = tmp_path / "outputs" / "last_run_info.json"
    state_file.parent.mkdir()
    state_file.write_text("{broken json", encoding="utf-8")
    state_file.with_suffix(state_file.suffix + ".bak").write_text(
        json.dumps(
            {
                "frontendfoc": {
                    "full_url": "https://frontendfoc.us/issues/739",
                }
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("LAST_RUN_INFO_PATH", str(state_file))

    should_skip = check_and_skip_if_same_issue(
        "frontendfoc",
        "issues/739",
        "https://frontendfoc.us",
    )

    assert should_skip is True
    assert json.loads(state_file.read_text(encoding="utf-8"))["frontendfoc"]["full_url"] == (
        "https://frontendfoc.us/issues/739"
    )


def test_last_run_tracker_keeps_backup_before_replacing_state(monkeypatch, tmp_path):
    state_file = tmp_path / "outputs" / "last_run_info.json"
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

    update_last_run_info(
        "javascriptweekly",
        {"full_url": "https://javascriptweekly.com/issues/784"},
    )

    payload = json.loads(state_file.read_text(encoding="utf-8"))
    backup = json.loads(state_file.with_suffix(state_file.suffix + ".bak").read_text(encoding="utf-8"))
    assert payload["nodeweekly"]["full_url"] == "https://nodeweekly.com/issues/622"
    assert payload["javascriptweekly"]["full_url"] == "https://javascriptweekly.com/issues/784"
    assert backup == {
        "nodeweekly": {
            "full_url": "https://nodeweekly.com/issues/622",
        }
    }
