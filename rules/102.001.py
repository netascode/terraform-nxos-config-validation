class Rule:
    id = "103.001"
    description = "BGP peer template is not configured under root.bgp.template_peers"
    severity = "HIGH"

    @classmethod
    def match(cls, data):
        results = []
        template_peers = []
        try:
            for template_peer in data["bgp"]["template_peers"]:
                template_peers.append(template_peer["name"])
        except KeyError:
            pass

        try:
            for vrf_index, vrf in enumerate(data["bgp"]["vrfs"]):
                try:
                    for neighbor_index, neighbor in enumerate(vrf["neighbors"]):
                        if neighbor["inherit_peer"] not in template_peers:
                            results.append(
                                f"root.bgp.vrfs.{vrf_index}.neighbors.{neighbor_index} - {neighbor['inherit_peer']}"
                            )
                except KeyError:
                    continue
        except KeyError:
            pass

        return results
