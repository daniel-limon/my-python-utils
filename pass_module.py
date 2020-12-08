import random
import string

DEFAULT_LEN = 16
MIN_PASSLEN = 1
MAX_PASSLEN = 512
COMPLEX_COUNT = 2

# error messages
LENGTH_ERROR = "Length is too short to meet complexity requirements."
INVALID_PASSLEN_ERROR = f"Invalid password length. Must be between {MIN_PASSLEN} and {MAX_PASSLEN}"
TYPE_ERROR = 'One or more passed values are of the incorrect type.'


class Pass:

    def __init__(self, pass_len = DEFAULT_LEN, complexity = True, special_chars = True):

        # data validation
        if type(pass_len) != int or type(complexity) != bool or type(special_chars) != bool:
            raise TypeError(TYPE_ERROR)

        if pass_len < MIN_PASSLEN or pass_len > MAX_PASSLEN:
            raise ValueError(INVALID_PASSLEN_ERROR)

        if complexity:
            if special_chars and pass_len < COMPLEX_COUNT * 4:
                raise ValueError(LENGTH_ERROR)
            elif pass_len < COMPLEX_COUNT * 3:
                raise ValueError(LENGTH_ERROR)

        # initializes object if data validation passes
        self.pass_len = pass_len
        self.complexity = complexity
        self.special_chars = special_chars
        self.complex_count = COMPLEX_COUNT


    def get_password(self):
        
        # this list will be used to collect chars for the password
        master_list = []
        
        # if password complexity required, collects min chars from each char category
        if self.complexity:
            master_list.extend(random.choices(string.ascii_lowercase, k = self.complex_count))
            master_list.extend(random.choices(string.ascii_uppercase, k = self.complex_count))
            master_list.extend(random.choices(string.digits, k = self.complex_count))
            if self.special_chars:
                master_list.extend(random.choices(string.punctuation, k = self.complex_count))

        # build master char list
        temp_list = []
        temp_list.extend(list(string.ascii_lowercase))
        temp_list.extend(list(string.ascii_uppercase))
        temp_list.extend(list(string.digits))
        if self.special_chars:
            temp_list.extend(list(string.punctuation))

        # add remaining random characters to master list
        master_list.extend(random.choices(temp_list, k = self.pass_len - len(master_list)))        

        # shuffle chars, join into string and return as string
        random.shuffle(master_list)
        return ''.join(master_list)
