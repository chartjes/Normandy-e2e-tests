"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin
from tests.conftest import find_recipe_rest_api


@pytest.mark.nondestructive
def test_delete_recipe(conf, base_url, selenium, qr_code):
    """Confirm recipe deleted on home page."""
    LDAP = LDAPLogin(selenium, base_url)
    home_page = LDAP.setup(conf, qr_code)
    recipe_page, recipe_name, messages_list = home_page.create_approved_and_enabled_recipe(conf) # noqa
    home_page = recipe_page.click_home_button()
    found_before_deleted_recipe, recipe_page, row_content = home_page.find_recipe_in_table(recipe_name) # noqa
    home_page, messages_list = recipe_page.delete_recipe()
    found_after_deleted_recipe, recipe_page, row_content = home_page.find_recipe_in_table(recipe_name) # noqa
    found_recipe_in_rest_api = find_recipe_rest_api(conf, recipe_name)
    assert found_before_deleted_recipe
    assert 'Recipe deleted.' in messages_list
    assert not found_after_deleted_recipe
    assert not found_recipe_in_rest_api
