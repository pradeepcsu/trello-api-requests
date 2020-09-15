import sys
import requests

class Trello_Obj:

      def number_of_cards_in_list(self):
            # url = "https://api.trello.com/1/lists/{list_id}/cards"
            url = "https://api.trello.com/1/lists/5f6023fe56e9112ad6226787/cards"

            query = {
               'key': '62e208412de52ff355e3f55dec33940f',
               'token': '1aaac0fc3a463f39bf5352960a4aaa65c163821d23c0c816287093884aa42cd8'
            }
            cards_list =[]
            try:
               response = requests.request("GET", url, params=query)
               response = response.json()
               for i in range(len(response)):
                     # cards_list.append(response[i]["name"])
                     cards_list.append(response[i]["badges"]["comments"])
                     print("card " + str(i + 1) + " name is :" + response[i]["name"])
            except Exception as e:
               print(str(e))
            print("Total cards on the list is: " + str(len(cards_list)))
            return str(len(cards_list))


      # Verify that there is a card with comment
      def number_of_cards_with_more_than_one_comment(self):
            # url = "https://api.trello.com/1/lists/{list_id}/cards"
            url = "https://api.trello.com/1/lists/5f6023fe56e9112ad6226787/cards"

            query = {
               'key': '62e208412de52ff355e3f55dec33940f',
               'token': '1aaac0fc3a463f39bf5352960a4aaa65c163821d23c0c816287093884aa42cd8'
            }
            cards_with_comments = 0
            try:
               response = requests.request("GET", url, params=query)
               response = response.json()
               for i in range(len(response)):
                  # cards_list.append(response[i]["name"])
                  if response[i]["badges"]["comments"] > 0:
                     cards_with_comments += 1
                  print("Number of comments on card " + str(i + 1) + " is :" + str(response[i]["badges"]["comments"]))
            except Exception as e:
               print(str(e))
            return cards_with_comments

     # Move the card to DONE
      def move_card_to_done(self):
            # url = "https://api.trello.com/1/cards/{card_id}/idlist?value={destination_list_id}"
            url = "https://api.trello.com/1/cards/5f60240dd3ed3c6168b83fae/idlist=5f5c53ed07f06d7aafdceae2"

            query = {
               'key': '62e208412de52ff355e3f55dec33940f',
               'token': '1aaac0fc3a463f39bf5352960a4aaa65c163821d23c0c816287093884aa42cd8'
            }
            response = requests.request("PUT", url, params=query)
            response = response.json()

            if response.status_code == 200:
               result_flag = True

            return result_flag



def main():
   test_obj = Trello_Obj()

   # validating there are only 2 cards on the list
   cards_count = test_obj.number_of_cards_in_list()
   assert len(cards_count) == 2

   # validating there are one card with more than 1 comment
   cards_with_comments = test_obj.number_of_cards_with_more_than_one_comment()
   print("cards with more than 1 comment are " + str(cards_with_comments))

   # move card to done
   card_moved = test_obj.move_card_to_done()
   assert card_moved

   return 0

if __name__ == '__main__':
   sys.exit(main())
