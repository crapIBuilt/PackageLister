import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
   for i in installed_packages])
po = 0
out = open('packs.txt', 'a')
for x in installed_packages_list:
    t = installed_packages_list[po].split("==", 1)
    out.write(t[0])
    out.write('\n')
    po += 1
out.close()
