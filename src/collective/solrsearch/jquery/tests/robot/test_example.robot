# ============================================================================
# EXAMPLE ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s collective.solrsearch.jquery -t test_example.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src collective.solrsearch.jquery.testing.COLLECTIVE_SOLRSEARCH_JQUERY_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/collective/solrsearch/jquery/tests/robot/test_example.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a member I want to be able to log into the website
  [Documentation]  Example of a BDD-style (Behavior-driven development) test.
  Given the search form
    and a document with the title 'Welcome to Plone'
   When I search for 'Plone'
   Then the search results contain 'Welcome to Plone'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

the search form
  Go To  ${PLONE_URL}/search

a document with the title '${title}'
  Enable autologin as  Contributor
  ${uid}=  Create content  type=Document  title=${title}
#  Fire transition  ${uid}  publish
#  Disable autologin


# --- WHEN -------------------------------------------------------------------

I search for '${term}'
  Input Text  SearchableText  ${term}
  Click Button  Search


# --- THEN -------------------------------------------------------------------

the search results contain '${title}'
  Wait until page contains  Search results
  Page should contain  ${title}
  Debug
