from django.db import models
from django.utils.crypto import get_random_string

def create_market_id():
    unique = False
    while not unique:
        market_id = get_random_string(
            8, allowed_chars='ABCDEFGHIJKLMSOPQRSTUVXYZ')
        if not Market.objects.filter(market_id=id).exists():
            unique = True
    return market_id

class Market(models.Model):
    market_id = models.CharField(max_length=16, primary_key=True)
    alpha = models.DecimalField(max_digits=10, decimal_places=4, default=105)
    beta = models.DecimalField(max_digits=10, decimal_places=4, default=17.5)
    theta = models.DecimalField(max_digits=10, decimal_places=4, default=14.58)
    min_cost = models.PositiveIntegerField(default=5)
    max_cost = models.PositiveIntegerField(default=15)
    round = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        """
        Set unique custom id for market before creating a new market object (not when updating an existing market)
        """
        if not self.market_id: 
            self.market_id = create_market_id()   
        super(Market, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.market_id}[{self.round}]:{self.alpha},{self.beta},{self.theta}"

class Trader(models.Model):
    initial_balance = 5000
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    name = models.CharField(max_length=16,)
    prod_cost = models.IntegerField(default=0)
    balance = models.IntegerField(default=initial_balance, blank=True) # This field is not strictly necessary, as it should always be possible to find this value in a stored Trade object
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f"{self.name} [{self.market.market_id}] - ${self.balance}"

    def is_ready(self):
        has_traded_this_round = Trade.objects.filter(trader=self, round=self.market.round, was_forced=False).count() == 1     
        if has_traded_this_round:
            return True
        else: 
            return False

class Trade(models.Model):
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE)
    unit_price = models.IntegerField(default=0,null=True)
    unit_amount = models.PositiveIntegerField(null=True, default=0)
    round = models.PositiveIntegerField() # not always equal to trader.market.round
    was_forced = models.BooleanField(default=False) 
    profit = models.IntegerField(null=True, blank=True)
    balance_after = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['trader', 'round'], name='trader_and_round_unique'),
        ]
    
    def __str__(self):
        return f"{self.trader.name} ${self.unit_price} x {self.unit_amount} [{self.trader.market.market_id}][{self.round}]"


