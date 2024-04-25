
class CandidateQuestion:
    def __init__(self,array_question=None):
        self.question_list=array_question

    def get_number_of_question(self):
        return len(self.question_list)
    
    def get_question_from_index(self,index):
        return self.question_list[index]

    @property
    def is_empty_list(self):
        return self.question_list is None