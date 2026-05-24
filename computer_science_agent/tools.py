def explain_algorithm(algorithm_name: str) -> dict:
    """
    Provides a concise explanation of a common computer science algorithm.
    """
    algo = algorithm_name.lower().strip()
    descriptions = {
        "binary search": {
            "description": "Searches a sorted list by repeatedly dividing the search interval in half.",
            "use_cases": ["Finding an item in a sorted array", "Lookup tables"]
        },
        "quick sort": {
            "description": "A divide‑and‑conquer sorting algorithm that picks a pivot and partitions the array.",
            "use_cases": ["General‑purpose sorting", "In‑memory array ordering"]
        },
        "dijkstra": {
            "description": "Finds the shortest path from a source node to all other nodes in a weighted graph.",
            "use_cases": ["Routing", "Network latency minimisation"]
        }
    }
    if algo in descriptions:
        return {"status": "success", "algorithm": algorithm_name, **descriptions[algo]}
    return {"status": "error", "message": f"No description available for '{algorithm_name}'."}


def fetch_programming_question(topic: str) -> dict:
    """Fetch a recent programming question from StackExchange API related to *topic*.
    This acts as a real MCP‑style tool (uses external HTTP request).
    """
    import json, urllib.request, urllib.parse, ssl
    # Build query URL – use StackOverflow site, filter by tag (topic) if possible
    tag = urllib.parse.quote(topic.lower())
    url = f"https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&tagged={tag}&site=stackoverflow&filter=!9_bDDxJY5"
    # Disable SSL verification as before (macOS issue)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, headers={"User-Agent": "SchoolMultiAgent/1.0"})
    try:
        with urllib.request.urlopen(req, context=ctx) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            items = data.get('items', [])
            if not items:
                return {"status": "error", "message": f"No recent StackOverflow questions found for tag '{topic}'."}
            # Return first item's title and link
            first = items[0]
            return {
                "status": "success",
                "question": first.get('title'),
                "link": first.get('link'),
                "topic": topic
            }
    except Exception as e:
        return {"status": "error", "message": f"Failed to fetch StackOverflow data: {str(e)}"}
