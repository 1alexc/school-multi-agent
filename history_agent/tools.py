import datetime
import urllib.request
import urllib.parse
import json

def get_now() -> dict:
    """
    Returns the current date and time. Use this to determine relative dates when the user asks about 'today', 'recently', or 'this year'.
    """
    now = datetime.datetime.now()
    return {
        "status": "success",
        "current_date": now.strftime("%Y-%m-%d"),
        "current_time": now.strftime("%H:%M:%S"),
        "current_year": now.year
    }

def wikipedia_summary(query: str) -> dict:
    """
    Fetches a factual summary of a historical event, figure, or topic from Wikipedia.
    Use this to ensure accuracy regarding dates and details of historical events.
    
    Args:
        query: The topic to search for (e.g., "World War II", "Julius Caesar").
        
    Returns:
        A dictionary containing the title, summary extract, and URL of the Wikipedia page.
    """
    try:
        import ssl
        
        # Bypass SSL verification which frequently fails on macOS Python installations
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        
        # Format the query for the Wikipedia REST API
        formatted_query = urllib.parse.quote(query.replace(" ", "_"))
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{formatted_query}"
        
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'SchoolMultiAgent/1.0 (Student Project)'}
        )
        
        with urllib.request.urlopen(req, context=ctx) as response:
            data = json.loads(response.read().decode('utf-8'))
            return {
                "status": "success",
                "title": data.get("title"),
                "summary": data.get("extract"),
                "url": data.get("content_urls", {}).get("desktop", {}).get("page")
            }
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return {"status": "error", "message": f"No exact Wikipedia match found for '{query}'. Try a more specific or different search term."}
        return {"status": "error", "message": f"Wikipedia API error: {e.code}"}
    except Exception as e:
        return {"status": "error", "message": f"Could not fetch Wikipedia summary. Error: {str(e)}."}
