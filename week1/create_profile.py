def create_profile(**kwargs):
    kwargs["status"] = "active"

    return kwargs

print(create_profile(name="Shura", city="Lviv"))
print(create_profile(nickname="coshurra"))