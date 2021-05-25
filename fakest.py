import faker
from typing import List, Dict, Optional
from numpy import random

NUM_GENERATORS = {
    "gauss": lambda x,y: random.normal(float(x), float(y)),
    "normal": lambda x,y: random.normal(float(x), float(y)),
}


def _get_params(param: str) -> Optional[List[str]]:
    params = param.split("@")
    if len(params) < 2: return None
    else: return params[1].split(",")

def _get_distribution(param: str) -> str:
    return param.split("@")[0]

def _get_generator(distribution: str):
    return NUM_GENERATORS[distribution]
    

def get_number(attribute: str):
    generator = _get_generator(_get_distribution(attribute))
    return generator(*_get_params(attribute))

def generate(attributes:List[str], number:int) -> Dict:
    fake = faker.Faker()
    numerical = [a for a in attributes if _get_distribution(a) not in dir(fake)]
    faker_attribures = [a for a in attributes if _get_distribution(a) in dir(fake)]
    faker_data = [{key: getattr(fake, key)() for key in faker_attribures} for _ in range(number)]
    numerical_data = [{f"value_{i}": get_number(attribute) for i,attribute in enumerate(numerical)} for _ in range(number)]
    return [{**fake, **num} for fake, num in zip(faker_data, numerical_data)]

