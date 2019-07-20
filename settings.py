from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
       'name': 'public_goods',
       'display_name': "Public Goods",
       'num_demo_participants': 16,
       'app_sequence': ['myfirstapp'],
       'real_world_currency_per_point': 0.5
    },
     {
       'name': 'public_goods0',
       'display_name': "Public Goods0",
       'num_demo_participants': 4,
       'app_sequence': ['myfirstapp'],
       'experimental_group': 0,
       'real_world_currency_per_point': 0.5
    },
     {
       'name': 'public_goods1',
       'display_name': "Public Goods1",
       'num_demo_participants': 4,
       'app_sequence': ['myfirstapp'],
       'experimental_group': 1,
       'real_world_currency_per_point': 0.5
    },
     {
       'name': 'public_goods2',
       'display_name': "Public Goods2",
       'num_demo_participants': 4,
       'app_sequence': ['myfirstapp'],
       'experimental_group': 2,
       'real_world_currency_per_point': 0.5
    },
     {
       'name': 'public_goods3',
       'display_name': "Public Goods3",
       'num_demo_participants': 4,
       'app_sequence': ['myfirstapp'],
       'experimental_group': 3,
       'real_world_currency_per_point': 0.5
    },
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ru'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'RUR'
USE_POINTS = True

ROOMS = [{'name':'myroom','display_name':'`my new room'}]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = '123'#environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'e*)_3_*gpf8!qu3li=r1=^n4(it^jc@28*tpgdrr-4^hk%dpww'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
