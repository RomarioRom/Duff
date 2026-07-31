# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: VisitTracker
class Profile:
    def __init__(self, name, email=""):
        self.name = name
        self.email = email

    def to_dict(self):
        return {"name": self.name, "email": self.email}

    @classmethod
    def from_dict(cls, d):
        return cls(name=d["name"], email=d.get("email", ""))


class ProfileManager:
    _profiles = {}

    def __init__(self):
        try:
            import json
            with open("profiles.json", "r") as f:
                data = json.load(f)
                for d in data:
                    self._profiles[d["name"]] = Profile.from_dict(d)
        except FileNotFoundError:
            pass

    def add(self, name, email=""):
        if name in self._profiles:
            return False
        p = Profile(name=name, email=email)
        self._profiles[name] = p
        try:
            import json
            with open("profiles.json", "w") as f:
                json.dump([p.to_dict() for p in self._profiles.values()], f, indent=2)
        except Exception:
            pass
        return True

    def delete(self, name):
        if name not in self._profiles:
            return False
        del self._profiles[name]
        try:
            import json
            with open("profiles.json", "w") as f:
                json.dump([p.to_dict() for p in self._profiles.values()], f, indent=2)
        except Exception:
            pass
        return True

    def get(self, name):
        return self._profiles.get(name)

    def list_all(self):
        return [p.name for p in self._profiles.values()]
