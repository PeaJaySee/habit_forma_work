from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from tracker.models import Habit, Progress
from datetime import date

class HabitListViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.habit = Habit.objects.create(
            description='Test Habit',
            frequency='Daily',
            user=self.user
        )

    def test_habit_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Habit')
        self.assertTemplateUsed(response, 'tracker/habit_list.html')

    def test_mark_complete(self):
        response = self.client.post(reverse('home'), {'complete': '', 'habit_id': self.habit.id})
        self.assertRedirects(response, reverse('home'))
        self.habit.refresh_from_db()
        self.assertTrue(self.habit.is_complete)
        self.assertEqual(self.habit.completion_date, date.today())
        progress = Progress.objects.get(habit=self.habit, date=date.today())
        self.assertTrue(progress.status)

    def test_delete_habit(self):
        response = self.client.post(reverse('home'), {'delete': '', 'habit_id': self.habit.id})
        self.assertRedirects(response, reverse('home'))
        self.assertFalse(Habit.objects.filter(id=self.habit.id).exists())