import datetime
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(day=None):
    day = day or datetime.datetime.now(datetime.timezone.utc).date()
    ideas = json.loads((ROOT / "ideas/backlog.json").read_text(encoding="utf-8"))
    if not ideas or len({x["slug"] for x in ideas}) != len(ideas):
        raise ValueError("Ideas must be non-empty and have unique slugs")
    idea = ideas[(day - datetime.date(2026, 10, 15)).days % len(ideas)]
    dest = ROOT / "proposals" / day.isoformat() / (idea["slug"] + ".md")
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists():
        dest.write_text("# " + idea["name"] + "\n\n## Problem\n" + idea["problem"] + "\n\n## Platform\n" + idea["platform"] + "\n\n## Language\n" + idea["language"] + "\n\n## MVP\n" + idea["mvp"] + "\n\n## Review checklist\n- [ ] Useful MVP delivered\n- [ ] Tests pass\n- [ ] No secrets\n- [ ] Destructive actions have dry-run\n- [ ] Documentation exists\n\nThis file is a proposal, **not implemented application code**.\n", encoding="utf-8")
    manifest = ROOT / "automation-runs" / (day.isoformat() + ".json")
    if not manifest.exists():
        manifest.write_text(json.dumps({"date":day.isoformat(),"slug":idea["slug"],"proposal":dest.relative_to(ROOT).as_posix(),"review_required":True,"status":"proposal_generated","implementation_generated":False},indent=2)+"\n",encoding="utf-8")
    print(dest.relative_to(ROOT))
    return dest


if __name__ == "__main__":
    run(datetime.date.fromisoformat(os.environ["FACTORY_DATE"]) if os.getenv("FACTORY_DATE") else None)
