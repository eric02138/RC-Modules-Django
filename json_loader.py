import os, sys

def json_load():
    from module_list.models import Module
    from django.utils import timezone
    import json
    import urllib2
    import datetime
    
    url = urllib2.urlopen('http://modules.rc.fas.harvard.edu/api/1/avail/index.html')
    contents = url.read()

    json_str = json.loads(contents)
    for module, details in json_str['modules'].items():
        print "Adding %s to database..." % module

        m = Module()
        m.name = module
        m.updated = datetime.datetime.fromtimestamp(float(details.get('modulefile_updated', 'no updated value'))).replace(tzinfo=timezone.utc)
        m.help_text = details.get('help', 'no help value')
        m.whatis = details.get('whatis', 'no whatis value')

        #print m.__dict__
        m.save()
        print "...saved"

        #print "\t%s" % (details.get('help', 'no help value'))
        #print "\t%s" % (datetime.datetime.fromtimestamp(float(details.get('modulefile_updated', 'no updated value'))))
        #print "\t%s" % (details.get('whatis', 'no whatis value'))
        
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rc_modules.settings")

    json_load()
