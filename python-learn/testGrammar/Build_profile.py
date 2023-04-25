def build_profile(first_name,last_name,**user_info):
    print(user_info)
    profile = {}
    profile["first_name"] = first_name
    profile["last_name"] = last_name
    for key,value in user_info.items():
        profile[key] = value
    return profile

def func_v1(first_name,last_name,*subject):
    print(first_name)
    print(last_name)
    print(subject)

result_profile = build_profile("ColdBaby","li",age=18,phone=110)
func_v1("ColdBaby","li","yuwen","shuxue","yihngyu")

print(result_profile)
