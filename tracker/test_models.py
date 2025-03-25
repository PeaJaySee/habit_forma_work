from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date
from tracker.models import Habit, Progress

#model testing

class HabitModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.habit = Habit.objects.create(
            description='Test Habit',
            frequency='Daily',
            user=self.user
        )

    def test_habit_creation(self):
        self.assertEqual(self.habit.description, 'Test Habit')
        self.assertEqual(self.habit.frequency, 'Daily')
        self.assertEqual(self.habit.user, self.user)

    def test_mark_complete(self):
        self.habit.mark_complete()
        self.assertTrue(self.habit.is_complete)
        self.assertEqual(self.habit.completion_date, date.today())
        progress = Progress.objects.get(habit=self.habit, date=date.today())
        self.assertTrue(progress.status)

class ProgressModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.habit = Habit.objects.create(
            description='Test Habit',
            frequency='Daily',
            user=self.user
        )
        self.progress = Progress.objects.create(
            habit=self.habit,
            date=date.today(),
            status=True
        )

    def test_progress_creation(self):
        self.assertEqual(self.progress.habit, self.habit)
        self.assertEqual(self.progress.date, date.today())
        self.assertTrue(self.progress.status)

