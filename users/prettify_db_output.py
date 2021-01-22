def prettify_output(raw_data: list):
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
