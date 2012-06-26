import os, sys

def delete_all():
    from module_list.models import Module

    modules = Module.objects.all()

    for module in modules:
        module.delete()
        print "%s deleted!" % (module.name)
        
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rc_modules.settings")

    delete_all()
