import random
from itertools import combinations


round_card_num = [1, 2]
round_num = len(round_card_num)
action_list = ['f', 'c', 'r']
action_encode_num = 'fcr'
action_encode = {action_list[i]: action_encode_num[i] for i in range(len(action_list))}
fold_encode = action_encode['f']
deck = ['2s', '2h', '3s', '3h', '4s', '4h']

# def encode_cards(card_list):
#
#     flu_c = 1
#     flu_map = dict()
#     encode_key = ''
#     for card in sorted_card_list:
#         num, flu = card
#         if flu in flu_map:
#             encode_key += num + flu_map[flu]
#         else:
#             encode_key += num + str(flu_c)
#             flu_map[flu] = str(flu_c)
#             flu_c += 1
#     return encode_key


def encode_cards(card_list):
    return "".join(sorted(card_list))


def get_winner(cards):
    result = ['32', '42', '43', '22', '33', '44']
    # Getting the result of the final round: seven cards
    card = [encode_cards(h) for h in cards]
    h0 = sorted([card[0][0], card[0][2]], reverse=True)
    h1 = sorted([card[1][0], card[1][2]], reverse=True)
    score_0 = result.index("".join(h0))
    score_1 = result.index("".join(h1))

    if score_0 == score_1:
        return [0.5, 0.5]
    else:
        result = [0., 0.]
        if score_0 > score_1:
            result[0] = 1.
        else:
            result[1] = 1.
        return result


def deal_pokers(res_poker):
    result_list = []
    for com in combinations(res_poker, 1):
        com = list(com)
        res_poker2 = res_poker - set(com)
        for com2 in combinations(res_poker2, 1):
            com2 = list(com2)
            res_poker3 = res_poker2 - set(com2)
            for com3 in combinations(res_poker3, 1):
                com3 = list(com3)
                result_list.append([com + com3, com2 + com3])
    return result_list