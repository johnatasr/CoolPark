from automobilies.models import Automobilie
from automobilies.entities import Automobilie as AutoEntity
from automobilies.repositories import AutomobiliesRepo
from django.test import TestCase


class AutoRepoTestCase(TestCase):
    """
    Tests of AutomobiliesRepo in automobilies.repository.py
    """

    def setUp(self):
        self.repo = AutomobiliesRepo()

    def test_create_auto_model(self):
        auto_entity = AutoEntity(plate="ABC-1234")
        auto = self.repo.create_auto_model(auto_entity)
        self.assertIsInstance(auto, object)
        self.assertEquals(auto.plate, "ABC-1234")

    def test_create_auto(self):
        auto_entity = self.repo.create_auto(plate="CBA-1234")
        self.assertIsInstance(auto_entity, object)
        self.assertEquals(auto_entity.plate, "CBA-1234")
