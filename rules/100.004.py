class Rule:
    id = "100.004"
    description = "VRF for BGP is not configured under root.vrfs"
    severity = "HIGH"

    @classmethod
    def match(cls, data):
        results = []
        vrfs = [vrf["name"] for vrf in data["vrfs"]]
        try:
            for i, vrf in enumerate(data["bgp"]["vrfs"]):
                if vrf["vrf"] not in vrfs:
                    results.append(f"root.bgp.{i} - {vrf['vrf']}")
        except KeyError:
            pass

        return results
