import requests
import pytest
from test_base import TestBase

#create a class for the endpoint
class TestUsers(TestBase):

    #positive test case as class method
    #@pytest.mark.smoke
    def test_user_by_id(self):
     
        endpoint = f'{self.base_url}/users/10'

        response = requests.get(endpoint)
        data = response.json()

        assert response.status_code == 200
        assert data['data']['id'] == 10
        assert 'data' in data.keys()
        assert 'support' in data.keys()


    #negative test case
    def test_non_existent_user(self):
        endpoint = f'{self.base_url}/users/100'

        response = requests.get(endpoint)

        assert response.status_code == 404
    #delete user test case
    def test_delete_user(self):
     
        endpoint = f'{self.base_url}/users/10'

        response = requests.delete(endpoint)

        assert response.status_code == 204

    def test_view_all_user_pages(self):
        endpoint = f'{self.base_url}/users'

        current_page = 1
        total_pages = 1

        while current_page <= total_pages:
            params = {'page': current_page}
            response = requests.get(endpoint, params=params)
            print(response.url)

            data = response.json()
            total_pages = data['total_pages']
            users = data['data']
            for user in users:
                print(user['email'])
                assert 'email' in user.keys()
        

            current_page += 1
    ids = range(1, 11)
    @pytest.mark.parametrize('id', ids)
    def test_view_user_by_multiple_ids(self, id):
     
        endpoint = f'{self.base_url}/users/{id}'

        response = requests.get(endpoint)
        print(response.url)

        data = response.json()



        assert response.status_code == 200
        #assert data['data']['id'] == 10
        #assert 'data' in data.keys()
        #assert 'support' in data.keys()

        assert 'email' in data['data'].keys()
        
        assert '@' in data['data']['email']
