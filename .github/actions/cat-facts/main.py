import requests, random, sys

cat_url = "https://cat-fact.herokuapp.com/facts"
r = requests.get(cat_url)
r_obj_list = r.json()

r_obj = random.choice(r_obj_list)

print(r_obj['text'])
print(f"::set-output name=fact::{r_obj['text']}")
