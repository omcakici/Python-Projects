import json, requests

category_data_init = {
    "trivia_categories":[
        {"id":9,"name":"General Knowledge"},
        {"id":10,"name":"Entertainment: Books"},
        {"id":11,"name":"Entertainment: Film"},
        {"id":12,"name":"Entertainment: Music"},
        {"id":13,"name":"Entertainment: Musicals & Theatres"},
        {"id":14,"name":"Entertainment: Television"},
        {"id":15,"name":"Entertainment: Video Games"},
        {"id":16,"name":"Entertainment: Board Games"},
        {"id":17,"name":"Science & Nature"},
        {"id":18,"name":"Science: Computers"},
        {"id":19,"name":"Science: Mathematics"},
        {"id":20,"name":"Mythology"},
        {"id":21,"name":"Sports"},
        {"id":22,"name":"Geography"},
        {"id":23,"name":"History"},
        {"id":24,"name":"Politics"},
        {"id":25,"name":"Art"},
        {"id":26,"name":"Celebrities"},
        {"id":27,"name":"Animals"},
        {"id":28,"name":"Vehicles"},
        {"id":29,"name":"Entertainment: Comics"},
        {"id":30,"name":"Science: Gadgets"},
        {"id":31,"name":"Entertainment: Japanese Anime & Manga"},
        {"id":32,"name":"Entertainment: Cartoon & Animations"}
    ]
}

class ApiCall:
    def __init__(self):
        self.category_data = {}
        self.question_data = {}
        self.category_id = 0
        self.amount = 0
        self.diffuclty = 'easy'

    def get_category_data(self):
        for category in category_data_init["trivia_categories"]:
            print(category["name"], "id:", category["id"])
        print('--------------------------------')
        category_id = input("FROM THE LIST ABOVE SELECT CATEGORY ID: ")
        print('--------------------------------')
        url_category =  f'https://opentdb.com/api_count.php?category={category_id}'
        response_category = requests.get(url_category)
        response_category.raise_for_status() # check for errors

        # Load JSON data into a Python variable.
        category_data = json.loads(response_category.text)
        self.category_id = category_id
        self.category_data = category_data

    def get_question_data(self):
        # First ask user how many questions they want, there is a limit(max=50) questions can be asked for each query
        # Then ask which category they are looking for, find the id of that category inside of that category_data,
        # Then ask the user what would be the diffuctly level for the question
        # For now, only using True/False questions, so that means type should be boolean all the time

        # Call an API
        print('At the below, for selected category it shows how many questions has total and per difficulty level')
        for key, value in self.category_data['category_question_count'].items():
            print(key[6:], '->', value)
        self.difficulty_level = input("Select Difficulty (easy/medium/hard): ")
        self.amount = input("Number of Questions: (max=10 for now)")
        url = f'https://opentdb.com/api.php?amount={self.amount}&category={self.category_id}&difficulty={self.diffuclty}&type=boolean'
        response = requests.get(url)
        response.raise_for_status() # check for errors

        # Load JSON data into a Python variable.
        question_data = json.loads(response.text)
        self.question_data = question_data
    








                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
