import copy
rules = []

class Term:
    def __init__(self, s):
        s = s.split('(')
        self.pred = s[0]
        self.args = s[1][:-1].split(',')

    def __repr__(self):
        return f'{self.pred}({','.join(self.args)})'

class Rule:
    def __init__(self, s):
        s = s.split(":-")
        self.head = Term(s[0])
        self.goals = []
        if len(s) == 2:
            s = s[1].replace("),", ");").split(";")
            for t in s:
                self.goals.append(Term(t))

class Goal:
    def __init__(self, rule, parent=None, atoms={}):
        self.rule = rule
        self.parent = parent
        self.atoms = copy.deepcopy(atoms)
        self.goalId = 0

def unify(srcTerm, srcAtoms, destTerm, destAtoms):
    if len(srcTerm.args) != len(destTerm.args) or srcTerm.pred != destTerm.pred:
        return False
    for srcKey, destKey in zip(srcTerm.args, destTerm.args):
        srcVal = srcAtoms.get(srcKey) if srcKey.isupper() else srcKey
        destVal = destAtoms.get(destKey) if destKey.isupper() else destKey
        if srcVal:
            if destVal:
                if srcVal != destVal:
                    return False
            else:
                destAtoms[destKey] = srcVal
    return True

def search(term):
    goal = Goal(Rule("j(o)"))
    goal.rule.goals = [term]
    stack = [goal]
    results = []
    while stack:
        item = stack.pop()
        if item.goalId >= len(item.rule.goals):
            if item.parent == None:
                if item.atoms:
                    results.append(item.atoms)
                else:
                    results.append(True)
                continue
            parent = copy.deepcopy(item.parent)
            unify (item.rule.head, item.atoms, parent.rule.goals[parent.goalId], parent.atoms)
            parent.goalId = parent.goalId+1
            stack.append(parent)
            continue

        for rule in rules:
            child = Goal(rule, item)
            if unify (item.rule.goals[item.goalId], item.atoms, child.rule.head, child.atoms):
                stack.append(child)
    print(f'{term}? -> {results}')
    return results

def solve(s):
    s = s.strip()
    if len(s) < 1:
        return None
    if s[-1] == '?':
        search(Term(s[:-1]))
    else:
        rules.append(Rule(s))

def prolog(prompts=None):
    if prompts:
        for s in prompts.split('\n'):
            solve(s)
    else:
        while True:
            solve(input(':'))

if __name__ == '__main__':
    prolog()
