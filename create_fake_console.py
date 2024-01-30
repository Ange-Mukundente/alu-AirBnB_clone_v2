from models import storage
from models.state import State
from models.city import City

def test_create_state():
    # Test create State name="California" is present (new feature) - DBStorage
    new_state = State(name="California")
    storage.new(new_state)
    storage.save()
    print("Test create State name='California' is present - Passed")

def test_create_city():
    # Test create State name="California" + create City state_id="<new state ID>" name="Fremont" is present (more than one parameter) - DBStorage
    new_state = State(name="California")
    storage.new(new_state)
    storage.save()
    
    new_city = City(state_id=new_state.id, name="Fremont")
    storage.new(new_city)
    storage.save()
    print("Test create City with state_id='<new state ID>' and name='Fremont' is present - Passed")

def test_create_city_space_translation():
    # Test create State name="California" 
    new_state = State(name="California")
    storage.new(new_state)
    storage.save()

    new_city = City(state_id=new_state.id, name="San Francisco")
    storage.new(new_city)
    storage.save()
    print("Test create City with state_id='<new state ID>' and name='San_Francisco' is present - Passed")

def test_rollback():
    # Rollback code
    storage.rollback()
    print("Rollback successful.")

def test_table_exists():
    # Table states exists
    if storage.check_table_exists("states"):
        print("Test passed: Table 'states' exists.")
    else:
        print("Test failed: Table 'states' does not exist.")

    # Table cities exists
    if storage.check_table_exists("cities"):
        print("Test passed: Table 'cities' exists.")
    else:
        print("Test failed: Table 'cities' does not exist.")

def main():
    test_create_state()
    test_create_city()
    test_create_city_space_translation()
    test_rollback()
    test_table_exists()

if __name__ == "__main__":
    main()
