import json
import urllib.request
import urllib.parse
import ssl


def get_country_info(country_name: str) -> dict:
    """
    Retrieves basic information about a country using the Rest Countries API.
    Args:
        country_name: Name of the country (e.g., "France", "Japan").
    Returns:
        A dictionary with status and selected fields such as capital, region, population, and flag URL.
    """
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        encoded = urllib.parse.quote(country_name.strip())
        url = f"https://restcountries.com/v3.1/name/{encoded}?fullText=true"
        req = urllib.request.Request(url, headers={'User-Agent': 'SchoolMultiAgent/1.0'})
        with urllib.request.urlopen(req, context=ctx) as response:
            data = json.loads(response.read().decode('utf-8'))
            if not data:
                return {"status": "error", "message": f"No data found for '{country_name}'."}
            info = data[0]
            result = {
                "status": "success",
                "name": info.get("name", {}).get("common"),
                "official_name": info.get("name", {}).get("official"),
                "capital": info.get("capital", [None])[0],
                "region": info.get("region"),
                "subregion": info.get("subregion"),
                "population": info.get("population"),
                "area_km2": info.get("area"),
                "primary_language": next(iter(info.get("languages", {}).values()), None),
                "flag_svg": info.get("flags", {}).get("svg")
            }
            return result
    except Exception as e:
        return {"status": "error", "message": f"Could not fetch country info: {str(e)}"}


def get_geography_trivia(difficulty: str = "medium") -> dict:
    """
    Retrieves a single geography trivia question from the Open Trivia Database.
    Args:
        difficulty: One of "easy", "medium", or "hard".
    Returns:
        A dictionary with the question, correct answer and list of incorrect answers.
    """
    try:
        difficulty = difficulty.lower()
        if difficulty not in {"easy", "medium", "hard"}:
            difficulty = "medium"
        url = f"https://opentdb.com/api.php?amount=1&category=22&difficulty={difficulty}&type=multiple"
        req = urllib.request.Request(url, headers={'User-Agent': 'SchoolMultiAgent/1.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            if data.get("response_code") != 0:
                return {"status": "error", "message": "No trivia question returned."}
            q = data["results"][0]
            return {
                "status": "success",
                "question": q.get("question"),
                "correct_answer": q.get("correct_answer"),
                "incorrect_answers": q.get("incorrect_answers", []),
                "category": q.get("category"),
                "difficulty": q.get("difficulty")
            }
    except Exception as e:
        return {"status": "error", "message": f"Could not fetch trivia: {str(e)}"}
