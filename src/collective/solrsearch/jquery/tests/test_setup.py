# -*- coding: utf-8 -*-
from collective.solrsearch.jquery.testing import COLLECTIVE_SOLRSEARCH_JQUERY_INTEGRATION_TESTING  # noqa
from plone import api
from zope.component import getMultiAdapter

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.solrsearch.jquery is properly installed."""

    layer = COLLECTIVE_SOLRSEARCH_JQUERY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        self.assertTrue(
            self.installer.isProductInstalled('collective.solrsearch.jquery')
        )

    def test_collective_solr_installed(self):
        self.assertTrue(
            self.installer.isProductInstalled('collective.solr'))

    def test_browserlayer(self):
        from collective.solrsearch.jquery.interfaces import ICollectiveSolrsearchJqueryLayer  # noqa
        from plone.browserlayer import utils
        self.assertTrue(
            ICollectiveSolrsearchJqueryLayer in utils.registered_layers()
        )

    def test_search_view_overridden(self):
        view = getMultiAdapter((self.portal, self.request), name="search")
        view = view.__of__(self.portal)
        self.assertTrue('typeahead.js' in view())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_SOLRSEARCH_JQUERY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.solrsearch.jquery'])

    def test_product_uninstalled(self):
        self.assertFalse(
            self.installer.isProductInstalled('collective.solrsearch.jquery')
        )
