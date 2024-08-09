role_permissions = {
    'CEO': {
        'Users': ['create', 'read', 'update', 'delete'],
        'Events': ['create', 'read', 'update', 'delete'],
        'Leaves Count': ['create', 'read', 'update', 'delete'],
        'Leaves Approve': [],
        'Lunch Menu': ['read'],
        'Projects': ['create', 'read', 'update', 'delete'],
        'Feedback': ['read']
    },
    'CTO': {
        'Users': ['create', 'read', 'update', 'delete'],
        'Events': ['create', 'read', 'update', 'delete'],
        'Leaves Count': ['create', 'read', 'update', 'delete'],
        'Leaves Approve': [],
        'Lunch Menu': ['read'],
        'Projects': ['create', 'read', 'update', 'delete'],
        'Feedback': ['read']
    },
    'S-HR': {
        'Users': ['create', 'read', 'update', 'delete'],
        'Events': ['create', 'read', 'update', 'delete'],
        'Leaves Count': ['create', 'read', 'update', 'delete'],
        'Leaves Approve': ['approve'],
        'Lunch Menu': ['create', 'read', 'update', 'delete'],
        'Projects': ['create', 'read', 'update'],
        'Feedback': ['create', 'read', 'update']
    },
    'J-HR': {
        'Users': ['create', 'read', 'update'],
        'Events': ['create', 'read', 'update'],
        'Leaves Count': ['read'],
        'Leaves Approve': ['approve'],
        'Lunch Menu': ['create', 'read', 'update', 'delete'],
        'Projects': ['create', 'read', 'update'],
        'Feedback': ['create', 'read', 'update']
    },
    'Project Manager': {
        'Users': ['read', 'update'],
        'Events': ['read'],
        'Leaves Count': ['read'],
        'Leaves Approve': [],
        'Lunch Menu': ['read'],
        'Projects': ['read', 'update'],
        'Feedback': ['read']
    },
    'Team Lead': {
        'Users': ['read'],
        'Events': ['read'],
        'Leaves Count': ['read'],
        'Leaves Approve': [],
        'Lunch Menu': ['read'],
        'Projects': ['read'],
        'Feedback': ['read']
    },
    'Employee': {
        'Users': ['read'],
        'Events': ['read'],
        'Leaves Count': ['read'],
        'Leaves Approve': [],
        'Lunch Menu': ['read'],
        'Projects': ['read'],
        'Feedback': ['read']
    }
}

HTTP_METHOD_POST = 'POST'