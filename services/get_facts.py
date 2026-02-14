import random
from utilits.facts_en import facts_en
from utilits.facts_ua import facts_ua

def get_facts_en():
    category=random.choice(list(facts_en))
    return 'Category:',category, 'Fact:', facts_en[category]

def get_facts_ua():
    category=random.choice(list(facts_ua))
    return 'Категорія:',category, 'Факт', facts_ua[category]