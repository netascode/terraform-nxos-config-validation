class Rule:
    id = "100.001"
    description = "VRF for ethernet interface is not configured under root.vrfs"
    severity = "HIGH"

    @classmethod
    def match(cls, data):
        results = []
        vrfs = [vrf["name"] for vrf in data["vrfs"]]
        key = "interfaces_ethernet"
        try:
            for interface in data[key]:
                if "vrf" in interface:
                    if interface["vrf"] not in vrfs:
                        results.append(f"root.{key}.{interface['id']}.vrf - {interface['vrf']}")
        except KeyError:
            pass

        return results
