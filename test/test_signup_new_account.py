def test_signup_new_account(app):
    username="user11"
    password="password"
    app.james.ensure_user_exists(username,password)
