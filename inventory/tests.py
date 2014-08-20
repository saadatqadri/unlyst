from django.test import TestCase

# Create your tests here.
from inventory.models import Property

class PropertyTests(TestCase):

	def test_str(self)

		prop = Property(home_type = 'HOUSE',
						street_number = 60,
						street_address = 'Heintzman',
						suite_number = 1911,
						neighborhood = 'Junction',
						city = 'TO',
						house_type = 'DETACHED',
						lot_size_frontage = 560,
						lot_size_depth = 234,
						num_beds = '4',
						num_baths = '1',
						num_park = '1',
						unlysted_value = 279000,
						status = 'OFFER'
				)

		self.assertEquals(
			init(prop),
			'60_Heintzman_Toronto',
			)
