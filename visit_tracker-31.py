# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: VisitTracker
class Profile:
    def __init__(self, name, email="", phone=""):
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {"name": self.name, "email": self.email, "phone": self.phone}

    @classmethod
    def from_dict(cls, data):
        return cls(name=data["name"], email=data.get("email", ""), phone=data.get("phone", ""))


class ProfileManager:
    def __init__(self):
        self.profiles = []
        self.active_profile_name = None

    def add(self, name, email="", phone=""):
        profile = Profile(name=name, email=email, phone=phone)
        if name in [p.name for p in self.profiles]:
            return False
        self.profiles.append(profile)
        if not self.active_profile_name and len(self.profiles) == 1:
            self.active_profile_name = profile.name
        return True

    def set_active(self, name):
        for p in self.profiles:
            if p.name == name:
                self.active_profile_name = name
                return True
        return False

    def get_current(self):
        return None if not self.active_profile_name else next((p for p in self.profiles if p.name == self.active_profile_name), None)

    def list_profiles(self):
        result = []
        for p in self.profiles:
            active = (p.name == self.active_profile_name)
            result.append({"name": p.name, "email": p.email, "phone": p.phone, "active": active})
        return result

    def save(self):
        data = [{"name": p.name, "email": p.email, "phone": p.phone} for p in self.profiles]
        if self.active_profile_name:
            data.append({"active_profile": self.active_profile_name})
        return {"profiles": data}

    @classmethod
    def load(cls, data):
        mgr = cls()
        profile_data = data.get("profiles", [])
        for pd in profile_data[:-1]:
            mgr.profiles.append(Profile.from_dict(pd))
        if len(profile_data) > 0 and isinstance(profile_data[-1], dict):
            active = profile_data[-1].get("active_profile")
            if active:
                mgr.active_profile_name = active
        return mgr

    def export(self, output_path="profiles.json"):
        import json
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump({"profiles": self.profiles}, f)
