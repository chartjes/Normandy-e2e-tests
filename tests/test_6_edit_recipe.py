"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.nondestructive
def test_edit_recipe(conf, base_url, selenium, foxpuppet, qr_code):
    """Find recipe on home page, and edit recipe."""
    """Check recipe was correctly changed."""
    LDAP = LDAPLogin(selenium, base_url)
    home_page = LDAP.setup(conf, qr_code)
    recipe_page, recipe_name, messages_list = home_page.create_approved_and_enabled_recipe(conf) # noqa
    home_page = recipe_page.click_home_button()
    found_recipe, recipe_page, row_content = home_page.find_recipe_in_table(
     recipe_name)
    recipe_page, messages_list = recipe_page.edit_enabled_recipe(conf)
    home_page = recipe_page.click_home_button()
    found_recipe, recipe_page, row_content = home_page.find_recipe_in_table(
     recipe_name)
    action_selected = recipe_page.get_action_selected
    print("enter browser chrome to check heartbeat")
    assert found_recipe
    assert recipe_page.find_element(*recipe_page.LOCATORS.survey_id).get_attribute('value') == conf.get('recipe', 'recipe_survey_id') # noqa
    assert recipe_page.find_element(*recipe_page.LOCATORS.action_message).get_attribute('value') == conf.get('recipe', 'recipe_message') # noqa
    assert recipe_page.find_element(*recipe_page.LOCATORS.thanks_message).get_attribute('value') == conf.get('recipe', 'recipe_thanks_message') # noqa
    assert recipe_page.find_element(*recipe_page.LOCATORS.post_answer_url).get_attribute('value') == conf.get('recipe', 'recipe_post_url') # noqa
    assert recipe_page.find_element(*recipe_page.LOCATORS.learn_more).get_attribute('value') == conf.get('recipe', 'recipe_learn_more')  # noqa
    assert recipe_page.find_element(*recipe_page.LOCATORS.learn_more_url).get_attribute('value') == conf.get('recipe', 'recipe_learn_more_url') # noqa
    assert action_selected == conf.get('recipe', 'recipe_new_action')
