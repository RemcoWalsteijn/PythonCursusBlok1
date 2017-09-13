def lang_genoeg(lengte):
    ''''Checkt of de gebruiker lang genoeg is om in de attractie te mogen'''
    if lengte >= 120:
        return('Je bent lang genoeg voor de attractie!')
    else:
        return('Sorry, je bent te klein!')

print(lang_genoeg(119))