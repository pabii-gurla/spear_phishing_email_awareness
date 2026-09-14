def spear_phish_template(target):
    return f"""
From : it-support@{target['company'].lower()}.com
To : {target['email']}
Subject : Action Required: Your {target['company']} account will be disabled

Hi {target['name']},

Our security team noticed a login from {target['location']}.
Please verify your account within 24 hours to avoid suspension. 

[Verify Account] -> https://lab.internal/awareness-test 

Regards
IT Ssecurity Team
"""

targets = [
    {
    "name": "Riya Sharman",
    "email": "riya@company.com",
    "company": "Sqrock",
    "location" : "Banglore, India"
},
{
    "name" : "Didintle Mosweu",
    "email" : "didimos12@company.com",
    "company" : "Sqrock",
    "location" : "capetown"
},
{
    "name" : "Charissa Smith",
    "email" : "charismith@company.com",
    "company" : "Sqrock",
    "location" : "Lagos, Nigeria"
}
]

for target in targets:
    print(spear_phish_template(target))
