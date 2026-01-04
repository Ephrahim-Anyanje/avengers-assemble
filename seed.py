from app import app, db
from models import Hero, Power, HeroPower

def seed_database():
    with app.app_context():
        db.session.query(HeroPower).delete()
        db.session.query(Hero).delete()
        db.session.query(Power).delete()
        db.session.commit()

        heroes_data = [
            {'name': 'Kamala Khan', 'super_name': 'Ms. Marvel'},
            {'name': 'Doreen Green', 'super_name': 'Squirrel Girl'},
            {'name': 'Gwen Stacy', 'super_name': 'Spider-Gwen'},
            {'name': 'Janet Van Dyne', 'super_name': 'The Wasp'},
            {'name': 'Wanda Maximoff', 'super_name': 'Scarlet Witch'},
            {'name': 'Carol Danvers', 'super_name': 'Captain Marvel'},
            {'name': 'Jean Grey', 'super_name': 'Dark Phoenix'},
            {'name': 'Ororo Munroe', 'super_name': 'Storm'},
            {'name': 'Kitty Pryde', 'super_name': 'Shadowcat'},
            {'name': 'Elektra Natchios', 'super_name': 'Elektra'}
        ]

        heroes = []
        for hero_data in heroes_data:
            hero = Hero(**hero_data)
            db.session.add(hero)
            heroes.append(hero)

        powers_data = [
            {'name': 'super strength', 'description': 'gives the wielder super-human strengths'},
            {'name': 'flight', 'description': 'gives the wielder the ability to fly through the skies at supersonic speed'},
            {'name': 'super human senses', 'description': 'allows the wielder to use her senses at a super-human level'},
            {'name': 'elasticity', 'description': 'can stretch the human body to extreme lengths'}
        ]

        powers = []
        for power_data in powers_data:
            power = Power(**power_data)
            db.session.add(power)
            powers.append(power)

        db.session.commit()

        hero_powers_data = [
            {'hero_id': 1, 'power_id': 2, 'strength': 'Strong'},
            {'hero_id': 2, 'power_id': 1, 'strength': 'Average'},
            {'hero_id': 3, 'power_id': 3, 'strength': 'Weak'},
            {'hero_id': 4, 'power_id': 4, 'strength': 'Strong'}
        ]

        for hp_data in hero_powers_data:
            hero_power = HeroPower(**hp_data)
            db.session.add(hero_power)

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()
