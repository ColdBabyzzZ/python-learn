def greet_user(username):
    print(f"Hello ! {username}")

def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

greet_user("ColdBaby")
describe_pet(pet_name="weiwei",animal_type="dog")