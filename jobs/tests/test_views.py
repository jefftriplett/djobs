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
def test_job_edit_get(tp, django_assert_num_queries, joblisting):
    with django_assert_num_queries(0):
        response = tp.get("job_edit", pk=joblisting.pk)
    tp.assert_http_302_found(response)


@pytest.mark.django_db
def test_job_feed_get(tp, django_assert_num_queries):
    with django_assert_num_queries(2):
        response = tp.get("job_feed")
    tp.assert_http_200_ok(response)


@pytest.mark.django_db
def test_job_flag_get(tp, django_assert_num_queries, joblisting):
    with django_assert_num_queries(0):
        response = tp.get("job_flag", pk=joblisting.pk)
    tp.assert_http_405_method_not_allowed(response)


@pytest.mark.django_db
def test_job_publish_get(tp, django_assert_num_queries, joblisting):
    with django_assert_num_queries(0):
        response = tp.get("job_publish", pk=joblisting.pk)
    tp.assert_http_302_found(response)


@pytest.mark.django_db
def test_job_list_get(tp, django_assert_num_queries):
    with django_assert_num_queries(1):
        response = tp.get("job_list")
    tp.assert_http_200_ok(response)


@pytest.mark.django_db
def test_login_get(tp, django_assert_num_queries):
    with django_assert_num_queries(0):
        response = tp.get("login")
    tp.assert_http_404_not_found(response)


@pytest.mark.django_db
def test_logout_get(tp, django_assert_num_queries):
    with django_assert_num_queries(0):
        response = tp.get("logout")
    tp.assert_http_302_found(response)


@pytest.mark.django_db
def test_review_flags_get(tp, django_assert_num_queries):
    with django_assert_num_queries(0):
        response = tp.get("flags")
    tp.assert_http_404_not_found(response)
