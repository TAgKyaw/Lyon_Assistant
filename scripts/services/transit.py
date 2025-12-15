def get_transit_summary(commute):
    # TODO: Replace with real TFL API integration
    return {
        "status": "delayed",
        "lines": commute["lines"],
        "reason": "minor delays reported on the Northern line"
    }
