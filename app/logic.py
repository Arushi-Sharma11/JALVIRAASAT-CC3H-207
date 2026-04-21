import datetime

class FinanceEngine:
    @staticmethod
    def calculate_fbs(user, amount, category):
        # Feature 1, 5, 7: Adaptive FBS + Context + Farmer Support
        score = user.fbs_score
        weights = {"Productive": 20, "Essential": 5, "Waste": -30}
        impact = weights.get(category, 0)

        # Feature 7: Farmer Seasonal Logic
        if user.role == "farmer":
            month = datetime.datetime.now().month
            if month in [6, 7, 10, 11]: # Sowing/Harvesting Season
                impact = impact * 0.4 if impact < 0 else impact # Kam penalty
        
        return max(0, min(1000, score + impact))

    @staticmethod
    def get_smart_nudge(amount, user):
        # Feature 2 & 6: Prediction & Smart Nudging
        if amount > (user.savings_goal * 0.2):
            return {
                "type": "WARNING",
                "message": "Ye spend aapke goal ko delay kar sakta hai. 2 din wait karein toh 10 bonus points milenge!",
                "prediction": "Goal delayed by approx 10 days"
            }
        return {"type": "SAFE", "message": "Good decision! Budget ke andar hai."}

    @staticmethod
    def get_gamified_scenario(category):
        # Feature 4: Gamified Correction Loop
        if category == "Waste":
            return "CHALLENGE: Aapne waste spend kiya! Kya aap agle 3 din zero spending kar ke points wapas pana chahte hain? [Yes/No]"
        return None