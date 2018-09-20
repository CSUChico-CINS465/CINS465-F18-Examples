from django.test import TestCase

from .models import SuggestionModel

# Create your tests here.
class SuggestionTestCase(TestCase):
    def setUp(self):
        SuggestionModel.objects.create(suggestion="lion")
        SuggestionModel.objects.create(suggestion="cat")

    def test_suggestion_to_string(self):
        lion = SuggestionModel.objects.get(suggestion="lion")
        cat = SuggestionModel.objects.get(suggestion="cat")
        self.assertEqual(str(lion), 'lion')
        self.assertEqual(str(cat), 'cat')
