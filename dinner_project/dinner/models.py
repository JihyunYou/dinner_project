from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class UserInfo(models.Model):
	user_id = models.CharField(primary_key=True, max_length=4, validators=[MinLengthValidator(4)])
	user_name = models.CharField(max_length=10, null=False)
	user_phone = models.CharField(max_length=4)

	def __str__(self):
		return f'{self.user_id}:{self.user_name}'

class CardInfo(models.Model):
	"""Model representing a card info."""
	card_name = models.CharField(max_length=20, help_text='Enter a Card Infomation (e.g. 개발운영2실')
	card_number = models.CharField(max_length=12, help_text='카드번호')

	def __str__(self):
		return self.card_name

class Chit(models.Model):
	"""Model representing a chit info 전표 사용 내역 입력"""
	base_date = models.DateField(null=False, blank=False)
	card = models.ForeignKey('CardInfo', on_delete=models.SET_NULL, null=True)
	amount = models.IntegerField(default=0)
	place = models.CharField(max_length=20, help_text="주문장소")
	order_user = models.ForeignKey('UserInfo', on_delete=models.SET_NULL, null=True)
	number_of_user = models.IntegerField()
	list_of_user = models.TextField(max_length=500, help_text='먹은 인원')

	MEAL_TYPE =  (
		('1', '야근식비'),
		('2', '접대비'),
		('3', '휴일근무식비'),
	)

	meal_type = models.CharField(
		max_length=1,
		choices=MEAL_TYPE,
		default='1',
		help_text='야근식비/접대비/휴일근무식비'
	)

	class Meta:
		ordering = ['-base_date', 'card']

	def __str__(self):
		return f'{self.base_date}[{self.card}]:{self.amount}'