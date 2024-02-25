def look_and_say(n, steps):
    if steps == 0:
        return n
    
    ans = ""
    amount = 1

    for i in range(len(n) - 1):
        if n[i] == n[i + 1]:
            amount += 1

        else:
            ans += f"{amount}{n[i]}"
            amount = 1

    if n[-2] != n[-1]:
        ans += f"1{n[-1]}"

    else:
        ans += f"{amount}{n[-1]}"

    return look_and_say(ans, steps - 1)
    
print(len(look_and_say("1321131112", 40)))
print(len(look_and_say("1321131112", 50)))

