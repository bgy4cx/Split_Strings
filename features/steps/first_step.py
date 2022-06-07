from pytest_bdd import given, when, then
from main import solution

@given('')
def given_impl(context):
    pass

@when('')
def when_impl(context):
    assert (solution("") is [])

@then('')
def then_impl(context):
	assert (solution("") is [])