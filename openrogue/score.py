import json
from pathlib import Path
from datetime import datetime


class ScoreManager:
    """Manage run scores saved to a JSON file."""

    def __init__(self, path="scores.json"):
        self.path = Path(path)
        self.scores = self._load()

    def _load(self):
        if self.path.exists():
            try:
                with self.path.open("r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, OSError):
                pass
        return []

    def add_score(self, moves):
        self.scores.append({"moves": moves, "ts": datetime.utcnow().isoformat()})
        self._save()

    def _save(self):
        try:
            with self.path.open("w", encoding="utf-8") as f:
                json.dump(self.scores, f, indent=2)
        except OSError:
            pass

    def best_score(self):
        if not self.scores:
            return None
        return min(self.scores, key=lambda s: s.get("moves", float("inf")))
