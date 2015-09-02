# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.solrsearch.jquery


class CollectiveSolrsearchJqueryLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.solrsearch.jquery)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.solrsearch.jquery:default')


COLLECTIVE_SOLRSEARCH_JQUERY_FIXTURE = CollectiveSolrsearchJqueryLayer()


COLLECTIVE_SOLRSEARCH_JQUERY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_SOLRSEARCH_JQUERY_FIXTURE,),
    name='CollectiveSolrsearchJqueryLayer:IntegrationTesting'
)


COLLECTIVE_SOLRSEARCH_JQUERY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_SOLRSEARCH_JQUERY_FIXTURE,),
    name='CollectiveSolrsearchJqueryLayer:FunctionalTesting'
)


COLLECTIVE_SOLRSEARCH_JQUERY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_SOLRSEARCH_JQUERY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveSolrsearchJqueryLayer:AcceptanceTesting'
)
