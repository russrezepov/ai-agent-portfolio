def execute(plan):
    actions = []
    if "notify" in plan.lower():
        actions.append("Notify CSM")
    if "follow-up" in plan.lower():
        actions.append("Create follow-up task")
    return actions
