def match_places():
    """
    Match places between location table and population table
    """
    # Full path to your django project directory
    your_djangoproject_home="./commute"

    import sys,os
    sys.path.append(your_djangoproject_home)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

    import django
    django.setup()

    from traveltime.models import Population, uk_location

    success = 0
    fail = 0

    for pop in Population.objects.all():

        m1 = uk_location.objects.filter(place_name = pop.place_name)
        if len(m1) == 1:
            pop.location = m1[0]
            pop.save()
            success += 1
            continue

        if pop.region_name is not None:
            m2 = uk_location.objects.filter(place_name = pop.region_name)
            if len(m2) == 1:
                pop.location = m2[0]
                pop.save()
                success += 1
                continue

        m3 = uk_location.objects.filter(place_name__contains = pop.place_name)
        if len(m3) > 0:
            pop.location = m3[0]
            pop.save()
            success += 1
            continue

        if pop.region_name is not None:
            m4 = uk_location.objects.filter(place_name__contains = pop.region_name)
            if len(m4) > 0:
                pop.location = m4[0]
                pop.save()
                success += 1
                continue

        fail += 1
        print("Failed to match %s" % pop.place_name)



    print("Matched %d / %d" % (success, fail + success))

if __name__ == '__main__':
    match_places()