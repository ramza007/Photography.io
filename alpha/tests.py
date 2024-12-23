from django.test import TestCase
from .models import Location, Timeshot, Details

# Create your tests here.

# <--------------- Location Test class --------------->

class LocationTestClass(TestCase):

    # Setting up method
    def setUp(self):
        self.kilimani = Location(Location = 'Kilimani')

# Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kilimani, Location))

# Testing save method
    def test_save_inatsnce(self):
        self.kilimani.save_editor()
        location = Location.objects.all()
        self.assertTrue(len(location)>0)

    def test_get_location(self):
        location_taken = Location.location_taken()

    def tearDown(self):
        Location.objects.all().delete()

# <--------------- End Location Test class --------------->


# <--------------- TimeShot Test class --------------->
class TimeshotTestClass(TestCase):
    def setUp(self):
        self.evening = Timeshot(Timeshot = 'Evening')

# Test the instance
    def test_instance(self):
        self.assertTrue(isinstance(self.evening, Timeshot))

# Testing the method
    def test_save_instance(self):
        self.evening.save_editor()
        timeshot = Timeshot.objects.all()
        self.assertTrue(len(timeshot)>0)

    def tearDown(self):
        Timeshot.objects.all().delete()
# <--------------- End Timeshot Test class --------------->


# <--------------- Details Test class --------------->
class DetailsTestCase(TestCase):
    def setUp(self):
        self.hello = Details(Details = 'Hello')

# Testing the instance
    def test_instance(self):
        self.assertTrue(isinstance(self.hello, Details))

# Testing the method
    def test_save_inatsnce(self):
        self.hello.save_editor()
        details = Details.objects.all()
        self.assertTrue(len(details)>0)

    def tearDown(self):
        Details.objects.all().delete()

# <--------------- End details Test class --------------->

# <--------------- Image Test class --------------->
