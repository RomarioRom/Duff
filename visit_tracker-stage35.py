# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: VisitTracker
def suggest_next_action(current_state: dict, recent_visits: list) -> dict:
    """Recommend the next action based on current state and recent visit history.

    Args:
        current_state: Dict with keys like 'total_visits', 'last_visit_date',
                       'pending_goals', 'last_goal', 'last_place', 'last_contact',
                       'last_note', 'visit_frequency', 'last_goal_achieved'.
        recent_visits: List of recent visit dicts with keys like 'date', 'place',
                       'goal', 'contact', 'note', 'status'.

    Returns:
        Dict with keys 'action', 'reason', 'priority' describing the next step.
    """
    priority = "low"
    reason = "No pending items. Consider scheduling a follow-up or planning a new visit."
    action = "Review recent visits and plan the next action."

    if current_state.get("pending_goals"):
        pending_count = len(current_state["pending_goals"])
        if pending_count > 0:
            priority = "high"
            reason = f"You have {pending_count} pending goals. Prioritize completing or scheduling them."
            action = "Work on pending goals."

    if recent_visits and current_state.get("last_goal"):
        last_goal = current_state["last_goal"]
        last_visit = recent_visits[-1] if recent_visits else None
        if last_visit and last_visit.get("goal") == last_goal:
            if last_visit.get("status") in ("pending", "scheduled"):
                priority = "high"
                reason = "Your last visit goal is still pending. Schedule a follow-up."
                action = "Schedule a follow-up for the last visit goal."
            elif last_visit.get("status") == "completed":
                if not current_state.get("last_goal_achieved"):
                    priority = "medium"
                    reason = "Last goal was completed. Mark it achieved and consider next steps."
                    action = "Mark last goal as achieved and plan next visit."

    if current_state.get("visit_frequency", 0) > 0 and not current_state.get("last_visit_date"):
        priority = "medium"
        reason = "You have visits recorded but no last visit date. Update your records."
        action = "Update the last visit date in your tracker."

    if recent_visits and len(recent_visits) >= 3:
        priority = "medium"
        reason = "You've made several visits. Consider reviewing trends and insights."
        action = "Review visit trends and insights."

    return {"action": action, "reason": reason, "priority": priority}
