from .. import celery


@celery.task
def do_big_thing(a):
    print('Doing literally big thing...')
    return "Big thing done: " + a
