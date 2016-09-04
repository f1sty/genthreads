from genthreads.actor import Actor


def test_actor():
    actor = Actor()
    actor.send(42)
    assert actor.inbox == [42]
