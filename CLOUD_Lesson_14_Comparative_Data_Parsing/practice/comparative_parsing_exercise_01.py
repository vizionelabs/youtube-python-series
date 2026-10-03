"""
Vizione Labs — Track A: Python Core Fundamentals & Scripting
Lesson 14: Comparative Data Parsing, Logic Flow Integration, Data Structure Lookups
File: practice/comparative_parsing_exercise_01.py

Purpose:
A foundational practice script demonstrating how to iterate over raw, multi-format
data payloads, compare key-value pairs against operational thresholds, perform
nested dictionary lookups, and construct structured metric summaries.
"""


def parse_and_compare_records(data_payload: list[dict], metric_key: str, threshold: float) -> dict:
    """
    Parses a list of record dictionaries, compares a target numerical metric against a threshold,
    and categorizes items into passed and flagged datasets.

    :param data_payload: List of dictionaries representing incoming raw records.
    :param metric_key: The string key inside each record to evaluate.
    :param threshold: Numerical benchmark for comparative filtering.
    :return: Dictionary containing structured breakdown and summary counts.
    """
    passed_records = []
    flagged_records = []

    for index, record in enumerate(data_payload):
        # Data structure lookup with direct key retrieval
        record_id = record.get("id", f"UNKNOWN_{index}")
        metric_value = record.get(metric_key, 0.0)

        # Logic Flow Integration: Conditional branching based on comparative evaluation
        if metric_value >= threshold:
            passed_records.append({
                "id": record_id,
                "value": metric_value,
                "status": "PASS"
            })
        else:
            flagged_records.append({
                "id": record_id,
                "value": metric_value,
                "status": "FLAGGED_BELOW_THRESHOLD"
            })

    # Summary metric aggregation
    total_processed = len(data_payload)
    pass_rate = (len(passed_records) / total_processed * 100) if total_processed > 0 else 0.0

    return {
        "summary": {
            "total_records": total_processed,
            "passed_count": len(passed_records),
            "flagged_count": len(flagged_records),
            "pass_rate_percentage": round(pass_rate, 2)
        },
        "passed": passed_records,
        "flagged": flagged_records
    }


def main() -> None:
    # Raw sample payload: Simulated operational metrics list
    raw_payload = [
        {"id": "REC_101", "score": 88.5, "tag": "batch_a"},
        {"id": "REC_102", "score": 62.0, "tag": "batch_a"},
        {"id": "REC_103", "score": 94.2, "tag": "batch_b"},
        {"id": "REC_104", "score": 45.8, "tag": "batch_b"},
        {"id": "REC_105", "score": 79.1, "tag": "batch_c"},
    ]

    target_metric = "score"
    benchmark_threshold = 75.0

    print("=== VIZIONE LABS: COMPARATIVE DATA PARSER ===")
    print(f"Evaluating metric '{target_metric}' against threshold: {benchmark_threshold}\n")

    # Execute parsing algorithm
    result = parse_and_compare_records(raw_payload, target_metric, benchmark_threshold)

    # Output structured parsed results
    print("--- PARSING SUMMARY ---")
    print(f"Total Records Processed : {result['summary']['total_records']}")
    print(f"Passed Threshold        : {result['summary']['passed_count']}")
    print(f"Flagged Below Threshold : {result['summary']['flagged_count']}")
    print(f"Pass Rate               : {result['summary']['pass_rate_percentage']}%\n")

    print("--- FLAGGED RECORDS FOR AUDIT ---")
    for item in result["flagged"]:
        print(f"ID: {item['id']} | Value: {item['value']} | Status: {item['status']}")


if __name__ == "__main__":
    main()