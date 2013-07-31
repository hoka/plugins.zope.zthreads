plugins.zope.zthreads
=====================

Show zope threads as stack to debug deadlocks.

it can be called from the browserr of your choice as followed.
The browsers is only accessible form the zope site root.

http://IP_OR_DOMAIN:PORT/@@zthreads

Code is tested against

- Zope2-2.13.20

may also works in earlier zope versions.

z3c.deadlockdebugger seems to be no longer maintained, the latest package 0.2 is not working in my latest zope / plone buildouts, so here an updated version.