# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: VisitTracker
import unittest
from visit_tracker.models import Visit, Place, Contact, Goal


class TestVisitTracker(unittest.TestCase):
    def setUp(self):
        self.place = Place("Coffee Shop", "cafe", "123 Main St")
        self.contact = Contact("John", "+1234567890", "john@example.com")
        self.goal = Goal("Discuss new project", "2024-01-15")
        self.visit = Visit(self.place, self.contact, self.goal)

    def test_place_attributes(self):
        self.assertEqual(self.place.name, "Coffee Shop")
        self.assertEqual(self.place.category, "cafe")
        self.assertEqual(self.place.address, "123 Main St")

    def test_contact_attributes(self):
        self.assertEqual(self.contact.first_name, "John")
        self.assertEqual(self.contact.phone, "+1234567890")
        self.assertEqual(self.contact.email, "john@example.com")

    def test_goal_attributes(self):
        self.assertEqual(self.goal.text, "Discuss new project")
        self.assertEqual(self.goal.target_date, "2024-01-15")

    def test_visit_attributes(self):
        self.assertEqual(self.visit.place.name, "Coffee Shop")
        self.assertEqual(self.visit.contact.first_name, "John")
        self.assertEqual(self.visit.goal.text, "Discuss new project")

    def test_visit_summary(self):
        self.visit.notes = "Great meeting!"
        summary = self.visit.summary()
        self.assertIn("Coffee Shop", summary)
        self.assertIn("John", summary)
        self.assertIn("Great meeting!", summary)


if __name__ == "__main__":
    unittest.main()
