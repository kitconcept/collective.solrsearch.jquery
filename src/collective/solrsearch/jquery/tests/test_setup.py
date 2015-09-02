# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.solrsearch.jquery.testing import COLLECTIVE_SOLRSEARCH_JQUERY_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that collective.solrsearch.jquery is properly installed."""

    layer = COLLECTIVE_SOLRSEARCH_JQUERY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.solrsearch.jquery is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.solrsearch.jquery'))

    def test_browserlayer(self):
        """Test that ICollectiveSolrsearchJqueryLayer is registered."""
        from collective.solrsearch.jquery.interfaces import ICollectiveSolrsearchJqueryLayer
        from plone.browserlayer import utils
        self.assertIn(ICollectiveSolrsearchJqueryLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_SOLRSEARCH_JQUERY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.solrsearch.jquery'])

    def test_product_uninstalled(self):
        """Test if collective.solrsearch.jquery is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('collective.solrsearch.jquery'))
