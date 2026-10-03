"""
Vizione Labs — Enterprise Automation Platform
Track A: Python Core Fundamentals & Scripting
Lesson 14: Comparative Data Parsing, Logic Flow Integration, Data Structure Lookups
File: main.py

System Purpose:
Enterprise Operational Audit & Metric Parsing Engine.
Parses multi-tenant operational records, evaluates system health indicators,
and outputs structured diagnostic and reporting payloads.
"""

from typing import Dict, List, Any, Tuple


class OperationalDataParser:
    """
    Core parsing engine that validates incoming telemetry records,
    performs nested dictionary lookups, applies logic rules, and generates audit reports.
    """

    def __init__(self, critical_threshold: float, warning_threshold: float) -> None:
        """
        Initializes the parser with system error and warning benchmarks.

        :param critical_threshold: Metric value below which a record triggers CRITICAL status.
        :param warning_threshold: Metric value below which a record triggers WARNING status.
        """
        self.critical_threshold = critical_threshold
        self.warning_threshold = warning_threshold

    def parse_payload(self, records: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Processes raw multi-tenant system logs and categorizes records based on score metrics.

        :param records: List of dictionary records containing node telemetry.
        :return: Structured summary report with metrics and categorized entries.
        """
        categorized_results: Dict[str, List[Dict[str, Any]]] = {
            "CRITICAL": [],
            "WARNING": [],
            "HEALTHY": []
        }

        total_latency_ms = 0.0
        valid_metric_count = 0

        for idx, record in enumerate(records):
            # Nested Data Structure Lookup with Fallbacks
            node_id = record.get("node_id", f"NODE_UNKNOWN_{idx + 1}")
            metrics = record.get("metrics", {})

            # Extract nested parameters safely
            health_score = metrics.get("health_score", 0.0)
            latency = metrics.get("latency_ms", 0.0)

            # Logic Flow Integration: Multi-tier conditional evaluation
            if health_score < self.critical_threshold:
                status = "CRITICAL"
            elif health_score < self.warning_threshold:
                status = "WARNING"
            else:
                status = "HEALTHY"

            parsed_entry = {
                "node_id": node_id,
                "region": record.get("region", "global-default"),
                "health_score": health_score,
                "latency_ms": latency,
                "status": status
            }

            categorized_results[status].append(parsed_entry)

            total_latency_ms += latency
            valid_metric_count += 1

        # Summary calculations
        total_records = len(records)
        avg_latency = (total_latency_ms / valid_metric_count) if valid_metric_count > 0 else 0.0

        return {
            "metadata": {
                "total_nodes_evaluated": total_records,
                "average_latency_ms": round(avg_latency, 2),
                "health_distribution": {
                    "healthy_count": len(categorized_results["HEALTHY"]),
                    "warning_count": len(categorized_results["WARNING"]),
                    "critical_count": len(categorized_results["CRITICAL"])
                }
            },
            "categorized_nodes": categorized_results
        }


def format_audit_report(parsed_data: Dict[str, Any]) -> str:
    """
    Formats the parsed structured data into a human-readable operational report.
    """
    meta = parsed_data["metadata"]
    dist = meta["health_distribution"]
    nodes = parsed_data["categorized_nodes"]

    lines = [
        "==================================================",
        "          VIZIONE LABS OPERATIONAL AUDIT          ",
        "==================================================",
        f"Total Nodes Evaluated : {meta['total_nodes_evaluated']}",
        f"Average System Latency: {meta['average_latency_ms']} ms",
        "--------------------------------------------------",
        "HEALTH DISTRIBUTION:",
        f"  - HEALTHY  : {dist['healthy_count']}",
        f"  - WARNING  : {dist['warning_count']}",
        f"  - CRITICAL : {dist['critical_count']}",
        "==================================================",
        "CRITICAL ALERT INCIDENTS:"
    ]

    if not nodes["CRITICAL"]:
        lines.append("  [NONE] All node systems operating within safe limits.")
    else:
        for node in nodes["CRITICAL"]:
            lines.append(
                f"  ! Node: {node['node_id']} | Region: {node['region']} | "
                f"Score: {node['health_score']} | Latency: {node['latency_ms']}ms"
            )

    lines.append("==================================================")
    return "\n".join(lines)


def main() -> None:
    # Simulated enterprise infrastructure telemetry dataset
    incoming_telemetry = [
        {
            "node_id": "us-east-srv-01",
            "region": "us-east-1",
            "metrics": {"health_score": 98.2, "latency_ms": 14.2}
        },
        {
            "node_id": "eu-central-srv-02",
            "region": "eu-central-1",
            "metrics": {"health_score": 68.5, "latency_ms": 45.1}
        },
        {
            "node_id": "ap-south-srv-03",
            "region": "ap-south-1",
            "metrics": {"health_score": 42.1, "latency_ms": 120.8}
        },
        {
            "node_id": "sa-east-srv-04",
            "region": "sa-east-1",
            "metrics": {"health_score": 88.0, "latency_ms": 22.0}
        },
        {
            "node_id": "us-west-srv-05",
            "region": "us-west-2",
            "metrics": {"health_score": 34.0, "latency_ms": 210.5}
        }
    ]

    # Initialize Parser with defined operational thresholds (Critical < 50, Warning < 75)
    parser = OperationalDataParser(critical_threshold=50.0, warning_threshold=75.0)

    # Process metrics and display report
    parsed_report = parser.parse_payload(incoming_telemetry)
    report_output = format_audit_report(parsed_report)

    print(report_output)


if __name__ == "__main__":
    main()