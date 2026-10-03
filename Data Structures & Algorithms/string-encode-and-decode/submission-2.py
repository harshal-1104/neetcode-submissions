class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        lengths = [str(len(s)) for s in strs]
        header = ",".join(lengths)
        payload = "".join(strs)

        return header + "#" + payload

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        header_end = s.find("#")
        header = s[:header_end]

        lengths = [int(length) for length in header.split(",")]
        payload = s[header_end+1:]

        ans = []
        pointer = 0

        for length in lengths:
            word = payload[pointer:pointer+length]
            ans.append(word)
            pointer+=length

        return ans