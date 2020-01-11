import pytest

from model_bakery import baker

from ..models import JobListing


@pytest.fixture()
def flag(db, joblisting):
    return baker.make("jobs.Flag", job=joblisting)


@pytest.fixture()
def joblisting(db):
    return baker.make("jobs.JobListing", status=JobListing.STATUS_ACTIVE)


@pytest.fixture()
def user(db):
    return baker.make("auth.User")
