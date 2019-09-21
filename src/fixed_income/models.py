
""""1 to N: uma empresa pode ter varias emissoes
django

class IssuerData(models.Model):
    company_id = models.IntegerField()
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Identifiers(models.Model):
    # company_id = models.ForeignKey(IssuerData, on_delete=models.CASCADE) #uma empresa tem varias dividas, nesse caso a gnt adiciona o fk na classe 'muitos'
    company_id = models.ForeignKey("IssuerData", on_delete=models.DO_NOTHING)
    generic_id = models.CharField(max_length=12)
    isin_id = models.CharField(max_length=12)
    exchange_id = models.CharField(max_length=20)

class IssuanceData(models.Model):
    generic_id = models.OneToOneField(Identifiers, on_delete=models.DO_NOTHING)
    series = models.CharField(max_length=5)
    currency = models.CharField(max_length=10)
    date_announced = models.DateField()
    date_priced = models.DateField()
    date_settle = models.DateField()
    date_int_accrual = models.DateField()

    date_first_cpn = models.DateField()
    date_maturity = models.DateField()

    issue_amount = models.DecimalField(max_digits=20, decimal_places=4)
    out_amount = models.DecimalField(max_digits=20, decimal_places=4)
    par_amount = models.DecimalField(max_digits=20, decimal_places=4)
    min_piece = models.DecimalField(max_digits=20, decimal_places=4)

class CouponData(models.Model):
    generic_id = models.OneToOneField(Identifiers, on_delete=models.DO_NOTHING)
    cpn_type = models.CharField(max_length=10)
    cpn_rate = models.DecimalField(max_digits=10, decimal_places=8)
    cpn_frequency = models.CharField(max_length=20)
    cpn_day_count = models.CharField(max_length=10)


class RedemptionData(models.Model):
    generic_id = models.OneToOneField(Identifiers, on_delete=models.DO_NOTHING)
    redemption_description = models.CharField(max_length=20)


class IssueType(models.Model):
    generic_id = models.OneToOneField(Identifiers, on_delete=models.DO_NOTHING)
    market_of_issue = models.CharField(max_length=20)


class Calcs (models.Model):
    generic_id = models.OneToOneField(Identifiers, on_delete=models.DO_NOTHING)
    calculation_type = models.IntegerField()


class CollateralData(models.Model):
    generic_id = models.OneToOneField(Identifiers, on_delete=models.DO_NOTHING)
    collateral_type  = models.CharField(max_length=20)


class Exchanges(models.Model):
    generic_id = models.OneToOneField(Identifiers, on_delete=models.DO_NOTHING)
    exchange_name = models.CharField(max_length=30)


class Notes(models.Model):
    generic_id = models.OneToOneField(Identifiers, on_delete=models.DO_NOTHING)
    des_note = models.TextField()

class SinkSchedule(models.Model):
    generic_id = models.OneToOneField(Identifiers, on_delete=models.DO_NOTHING)
    # sink_date = models.DateField()
    My_CHOICES = (('item_key1', 'Item title 1.1'),
                  ('item_key2', 'Item title 1.2'),
                  ('item_key3', 'Item title 1.3'))

    sink_rate = models.DecimalField(max_digits=10, decimal_places=8)
    # sink_date = models.DateField(choices=My_CHOICES)
    sink_date = models.DateField()

"""
