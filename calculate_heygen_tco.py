#!/usr/bin/env python3
"""
HeyGen vs Synthesia AI Avatar Video Generation TCO Calculator (2026)
Calculates unit economics, credits per video minute, and annual enterprise ROI.
"""

def calculate_heygen_tco(video_minutes_per_month: int, plan_type: str = "creator"):
    plans = {
        "creator": {"base_price": 29.0, "credits_included": 15, "extra_minute_rate": 2.0},
        "team": {"base_price": 89.0, "credits_included": 30, "extra_minute_rate": 1.8},
        "pro": {"base_price": 199.0, "credits_included": 100, "extra_minute_rate": 1.5}
    }
    
    selected = plans.get(plan_type.lower(), plans["creator"])
    base = selected["base_price"]
    inc = selected["credits_included"]
    rate = selected["extra_minute_rate"]
    
    extra_minutes = max(0, video_minutes_per_month - inc)
    monthly_total = base + (extra_minutes * rate)
    cost_per_minute = monthly_total / max(1, video_minutes_per_month)
    
    return {
        "plan": plan_type,
        "video_minutes": video_minutes_per_month,
        "base_cost": base,
        "overage_cost": extra_minutes * rate,
        "monthly_total": monthly_total,
        "cost_per_minute": round(cost_per_minute, 2),
        "annual_total": round(monthly_total * 12, 2)
    }

if __name__ == "__main__":
    import sys
    minutes = int(sys.argv[1]) if len(sys.argv) > 1 else 45
    plan = sys.argv[2] if len(sys.argv) > 2 else "team"
    res = calculate_heygen_tco(minutes, plan)
    print(f"[*] HeyGen AI Video TCO Analysis ({res['plan'].upper()} Plan):")
    print(f"    Total Video Minutes: {res['video_minutes']} min/mo")
    print(f"    Base Subscription:   ${res['base_cost']}/mo")
    print(f"    Overage Fees:        ${res['overage_cost']:.2f}/mo")
    print(f"    Monthly Net TCO:     ${res['monthly_total']:.2f}")
    print(f"    Unit Cost/Minute:    ${res['cost_per_minute']:.2f}/min")
    print(f"    Annual Run-Rate:     ${res['annual_total']:.2f}/yr")
