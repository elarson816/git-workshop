"""Select a random project trunk form maintainer and randomly assign 6 tasks!
"""
from random import randrange
# from collections import OrderedDict


participants = \
    ['Beth', 'Julien', 'Linnea', 'Sally', 'Shulin', 'Suzanne', 'Varsha']
project_trunk_maintainer = '?'
issueoffset = 1
assignments = {}
announcement = 'The project maintainer is {}!\n\n' \
               'Assignments are as follows: \n{}'


def select_trunk_maintainer(workshop_participants):
    """Randomly select project trunk maintainer."""
    random_num = randrange(len(workshop_participants))
    return workshop_participants.pop(random_num), workshop_participants


def assign_tasks(workshop_participants, issue_assignments={}, i=1+issueoffset):
    """Randomly assign tasks."""
    if workshop_participants:
        random_num = randrange(len(workshop_participants))
        issue_assignments[i] = workshop_participants.pop(random_num)
        i += 1
        assign_tasks(workshop_participants=workshop_participants,
                     issue_assignments=issue_assignments,
                     i=i)
    return issue_assignments


if __name__ == '__main__':
    # try:
    project_trunk_maintainer, participants = \
        select_trunk_maintainer(participants)
    assignments = assign_tasks(participants)
    # announcement = announcement\
    #     .format(project_trunk_maintainer,
    #             str('{}: {}'.format(k, v) for k, v in assignments.items()))
    announcement = announcement.format(project_trunk_maintainer, assignments)
    print(announcement)
    # except KeyError:
    #     # from pdb import set_trace; set_trace()
    #     pass
