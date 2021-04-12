def test_user_created_properly(user_fixture):
    assert user_fixture.username == "dummyuser"

    user_fixture.first_name = "John"
    user_fixture.last_name = "Doe"
    user_fixture.save()

    assert user_fixture.username == "john-doe"
