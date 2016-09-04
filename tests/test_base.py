import pytest
from genthreads import actor


def test_actor_inbox():
    act = actor.Actor()
    act.send(42)
    assert act.inbox == [42]


@pytest.mark.xfail(raises=actor.InboxFullError)
def test_full_inbox_error():
    act = actor.Actor()
    for i in range(49):
        act.send(i)
