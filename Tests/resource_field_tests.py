import unittest


class TestPlanet(unittest.TestCase):
    def test_factory_method(self):
        import Models.ResourceField.ResourceFieldFactory as ResourceFactory
        factory_list = (
            ResourceFactory.BalancedResourceFieldFactory(),
            ResourceFactory.RichResourceFieldFactory(),
            ResourceFactory.SparseResourceFieldFactory()
        )
        for factory in factory_list:
            resource_field = factory.factory_method()
            try:
                resource_field.start_mining()  # duck-typing test
            except AttributeError:
                self.fail('Resource Field needs to implement start_mining')

    def test_start_mining(self):
        import Models.ResourceField.ResourceFieldFactory as ResourceFactory
        factory_list = (
            ResourceFactory.BalancedResourceFieldFactory(),
            ResourceFactory.RichResourceFieldFactory(),
            ResourceFactory.SparseResourceFieldFactory()
        )
        for factory in factory_list:
            resource_field = factory.factory_method()
            self.assertTrue(not resource_field.is_mined)
            resource_field.start_mining()
            self.assertTrue(resource_field.is_mined)

    def test_stop_mining(self):
        import Models.ResourceField.ResourceFieldFactory as ResourceFactory
        factory_list = (
            ResourceFactory.BalancedResourceFieldFactory(),
            ResourceFactory.RichResourceFieldFactory(),
            ResourceFactory.SparseResourceFieldFactory()
        )
        for factory in factory_list:
            resource_field = factory.factory_method()
            self.assertTrue(not resource_field.is_mined)
            resource_field.start_mining()
            self.assertTrue(resource_field.is_mined)
            resource_field.stop_mining()
            self.assertTrue(not resource_field.is_mined)
