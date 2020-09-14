"""
Trello board testing
"""
from trello_util_fun import Trello_Util
from authorization import key, token
from data_variables import board_name, card_names, list_names  # sample_board, sample_cards, member_ids, member_username


def test_trello_util(key, token):
    # Creating an object of Trello Util
    test_obj = Trello_Util(key, token)
    # Get the board names from config
    current_board_name = list(set(board_name))
    print("Board Names from the current list", current_board_name)
    new_board_name = current_board_name[0]
    current_list_name = list(set(list_names))
    print("List Names from the current list", current_list_name)
    current_card_name = list(set(card_names))
    print("Card Names from the current list", current_card_name)


    """ Create a new board """
    result_flag = test_obj.add_board(new_board_name)
    if result_flag == True:
        print("Able to add New board with name %s" % new_board_name)
    else:
        print("Not able to add new with name %s" % new_board_name)

    """ Add list to the newly created board """

    result_flag = test_obj.add_list(new_board_name, current_list_name)
    if result_flag == True:
        print("Able to add list_name %s to board name %s" % (current_list_name, new_board_name))
    else:
        print("Not able to add list_name %s to board name %s" % (current_list_name, new_board_name))


    """ Add card to the list names """
    result_flag = test_obj.add_card(new_board_name, current_list_name, current_card_name)
    if result_flag == True:
        print("Able to add card_names %s to list name %s" % (current_card_name, current_list_name))
    else:
        print("Not able to add card_names %s to list name %s" % (current_card_name, current_list_name))


    """ Add comment to the card from the card names list """
    result_flag = test_obj.add_comment_to_card(new_board_name, current_card_name)
    if result_flag == True:
        print("Able to add new comment to the card %s to list name %s" % (current_card_name, current_list_name))
    else:
        print("Not able to add new comment to the card %s to list name %s" % (current_card_name, current_list_name))


    """ Edit / update the comment to the card from the card names list """
    result_flag = test_obj.edit_comment(new_board_name, current_card_name)
    if result_flag == True:
        print("Able to edit the newly added comment to the card")
    else:
        print("Not able to edit the newly added new comment to the card")

    """Delete a card from the card names list"""
    result_flag = test_obj.delete_card(new_board_name, current_card_name)
    if result_flag == True:
        print("Able to delete card from card names")
    else:
        print("Not able to delete card from card name")


if __name__ == '__main__':
    test_trello_util(key=key, token=token)
