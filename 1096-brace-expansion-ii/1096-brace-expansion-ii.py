class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(s: str) -> set[str]:
            if not s:
                return set()
            if s[0] != '{' and s[0] != ',' and len(s) == 1 or (s[0] != '{' and '{' not in s and ',' not in s):
                return {s}
            
            # Find groups
            stack = 0
            j = 0
            while j < len(s):
                if s[j] == '{': stack += 1
                elif s[j] == '}': stack -= 1
                elif stack == 0 and s[j] == ',':
                    break
                j += 1
            
            if j < len(s):
                # Comma at top level -> Union
                res = set()
                curr = 0
                st = 0
                for i, ch in enumerate(s):
                    if ch == '{': st += 1
                    elif ch == '}': st -= 1
                    elif st == 0 and ch == ',':
                        res |= parse(s[curr:i])
                        curr = i + 1
                res |= parse(s[curr:])
                return res
            
            # Concatenation or nested group
            if s[0] == '{':
                # Find matching closing brace
                st = 0
                end = 0
                for i, ch in enumerate(s):
                    if ch == '{': st += 1
                    elif ch == '}': st -= 1
                    if st == 0:
                        end = i
                        break
                left = parse(s[1:end])
                right = parse(s[end+1:])
                if not right:
                    return left
                return {a + b for a in left for b in right}
            else:
                # Starts with a letter followed by a group or letters
                st = 0
                end = 0
                for i, ch in enumerate(s):
                    if ch == '{':
                        st += 1
                    elif ch == '}':
                        st -= 1
                    elif st == 0 and ch == ',':
                        break
                    elif st == 0 and ch == '{':
                        pass
                    if ch == '{' and st == 1:
                        end = i
                        break
                # If there is a brace block following the prefix
                if '{' in s:
                    # Find first standalone block
                    st = 0
                    idx = 0
                    for i, ch in enumerate(s):
                        if ch == '{':
                            if st == 0:
                                idx = i
                                break
                            st += 1
                        elif ch == '}':
                            st -= 1
                    prefix = s[:idx]
                    # find matching brace for s[idx]
                    st = 0
                    end = idx
                    for i in range(idx, len(s)):
                        if s[i] == '{': st += 1
                        elif s[i] == '}': st -= 1
                        if st == 0:
                            end = i
                            break
                    left = {prefix}
                    mid = parse(s[idx:end+1])
                    right = parse(s[end+1:])
                    res = {a + b for a in left for b in mid}
                    if right:
                        res = {a + b for a in res for b in right}
                    return res
                else:
                    return {s}

        return sorted(list(parse(expression)))