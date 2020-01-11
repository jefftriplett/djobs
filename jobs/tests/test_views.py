import pytest


def test_job_detail_uri(tp, joblisting):
    expected_url = f"/{joblisting.pk}/"
    reversed_url = tp.reverse("job_detail", pk=joblisting.pk)
    assert expected_url == reversed_url


def test_job_feed_uri(tp):
    expected_url = "/feed/"
    reversed_url = tp.reverse("job_feed")
    assert expected_url == reversed_url


def test_job_list_uri(tp):
    expected_url = "/"
    reversed_url = tp.reverse("job_list")
    assert expected_url == reversed_url


@pytest.mark.django_db
def test_job_detail_get(tp, django_assert_num_queries, joblisting):
    with django_assert_num_queries(3):
        response = tp.get("job_detail", pk=joblisting.pk)
    tp.assert_http_200_ok(response)


@pytest.mark.django_db
def test_job_feed_get(tp, django_assert_num_queries):
    with django_assert_num_queries(1):
        response = tp.get("job_feed")
    tp.assert_http_200_ok(response)


@pytest.mark.django_db
def test_job_list_get(tp, django_assert_num_queries):
    with django_assert_num_queries(1):
        response = tp.get("job_list")
    tp.assert_http_200_ok(response)
