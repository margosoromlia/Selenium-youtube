import time

import pytest

from pom.homepge_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        # actual_link = homepage_nav.det_nav_links_text()
        # expected_links = homepage_nav.NAV_LINK_TEXT
        # assert expected_links == actual_link, 'Validating Nav Links text'
        cookies = homepage_nav.driver.get_cookies()
        print(cookies)
        elements = homepage_nav.get_nav_links()
        for indx in range(len(elements)):
            homepage_nav.get_nav_links()[indx].click()
            time.sleep(1.5)
            self.driver.back()
