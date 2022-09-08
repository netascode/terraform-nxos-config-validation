class Rule:
    id = "101.001"
    description = "Feature BGP is not enabled, but BGP configuraion is present."
    severity = "HIGH"

    @classmethod
    def match(cls, data):
        results = []
        feature_enabled = False
        try:
            feature_enabled = "bgp" in data["features"]
        except KeyError:
            pass

        if "bgp" in data and not feature_enabled:
            results.append(f"add `bgp` to root.features")

        return results
