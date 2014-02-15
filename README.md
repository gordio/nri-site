NRI-site
========

**Site in development**
NRI Photographer site


Depends
=======

 * python-3.3
 * virtualenv
 * fabric


Usage
=====

0. Configure `settings_local.py` exmpl: `cp nri/settings_local.py{_example,}`
1. `fab build` - build site environment
2. `fab run` or `fab run:0.0.0.0:8080` - run dev server
3. `fab manage:shell`, `fab manage:'dbshell -h'`, etc...
