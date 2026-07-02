from __future__ import annotations

from copy import deepcopy
from typing import Any

from .crawler_agent import run_crawler_agent
from .devtools_agent import run_devtools_agent
from .discovery_agent import discovery_endpoint_rows, run_discovery_agent
from .report_agent import run_report_agent
from .sqli_agent import run_sqli_agent
from .technology_agent import run_technology_agent


def run_orchestrator(
    target: str,
    domain_data: dict[str, Any] | None = None,
    config: dict[str, Any] | None = None,
) -> dict[str, Any]:
    domain_data = deepcopy(domain_data or {})
    config = config or {}
    steps = []

    crawler = run_crawler_agent(domain_data)
    steps.append(_step("crawler_agent", crawler.get("summary") or {}))

    devtools = run_devtools_agent(domain_data)
    steps.append(_step("devtools_agent", devtools.get("summary") or {}))

    technology = run_technology_agent(domain_data)
    steps.append(_step("technology_agent", technology.get("summary") or {}))

    discovery = run_discovery_agent(target, domain_data, config=config.get("discovery"))
    steps.append(_step("discovery_agent", discovery.get("summary") or {}))

    discovery_endpoints = discovery_endpoint_rows(discovery)
    domain_data["api_endpoints"] = _merge_endpoint_rows(domain_data.get("api_endpoints") or [], discovery_endpoints)
    domain_data["discovery"] = discovery

    sqli = run_sqli_agent(target, domain_data, discovery, config=config.get("sqli"))
    domain_data["sqli_analysis"] = sqli
    steps.append(_step("sqli_analysis_agent", sqli.get("summary") or {}))

    report = run_report_agent(domain_data)
    steps.append(_step("report_agent", report.get("summary") or {}))

    return {
        "agent": {"name": "orchestrator", "role": "local Pamp agent workflow"},
        "target": target,
        "steps": steps,
        "crawler": crawler,
        "devtools": devtools,
        "technology": technology,
        "discovery": discovery,
        "discovery_endpoints": discovery_endpoints,
        "sqli_analysis": sqli,
        "report": report,
        "domain_updates": {
            "api_endpoints": domain_data.get("api_endpoints") or [],
            "discovery": discovery,
            "sqli_analysis": sqli,
            "agent_workflow": steps,
        },
    }


def _step(agent: str, summary: dict[str, Any]) -> dict[str, Any]:
    return {"agent": agent, "status": "done", "summary": summary}


def _merge_endpoint_rows(existing: list[dict[str, Any]], new_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged = []
    seen = set()
    for row in list(existing or []) + list(new_rows or []):
        endpoint = str(row.get("endpoint") or "")
        method = str(row.get("method") or "")
        if not endpoint:
            continue
        key = f"{method}|{endpoint}"
        if key in seen:
            continue
        seen.add(key)
        merged.append(row)
    return merged[:350]
