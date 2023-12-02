from task2 import get_data, get_posts


def test_check_post_existence(auth_token):
    config_data = get_data()
    url_posts = config_data['url_posts']
    required_post_id = 90800

    posts_data = get_posts(auth_token, url_posts)
    posts_ids = [post.get('id') for post in posts_data]

    assert required_post_id in posts_ids, f"Пост с ID {required_post_id} не найден в ответе от сервера"
