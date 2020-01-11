def test_job_archive_uri(tp, joblisting):
    expected_url = f"/{joblisting.pk}/archive/"
    reversed_url = tp.reverse("job_archive", pk=joblisting.pk)
    assert expected_url == reversed_url


def test_job_create_uri(tp):
    expected_url = "/new/"
    reversed_url = tp.reverse("job_create")
    assert expected_url == reversed_url


def test_job_detail_uri(tp, joblisting):
    expected_url = f"/{joblisting.pk}/"
    reversed_url = tp.reverse("job_detail", pk=joblisting.pk)
    assert expected_url == reversed_url


def test_job_edit_uri(tp, joblisting):
    expected_url = f"/{joblisting.pk}/edit/"
    reversed_url = tp.reverse("job_edit", pk=joblisting.pk)
    assert expected_url == reversed_url


def test_job_feed_uri(tp):
    expected_url = "/feed/"
    reversed_url = tp.reverse("job_feed")
    assert expected_url == reversed_url


def test_job_flag_uri(tp, joblisting):
    expected_url = f"/{joblisting.pk}/flag/"
    reversed_url = tp.reverse("job_flag", pk=joblisting.pk)
    assert expected_url == reversed_url


def test_job_publish_uri(tp, joblisting):
    expected_url = f"/{joblisting.pk}/publish/"
    reversed_url = tp.reverse("job_publish", pk=joblisting.pk)
    assert expected_url == reversed_url


def test_job_list_mine_uri(tp):
    expected_url = "/mine/"
    reversed_url = tp.reverse("job_list_mine")
    assert expected_url == reversed_url


def test_job_list_uri(tp):
    expected_url = "/"
    reversed_url = tp.reverse("job_list")
    assert expected_url == reversed_url


def test_login_uri(tp):
    expected_url = "/login/"
    reversed_url = tp.reverse("login")
    assert expected_url == reversed_url


def test_logout_uri(tp):
    expected_url = "/logout/"
    reversed_url = tp.reverse("logout")
    assert expected_url == reversed_url


def test_review_flags_uri(tp):
    expected_url = "/flags/"
    reversed_url = tp.reverse("review_flags")
    assert expected_url == reversed_url
