def prettify_pagination_output(raw_data: list):
    output = []
    for tuple_ in raw_data:
        user = {
                'user_id': tuple_[0],
                'first_name': tuple_[1],
                'last_name': tuple_[2],
                'email': tuple_[3],
                'gender': tuple_[4],
                'ip_address': tuple_[5],
                'total_clicks': tuple_[6],
                'total_page_views': tuple_[7],
                }
        output.append(user)

    return output


def prettify_user_stats(raw_data: list):
    output = []
    for tuple_ in raw_data:
        user_stats = {
                    'user_id': tuple_[0],
                    'date': tuple_[1],
                    'page_views': tuple_[2],
                    'clicks': tuple_[3],
                    }
        output.append(user_stats)

    return output
