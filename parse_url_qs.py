import json
from urllib.parse import parse_qs


def get_parse_qs(qs: str) -> dict:
    r = parse_qs(qs)
    parsed_query_dict = {}
    for k, v in r.items():

        if len(v) == 1:
            v = v[0]
        parsed_query_dict[k] = v
    return parsed_query_dict


if __name__ == '__main__':
    qs = 'charset=UTF-8&notify_time=2024-05-17+14%3A57%3A37&unsign_time=2024-05-17+14%3A57%3A37&alipay_user_id=205076&sign=VJDgXQZFXlKP6ztdVLHHd8%2FPBqODNxB1eHP5CeDwLDIejPNQgJjB2Sr4pMSxpiwQ%3D%3D&external_agreement_no=cy90100225959&version=1.0&notify_id=213174228&notify_type=dut_sign&agreement_no=202355205007&auth_app_id=20210690218&personal_product_code=CYTH_P&app_id690218&sign_type=A2&alipay_logon_id=139**1233&status=UNSN&sign_scene=INTRY%7CEDU'
    query_dict = get_parse_qs(qs)
    print(json.dumps(query_dict, indent=2))
