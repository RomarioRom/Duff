# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: VisitTracker
import unittest
from visit_tracker.models import Visit, Place, Contact, Goal, Note
from visit_tracker.tracker import VisitTracker


class TestEdgeCases(unittest.TestCase):
    def setUp(self):
        self.tracker = VisitTracker()

    def test_visit_with_empty_place(self):
        place = Place(name="", address="", latitude=0, longitude=0, category="")
        visit = Visit(date="2023-01-01", place=place)
        self.assertEqual(visit.place.name, "")

    def test_visit_with_empty_contact(self):
        contact = Contact(name="", phone="", email="", role="")
        visit = Visit(date="2023-01-01", contact=contact)
        self.assertEqual(visit.contact.name, "")

    def test_visit_with_empty_goal(self):
        goal = Goal(topic="", description="", priority="low")
        visit = Visit(date="2023-01-01", goal=goal)
        self.assertEqual(visit.goal.topic, "")

    def test_visit_with_empty_note(self):
        note = Note(content="", date="2023-01-01")
        visit = Visit(date="2023-01-01", note=note)
        self.assertEqual(visit.note.content, "")

    def test_add_multiple_visits(self):
        self.tracker.add_visit(Visit(date="2023-01-01"))
        self.tracker.add_visit(Visit(date="2023-01-02"))
        self.tracker.add_visit(Visit(date="2023-01-03"))
        self.assertEqual(len(self.tracker.visits), 3)

    def test_add_visit_with_all_fields(self):
        place = Place(name="Test Place", address="123 Test St", latitude=40.7128, longitude=-74.0060, category="Business")
        contact = Contact(name="John Doe", phone="1234567890", email="john@example.com", role="Manager")
        goal = Goal(topic="Meeting", description="Discuss project", priority="high")
        note = Note(content="Great meeting", date="2023-01-01")
        visit = Visit(date="2023-01-01", place=place, contact=contact, goal=goal, note=note)
        self.tracker.add_visit(visit)
        self.assertEqual(len(self.tracker.visits), 1)
        self.assertEqual(self.tracker.visits[0].place.name, "Test Place")
        self.assertEqual(self.tracker.visits[0].contact.name, "John Doe")
        self.assertEqual(self.tracker.visits[0].goal.topic, "Meeting")
        self.assertEqual(self.tracker.visits[0].note.content, "Great meeting")

    def test_add_visit_with_none_place(self):
        visit = Visit(date="2023-01-01")
        self.tracker.add_visit(visit)
        self.assertEqual(len(self.tracker.visits), 1)

    def test_add_visit_with_none_contact(self):
        place = Place(name="Test Place", address="123 Test St", latitude=40.7128, longitude=-74.0060, category="Business")
        visit = Visit(date="2023-01-01", place=place)
        self.tracker.add_visit(visit)
        self.assertEqual(len(self.tracker.visits), 1)

    def test_add_visit_with_none_goal(self):
        place = Place(name="Test Place", address="123 Test St", latitude=40.7128, longitude=-74.0060, category="Business")
        visit = Visit(date="2023-01-01", place=place)
        self.tracker.add_visit(visit)
        self.assertEqual(len(self.tracker.visits), 1)

    def test_add_visit_with_none_note(self):
        place = Place(name="Test Place", address="123 Test St", latitude=40.7128, longitude=-74.0060, category="Business")
        visit = Visit(date="2023-01-01", place=place)
        self.tracker.add_visit(visit)
        self.assertEqual(len(self.tracker.visits), 1)

    def test_add_visit_with_invalid_date(self):
        with self.assertRaises(ValueError):
            visit = Visit(date="invalid-date")

    def test_add_visit_with_invalid_latitude(self):
        with self.assertRaises(ValueError):
            place = Place(latitude=999)

    def test_add_visit_with_invalid_longitude(self):
        with self.assertRaises(ValueError):
            place = Place(longitude=999)

    def test_add_visit_with_invalid_priority(self):
        with self.assertRaises(ValueError):
            goal = Goal(priority="urgent")

    def test_add_visit_with_all_fields_set(self):
        place = Place(name="Test Place", address="123 Test St", latitude=40.7128, longitude=-74.0060, category="Business")
        contact = Contact(name="John Doe", phone="1234567890", email="john@example.com", role="Manager")
        goal = Goal(topic="Meeting", description="Discuss project", priority="high")
        note = Note(content="Great meeting", date="2023-01-01")
        visit = Visit(date="2023-01-01", place=place, contact=contact, goal=goal, note=note)
        self.tracker.add_visit(visit)
        self.assertEqual(len(self.tracker.visits), 1)
        self.assertEqual(self.tracker.visits[0].place.name, "Test Place")
        self.assertEqual(self.tracker.visits[0].contact.name, "John Doe")
        self.assertEqual(self.tracker.visits[0].goal.topic, "Meeting")
        self.assertEqual(self.tracker.visits[0].note.content, "Great meeting")


if __name__ == "__main__":
    unittest.main()
