from django.db import models

# Create your models here.
class TestConfig(models.Model):
    name = models.CharField(max_length=128,unique=True)

    configPart = models.TextField()
    staticPart = models.TextField()

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.name

'''
this class stores all Templates of TCL files that are used to create confuguration of the test
'''
class Template (models.Model):
    name = models.CharField(max_length=128,unique=True,default='default')
    configPart = models.TextField(default='COPY TCL TEMPLATE HERE')

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.name
'''
special class that stores configuration of the chassis which autobuddy connects to execute the test
I'll figure out later how to change mode from test classes
'''
class chassisConfig(models.Model):
    name = models.CharField(max_length=128,unique=True)
    ip = models.GenericIPAddressField(protocol='IPv4')
    username = models.CharField(max_length=128, default='admin')
    password = models.CharField(max_length=128, default='admin')
    group = models.IntegerField(default=10)
    MODE_CHOISES = (
    ('setCardModeBPS_L23', 'L3'),
    ('setCardModeBPS', 'L4'),
    )
    crdMode = models.CharField(max_length=128,choices=MODE_CHOISES,
                                      default='setCardModeBPS')
    card = models.IntegerField(default=1)
    port1 = models.IntegerField(default=0)
    port2 = models.IntegerField(default=4)
    configfields = models.CharField(max_length=300,default='card crdMode config ip name password port1 port2 username group')
    config = models.ForeignKey(Template)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.name
'''
special class that stores tcl configuration of the neighborhood part of the test
'''
class neighborhoodConfig(models.Model):
    name = models.CharField(max_length=128,unique=True)
    configPart = models.TextField()
    configfields = models.CharField(max_length=300,default='name')

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.name
'''
this class stores  results of the executed tests of all types
'''
class Result(models.Model):
    name = models.CharField(max_length=128,unique=True)
    type = models.CharField(max_length=128, null=True)
    device = models.CharField(max_length=128,null=True)
    software = models.CharField(max_length=128,null=True)
    STATUS_CHOISES = (
    ('A', 'Active'),
    ('P', 'Passed'),
    ('F', 'Failed'),
    ('N', 'Not started'),
    )
    status = models.CharField(max_length=128,choices=STATUS_CHOISES,
                                      default='N')
    result = models.TextField()
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.name
'''
models below are special classes that are particular tests. They contain config of the test, which is mostly values of variables which are located in Template
Every test has similar parameters:
    name - name of the test, it is used to call this particular configuration ( model object)
    steadyTime - every test has steady time value - time interval in which traffic should be generated without fails to consider test successfull
    config - Template. Variables inside the template begin with %. They are replaced with configFields
    configfiels - fields of the object which have similar names as variables in template config - they values replace variables in template which begins with %
    resultkey - regexp pattern which is used to find the result of the test after it was executed
    dutprofile - name of the DUT profile

    other fieds are TEST SPECIFIC fields that change variables in that specific tests

    LEts try to do JSON tests to create one model which has all similar values as
'''
class cpsTest(models.Model):
    name = models.CharField(max_length=128,unique=True)
    cpsMAX = models.IntegerField(default=5000)
    cpsSTEP = models.IntegerField(default=50)
    failSTEP = models.IntegerField(default=50)
    steadyTime = models.IntegerField(default=1)
    configfields = models.CharField(max_length=300,default='cpsMAX cpsSTEP failSTEP neighborhood failSTEP dutprofile')
    config = models.ForeignKey(Template)
    neighborhood = models.ForeignKey(neighborhoodConfig)
    dutprofile = models.CharField(max_length=128,default='BreakingPoint Default')
    resultkey = models.CharField(max_length=128,default=r'MAX_CPS:.+')
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.name

class udpTest(models.Model):
    name = models.CharField(max_length=128,unique=True)
    allowedDrop = models.FloatField(default=0.3)
    tputMAX = models.IntegerField(default=1000)
    tputSTEP = models.IntegerField(default=1)
    steadyTime = models.IntegerField(default=1)
    packetSizelist = models.CharField(max_length=300,default='64 128 256 512 1024 1500')
    configfields = models.CharField(max_length=300,default='allowedDrop steadyTime tputSTEP tputMAX packetSizelist dutprofile neighborhood')
    config = models.ForeignKey(Template)
    dutprofile = models.CharField(max_length=128,default='BreakingPoint Default')
    neighborhood = models.ForeignKey(neighborhoodConfig)
    resultkey = models.CharField(max_length=128,default=r'pkt:.+')

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.name

class ccTest(models.Model):
    name = models.CharField(max_length=128,unique=True)
    steadyTime = models.IntegerField(default=1)
    rateMAX = models.IntegerField(default=2000)
    failSTEP = models.IntegerField(default=50)
    configfields = models.CharField(max_length=300,default='rateMAX steadyTime failSTEP rateMAX steadyTime failSTEP dutprofile neighborhood')
    config = models.ForeignKey(Template)
    dutprofile = models.CharField(max_length=128,default='BreakingPoint Default')
    neighborhood = models.ForeignKey(neighborhoodConfig)
    resultkey = models.CharField(max_length=128,default=r'MAX_CC:.+')
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.name

class tpsTest(models.Model):
    name = models.CharField(max_length=128,unique=True)
    tpsMAX = models.IntegerField(default=10000)
    tpsSTEP = models.IntegerField(default=100)
    failSTEP = models.IntegerField(default=100)
    tputMAX = models.IntegerField(default=1000)
    steadyTime = models.IntegerField(default=1)
    modifier = models.IntegerField(default=10)
    configfields = models.CharField(max_length=300,default='tpsMAX tpsSTEP tputMAX steadyTime failSTEP neighborhood modifier dutprofile')
    config = models.ForeignKey(Template)
    dutprofile = models.CharField(max_length=128,default='BreakingPoint Default')
    neighborhood = models.ForeignKey(neighborhoodConfig)
    resultkey = models.CharField(max_length=128,default=r'MAX_TPS:.+')
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.name

class httpTest(models.Model):
    name = models.CharField(max_length=128,unique=True)
    tputMAX = models.IntegerField(default=100)
    failSTEP = models.IntegerField(default=50)
    steadyTime = models.IntegerField(default=1)
    configfields = models.CharField(max_length=300,default='tputMAX failSTEP steadyTime dutprofile neighborhood')
    config = models.ForeignKey(Template)
    dutprofile = models.CharField(max_length=128,default='BreakingPoint Default')
    neighborhood = models.ForeignKey(neighborhoodConfig)
    resultkey = models.CharField(max_length=128,default=r'rsp:.+')

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.name