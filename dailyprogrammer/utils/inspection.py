#!/usr/bin/env python

import pkgutil

from dailyprogrammer.utils.logging import moduleLogger

logger = moduleLogger(__name__)

def listModules(package):
    """
    List immediate children of the given package (modules or packages)

    Returns a tuple in the format ``(name, isPackage)``, where ``name`` is the
    string name of the module, and ``isPackage`` is a boolean value.

    :param package: An imported python package
    :rtype: tuple
    """
    logger.debug("Listing modules for {0}".format(package.__name__))
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        yield (modname, ispkg)
