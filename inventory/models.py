from django.db import models

# Create your models here.

class Property(models.Model):

	HOME_TYPE_CHOICES = (
		('H', 'House'),
		('C', 'Condominium')
	)

	CITY_CHOICES = (
		('TO', 'Toronto'),
		('VAN', 'Vancouver')
	)

	HOUSE_TYPE_CHOICES	= (
		('DETACHED', 'Detached'),
		('SEMI', 'Semi-detached'),
		('ATTACHED', 'Attached')
	)

	BEDROOM_CHOICES = (
		('ONE', '1'),
		('ONEHALF', '1.5'),
		('TWO', '2'),
		('THREE', '3'),
		('FOUR', '4'),
		('FIVE', '5')
	)

	BATH_CHOICES = (
		('ONE', '1'),
		('TWO', '2'),
		('THREE', '3'),
		('FOUR', '4'),
		('FIVE', '5')
	)

	STATUS_CHOICES = (
		('OFFER', 'Make me an offer'),
		('SELL', 'Would sell for the right price'),
		('NEVER', 'Would never sell')
	)

	slug = models.SlugField(max_length=255, unique=False)
	home_type = models.CharField(max_length=25, choices=HOME_TYPE_CHOICES)
	street_number = models.PositiveIntegerField()
	street_address = models.CharField(max_length=255)
	suite_number = models.PositiveIntegerField(blank=True)
	neighborhood = models.CharField(max_length=255)
	city = models.CharField(max_length=255, choices=CITY_CHOICES)
	house_type = models.CharField(max_length=255, choices=HOUSE_TYPE_CHOICES)
	lot_size_frontage = models.IntegerField()
	lot_size_depth = models.IntegerField()
	num_beds = models.CharField(max_length=25, choices=BEDROOM_CHOICES)
	num_baths = models.CharField(max_length=25, choices=BATH_CHOICES)
	num_park = models.IntegerField()
	unlysted_value = models.PositiveIntegerField(blank=True)
	status = models.CharField(max_length=25, choices=STATUS_CHOICES)
	photo = models.ImageField(upload_to='images', blank=True)

	def __unicode__(self):
		return '_'.join([
			str(self.street_number),
			self.street_address,
			self.city,
		])

	@models.permalink
	def get_absolute_url(self):
		return('property-feed', (), {
			'property_slug': self.slug,
			'pk': self.id
			})


