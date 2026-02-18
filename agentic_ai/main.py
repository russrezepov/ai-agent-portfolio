from agents.risk_agent import analyze
from agents.planner_agent import plan
from agents.executor_agent import execute
from tools.slack import send_slack
from tools.email import send_email
from memory.memory import save_memory
from logs.logger import log
from drift.drift_sim import simulate_drift

customers = [
    {"tenant": "Acme", "risk_score": 0.82, "usage_trend": "down", "open_tickets": 4},
    {"tenant": "BetaCorp", "risk_score": 0.65, "usage_trend": "flat", "open_tickets": 2},
]

for customer in customers:
    customer = simulate_drift(customer)
    analysis = analyze(customer)
    log(f"Risk analyzed for {customer['tenant']}")
    plan_out = plan(analysis)
    log(f"Plan created for {customer['tenant']}")
    actions = execute(plan_out)

    for action in actions:
        if "Notify" in action:
            send_slack(f"High risk customer: {customer['tenant']}")
            send_email(f"Customer Risk Alert - {customer['tenant']}", f"{customer}\n\n{analysis}")
            log("Human notified")

    save_memory({"customer": customer["tenant"], "analysis": analysis, "actions": actions}, tenant=customer["tenant"])

print("Multi-agent run complete with drift simulation and multi-tenant memory.")
