import os
import main
import unittest


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        # DATABASEURI = "postgresql://Linnan@localhost:5432/stock"
        # ENGINE = create_engine(DATABASEURI)
        # try:
        #     self.a = ENGINE.connect()
        # except Exception:
        #     assert "uh oh, problem connecting to database"
        #     # traceback.print_exc()
        #     self.a = None
        # print self.a
        self.app = main.APP.test_client()

    def tearDown(self):
        print "done"
        # try:
        #     self.a.close()
        # except Exception as e:
        #     print "No open database to close"

    def test_empty_db(self):
        rv = self.app.get('/')
        print "pass"

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def test_login(self):
        rv = self.login('admin', 'default')
        assert '2' in rv.data
        rv = self.login('user1', '12345')
        print rv.data
        assert '1' in rv.data
        print "all login are passed"

    def test_get_price(self):
        rv = self.app.get('/get_price')
        print rv.data

    def register(self, username, password):
        return self.app.post('/register', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def test_register(self):
        rv = self.register('admin', 'default')
        assert '1' in rv.data
        rv = self.app.post('/del_user', data=dict(
            username='admin',
        ), follow_redirects=True)
        assert '1' in rv.data

    def test_sell(self):
        rv = self.app.post('/submit', data=dict(
            quantity=100,
        ), follow_redirects=True)
        assert '1' in rv.data

    def test_history(self):
        rv = self.app.get('/b')
        print rv.data
        assert '1' in rv.data

if __name__ == '__main__':
    unittest.main()