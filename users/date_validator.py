import re


def validate_date_format(date: str) -> str:
    date_mask = re.compile(r'\d{4}-\d{2}-\d{2}')  # 2020-01-03 is the correct format
    try:
        match_obj = date_mask.search(date)
        return match_obj.group()
    except AttributeError:
        return None
