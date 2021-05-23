import faker
from typing import List, Dict
from numpy import random

def generate(attributes:List[str], number:int) -> Dict:
    fake = faker.Faker()
    return [
        {key: getattr(fake, key)() for key in attributes} for _ in range(number)
    ]