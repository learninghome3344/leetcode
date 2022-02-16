#-*-coding:GBK -*-

def merge_all_problem():
    res = ""
    for i in range(22):
        f = open("leetcode_cn_{i}.md".format(i=i), 'r', encoding='utf-8')
        lines = "".join(f.readlines())
        res += lines
        f.close()
    return res

def gen_id_problem_dict(problems):
    problem_dict = {}
    problems = problems.split("""
## 
```python

```
>
""")
    print(len(problems))
    # for i, p in enumerate(problems[:10]):
    #     print(i, "#"*100)
    #     print(p)
    #     print("\n\n\n")
    for i in range(len(problems)):
        if not problems[i]:
            continue
        s = problems[i].strip()[1:].strip()
        idx = 0
        for j in range(len(s)):
            if not s[j].isdigit():
                idx = j
                break
        # print("s[:idx]: ", s[:idx])
        # print("s: ", s.split("\n"))
        # print("problems[i]", problems[i].split("\n"))
        problem_dict[int(s[:idx])] = problems[i]
    return problem_dict


def gen_markdown(path, content):
    """ 生成 markdown 文件
    """
    file = open(path, 'a', encoding="utf-8")
    markdowncontenct = """{content}
##
```python

```
>
""".format(content=content)
    file.write(markdowncontenct)
    # print(path)
    file.close()


if __name__ == '__main__':
    problems = merge_all_problem()
    problem_dict = gen_id_problem_dict(problems)

    # linked_list
    problem_list = [2,19,21,23,24,25,61,82,83,86,92,109,114,116,117,138,141,143,146,147,148,160,203,206,234,237,328,355,369,379,382,426,430,432,445,460,622,641,705,706,707,708,716,725,817,876,1019,1171,1206,1265,1290,1367,1472,1474,1634,1669,1670,1721,1836,2046,2058,2074,2095,2130]
    # backtrack
    problem_list = [17,22,37,39,40,46,47,51,52,77,78,79,89,90,93,95,113,126,131,140,212,216,254,257,267,282,291,294,301,306,320,351,357,401,411,425,465,473,489,491,494,526,638,679,691,698,784,797,816,842,967,980,996,1066,1079,1087,1088,1096,1215,1219,1238,1239,1240,1255,1258,1286,1307,1415,1467,1593,1601,1655,1718,1723,1774,1799,1820,1849,1863,1947,1980,1986,2002,2014,2044,2048,2056,2065,2151,2152]
    
    
    print(sorted(problem_list) == problem_list)
    for pid in problem_list:
        content = "# " + str(pid)
        if pid in problem_dict:
            content = problem_dict[pid]
        gen_markdown("backtrack.md", content)
