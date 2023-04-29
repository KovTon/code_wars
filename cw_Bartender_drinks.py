def get_drink_by_profession(param: str):
    param = param.lower().title()

    visitors = ["Jabroni",
                "School Counselor",
                "Programmer",
                "Bike Gang Member",
                "Politician",
                "Rapper"
                ]

    drinks = ["Patron Tequila",
              "Anything with Alcohol",
              "Hipster Craft Beer",
              "Moonshine",
              "Your tax dollars",
              "Cristal"
              ]

    visitors_drink_preferences = dict(zip(visitors, drinks))
    drink = ''
    try:
        visitors_drink_preferences[param]
        drink = visitors_drink_preferences.get(param)
    except KeyError:
        drink = "Beer"
    return drink


print(get_drink_by_profession('School Counselor'))
