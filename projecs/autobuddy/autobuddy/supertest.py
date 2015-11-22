__author__ = 'narek'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autobuddy.settings')
import django
import re,subprocess
from os.path import expanduser
from time import gmtime, strftime,localtime
from auto.models import TestConfig,chassisConfig,neighborhoodConfig,cpsTest,Result,udpTest,ccTest,tpsTest,httpTest

django.setup()

'''
this is global variables ( thats why i defined them i uppercase). I will optimise they usage later
'''
TESTNAME = "Dude" #name of the test ( should be derived from web)

TIMENOW = strftime("%y-%m-%d-%H-%M-%S", localtime())
LOCALPATH =  os.path.dirname(os.path.realpath(__file__))
CONFIGFILE = LOCALPATH+'/tester/TEST_'+TESTNAME +'_'+ TIMENOW + '.tcl'
TEMPFILE = LOCALPATH+'/tester/TEMP_'+TESTNAME +'_'+ TIMENOW + '.tcl'
BPSHFILE = expanduser("~")+'/.bpsh/bin/bpsh '

'''
this function is used to replace configfields values from template of the test to it value, which is defined in particular model object
'''
def find_and_replace(regexp,value):
    global TEMPFILE
    global TEXTTOEDIT
    pattern = r'%'+regexp #creating a pattern to match
    result = re.sub(pattern,value,TEXTTOEDIT) #replacing file
    f_out = file(TEMPFILE, 'w') #writing to temptile
    f_out.write(result)
    f_out.close()
    fh = file(TEMPFILE, 'r') #reading from tempfile to chage globalvalue
    TEXTTOEDIT = fh.read()
    fh.close()
#adds edited text to config file
'''
this function is used to add edited template to configuration file. Used to sum chassis, neighborhood and test parts together

'''
def write_to_config_file():
    global CONFIGFILE
    global TEMPFILE
    with open(CONFIGFILE,'a') as myFile:
        myFile.write("\n")
        fh = file(TEMPFILE, 'r')
        myFile.write(fh.read())
#creates part of config - iterated throgh model values that should be used as regexp in config template
'''
this function is used to iterate over all configfields which are needed to be replaced by according values from test model object

'''
def create_part_of_config(model):
    checklist = model.configfields.split()
    for field in model._meta.get_all_field_names():
        if any(field in s for s in checklist):
            find_and_replace(field,str(getattr(model, field)))
    write_to_config_file()

'''
this function is used to run the test and derive the result value. It does next things:
    creates result record in database which has the name of the test, its type and changes status to active
    executes tcl file from BPSH and writes all output to logfile
    after the execution it looks to the logfile to find result by regexp matching ( derived from resultkey field of the particular key)

'''
def run_and_write_result(model):
    resultName = model.name + " " + TIMENOW #creates result object in database when test is started
    result = Result.objects.get_or_create(name=resultName)[0]
    types_list = [cpsTest,udpTest,ccTest,tpsTest,httpTest]
    for type in types_list:
        if isinstance(model,type):
            result.type = type.__name__
    result.status = 'A'
    result.save()
    LOGFILE =  LOCALPATH+'/log/'+TESTNAME +'_'+resultName+'.log'
    os.remove(TEMPFILE)
    with open(LOGFILE, 'w') as f: #runs test and writes output to log file
	    subprocess.call(BPSHFILE + CONFIGFILE,shell=True,stdout=f)
    with open(LOGFILE, 'r') as f: #looks in logfile to derive the result
        subject = f.read()
        f.close()
        found = re.findall(model.resultkey,subject)
        if found:
            res = ''
            for i in found:
                res = res + i
                res = res + "\r"
            result.result = res
            result.status = 'P'
            os.remove(CONFIGFILE)
        else:
            result.result = 'n/a'
            result.status = 'F'
        result.save()
'''
this function creates chassis part of the tcl file
'''

def create_chassispart(chassisname): #this function creates chassis part of the config, which is called by create_and_run_func
    global TEXTTOEDIT
    CHASSIS = chassisConfig.objects.get(name =chassisname)
    TEXTTOEDIT = CHASSIS.config.configPart #we derive a part of config to edit
    create_part_of_config(CHASSIS)
'''
this function creates neighborhood  part of the tcl file
'''
def create_neighborhoodpart(neighborhoodname): #this function creates neighborhood part of the config, which is called by create_and_run_func
    global TEXTTOEDIT
    NEIGHBORHOOD = neighborhoodConfig.objects.get(name=neighborhoodname)
    TEXTTOEDIT = NEIGHBORHOOD.configPart
    create_part_of_config(NEIGHBORHOOD)
'''
this 'main' function that manages creation and execution of the test. It does
    creation of chassis, neighborhood and test parts of the config by executing according functions
    execution of the created tcl file by executing according function
'''
def create_and_run_test(test,testname,chassisname,neighborhoodname): #this is "main" function - it calls functions which creates all parts of config and runs
    global TEXTTOEDIT
    create_chassispart(chassisname)
    create_neighborhoodpart(neighborhoodname)
    TEST = test.objects.get(name=testname)
    TEXTTOEDIT = TEST.config.configPart
    create_part_of_config(TEST)
    run_and_write_result(TEST)



#run
create_and_run_test(test=cpsTest,testname='CPS',chassisname='PsOne_L4',neighborhoodname='Routed_Network')







