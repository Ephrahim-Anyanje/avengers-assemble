from app import app, db
from seed import seed_database
import json

EXPECTED_HERO_KEYS = {'id','name','super_name'}
EXPECTED_POWER_KEYS = {'id','name','description'}


def run():
    with app.app_context():
        seed_database()

        client = app.test_client()

        # GET /heroes
        r = client.get('/heroes')
        assert r.status_code == 200
        heroes = r.get_json()
        assert isinstance(heroes, list)
        assert EXPECTED_HERO_KEYS.issubset(set(heroes[0].keys()))

        
        r = client.get('/heroes/1')
        assert r.status_code == 200
        hero = r.get_json()
        assert EXPECTED_HERO_KEYS.issubset(set(hero.keys()))
        assert 'hero_powers' in hero

        
        r = client.get('/powers')
        assert r.status_code == 200
        powers = r.get_json()
        assert isinstance(powers, list)
        assert EXPECTED_POWER_KEYS.issubset(set(powers[0].keys()))

        
        r = client.get('/powers/1')
        assert r.status_code == 200
        power = r.get_json()
        assert EXPECTED_POWER_KEYS.issubset(set(power.keys()))

        
        r = client.patch('/powers/1', json={'description': 'short'})
        assert r.status_code == 400
        data = r.get_json()
        assert 'errors' in data

        
        new_desc = 'This is a sufficiently long description for the power.'
        r = client.patch('/powers/1', json={'description': new_desc})
        assert r.status_code == 200
        data = r.get_json()
        assert data['description'] == new_desc

        
        payload = {'hero_id': 1, 'power_id': 1, 'strength': 'Strong'}
        r = client.post('/hero_powers', json=payload)
        assert r.status_code == 201
        hp = r.get_json()
        assert hp['strength'] == 'Strong'
        assert 'hero' in hp and 'power' in hp

        print('All smoke tests passed')


if __name__ == '__main__':
    run()
