import requests

class Trello_Util:
    """Trello util to
        create board,
        create list ,
        create cards to that list name
        Edit a card
        Add a new comment to the card """

    def __init__(self, key, token):
        self.auth = {'key': key, 'token': token}
        self.url = "https://trello.com/1"
        self.headers = {
            'type': "type",
            'content-type': "application/json"
        }

    def get_account_details(self):
        "Get the details of the user"
        result_flag = False
        get_account_details_url = 'https://trello.com/1/member/me'
        try:
            response = requests.get(url=get_account_details_url, params=self.auth)
            if response.status_code == 200:
                self.boards = response.json()['idBoards']
                result_flag = True
        except Exception as e:
            print(str(e))

        return result_flag

    def get_board_names(self):
        get_board_url = 'https://trello.com/1/boards'
        board_list = []
        try:
            response = requests.get(url=get_board_url, params=self.auth)
            response = response.json()
            for i in range(len(response)):
                board_list.append(response[i]["name"])
        except Exception as e:
            print(str(e))

        return board_list


    def add_board(self, board_name):
        """Add board using board name"""
        result_flag = False
        self.payload = self.auth.copy()
        self.payload['name'] = board_name
        self.payload['defaultLists'] = "false"
        url = self.url + "/boards/"
        response = requests.post(url=url, data=self.payload)
        if response.status_code == 200:
            result_flag = True

        return result_flag


    def add_card(self, new_board_name, list_names, card_names):
        """Add Card to the list item"""
        result_flag = False
        self.payload = self.auth.copy()
        board_list_id = self.get_list_id(new_board_name, list_names)
        for i in range(len(card_names)):
            self.payload['name'] = card_names[i]
            self.payload['defaultLists'] = "false"
            self.payload['idBoard'] = board_list_id[0]
            self.payload['idLabels'] = []
            self.payload['idList'] = board_list_id[1]
            url = self.url + "/cards/"
            response = requests.post(url=url, data=self.payload)
            if response.status_code == 200:
                result_flag = True

        return result_flag


    def delete_card(self, board_name, card_names):
        """Add Card to the list item"""
        result_flag = False
        self.payload = self.auth.copy()
        card_id = self.get_card_id(board_name, card_names)
        self.payload['defaultLists'] = "false"
        url = self.url + "/cards/" + card_id
        response = requests.delete(url=url, data=self.payload)
        if response.status_code == 200:
            result_flag = True
            return result_flag


    def add_comment_to_card(self, board_name, card_names):
        """Add Card to the list item"""
        result_flag = False
        self.payload = self.auth.copy()
        card_id = self.get_card_id(board_name, card_names)
        self.payload['defaultLists'] = "false"
        self.payload['text'] = "Hello Welcome to my Trello Cards"
        url = self.url + "/cards/" + card_id + "/actions/" + "comments"
        response = requests.post(url=url, data=self.payload)
        if response.status_code == 200:
            result_flag = True
            return result_flag

    def edit_comment(self, board_name, card_names):
        """Add Card to the list item"""
        result_flag = False
        self.payload = self.auth.copy()
        card_id = self.get_card_id(board_name, card_names)
        action_id = self.get_action_id_name(board_name, card_names)
        self.payload['text'] = "Comment edited / Updated the comment"
        url = self.url + "/cards/" + card_id + "/actions/" + action_id + "/comments"
        response = requests.put(url=url, data=self.payload)
        if response.status_code == 200:
            result_flag = True
            return result_flag


    def add_list(self, board_name, list_names):
        "Add a list for a board"
        result_flag = True
        self.payload = self.auth.copy()
        board_id = self.get_board_id_by_name(board_name)
        for list_name in list_names:
            self.payload['name'] = list_name
            self.payload['idBoard'] = board_id
            url = self.url + "/lists/"
            response = requests.post(url=url, data=self.payload)
            if response.status_code == 200:
                result_flag = True
        return result_flag


    def get_card_id(self, board_name, card_names):
        "Get the card id using board name and card name"
        board_id = self.get_board_id_by_name(board_name)
        card_id = self.get_card_id_by_name(board_id, card_names)
        return card_id

    def get_action_id_name(self, board_name, card_names):
        "Get the card id using board name and card name"
        board_id = self.get_board_id_by_name(board_name)
        card_id = self.get_card_id_by_name(board_id, card_names)
        action_url = self.url + '/cards/' + card_id + '/actions'
        action_details = requests.get(url=action_url, params=self.auth)
        action_details = action_details.json()
        for i in range(len(action_details)):
            if action_details[i]['data']['text'] == action_details[i]['data']['text']:
                action_id = action_details[i]['id']
                break
        return action_id


    def get_list_id(self, board_name, list_names):
        "Get the list id where you are adding the new cards"
        board_id = self.get_board_id_by_name(board_name)
        board_list = self.get_board_list(board_id)
#        reversed(list_names)
        for i in range(len(board_list)):
            if board_list[i]['name'] == list_names[i]:
                board_list_id = board_list[i]['id']

        return board_id, board_list_id


    def get_card_id_by_name(self, board_id, card_name):
        "Get the card id"
        card_id = None
        card_url = self.url + '/boards/' + board_id + '/cards'
        card_details = requests.get(url=card_url, params=self.auth)
        card_details = card_details.json()
        for i in range(len(card_details)):
            if card_details[i]['name'] == card_name[i]:
                card_id = card_details[i]['id']
        return card_id

    def get_board_id_by_name(self, board_name):
        "Get the board id for a board name"
        board_id = None
        self.get_account_details()
        for board in self.boards:
            board_url = self.url + '/boards/' + board
            board_details = requests.get(url=board_url, params=self.auth)
            board_details = board_details.json()
            if board_details['name'] == board_name:
                board_id = board
        return board


    def get_board_list(self, board_id):
        "Get the board id for a board name"
        board_list_url = self.url + '/boards/' + board_id + '/lists'
        board_details = requests.get(url=board_list_url, params=self.auth)
        return board_details.json()

