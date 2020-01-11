import pytest


@pytest.mark.django_db
def test_job_archive_get(tp, django_assert_num_queries, joblisting):
    with django_assert_num_queries(0):
        response = tp.get("job_archive", pk=joblisting.pk)
    tp.assert_http_302_found(response)


@pytest.mark.django_db
def test_job_create_get(tp, django_assert_num_queries):
    with django_assert_num_queries(0):
        response = tp.get("job_create")
    tp.assert_http_302_found(response)


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
