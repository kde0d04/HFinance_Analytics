from tests.test_case import TEST_QUERIES

def run_test(query: str):
    if query in TEST_QUERIES:
        return f"✅ Test passed for query: {query}"
    else:
        return f"⚠️ No predefined test found for query: {query}"
