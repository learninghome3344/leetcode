# -*- coding: utf-8 -*-
import os
import json
import sys


def parse_problem(s):
    s = s[:-3] # remove ".py"
    if "." in s:
        pid, name = s.split(".")
    else:
        i = 0
        while s[i].isdigit():
            i += 1
        pid, name = s[:i], s[i:]
    return pid, name

def del_prefix_num(s):
    i = 0
    while s[i].isdigit():
        i += 1
    return s[i:]


# print(parse_problem("6字符串转换整数(atoi).py"))
# sys.exit(0)

def mapping2printstr(mapping, prefix, level):
    sub_level = level + 1
    sub_prefix = prefix * sub_level

    sub_items = []
    for key, value in mapping.items():
        sub_item = sub_prefix + key + ": "
        # 仅在value为字典时才会递归调用
        if isinstance(value, dict):  # 可以看做是在模拟d0中的b1
            # 进入下一字典层级中
            sub_item += "{\n"
            sub_item += mapping2printstr(value, prefix, sub_level)  # 递归调用的部分实际上可以看做是在模拟b1中的a2
            sub_item += "\n" + sub_prefix + "}"
        else:
            # 对于非字典项，直接转化为字符串
            sub_item += str(value)[:5]  # 模拟d0中的a1
        sub_items.append(sub_item)
    # 使用'\n'连接a1、b1、c1
    sub_items = "\n".join(sub_items)
    return sub_items


def merge_all_problem():
    res = ""
    path = "/Users/bingjian.yan/recent_learning/algorithm_learning/leetcode/markdown_files/spider"
    for i in range(22):
        file = os.path.join(path, "leetcode_cn_all_problems/leetcode_cn_{i}.md".format(i=i))
        f = open(file, 'r', encoding='utf-8')
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
    root = os.getcwd()
    g = os.walk(os.path.join(root, "../fishredleaf_code/leetcode"))
    path_dict = {}
    paths = []
    for path, dir_list, file_list in g:
        for file_name in file_list:
            problem_path = os.path.join(path, file_name)
            paths.append((file_name, problem_path))
            # print(file_name)
            # print(problem_path)


    res = {} # {"分组刷题": {"9字典树": [677, 键值映射]}}
    for file_name, path in paths:
        pid, title = parse_problem(file_name)
        idx = path.index("leetcode")
        relative_path = path[idx+9:]
        tags = relative_path.split("/")[:-1]
        for i in range(len(tags)):
            if len(tags) == 2:
                if i == 0:
                    res[tags[0]] = res.get(tags[0], {})
                if i == 1:
                    res[tags[0]][tags[1]] = res[tags[0]].get(tags[1], [])
            if len(tags) == 3:
                if i == 0:
                    res[tags[0]] = res.get(tags[0], {})
                if i == 1:
                    res[tags[0]][tags[1]] = res[tags[0]].get(tags[1], {})
                if i == 2:
                    res[tags[0]][tags[1]][tags[2]] = res[tags[0]][tags[1]].get(tags[2], [])
        pid = int(pid) if pid else 0
        if len(tags) == 2:
            res[tags[0]][tags[1]].append((pid, title, path))
        if len(tags) == 3:
            res[tags[0]][tags[1]][tags[2]].append((pid, title, path))

    # print(mapping2printstr(res, "  ", 0))
    # sys.exit(0)

    all_problems = merge_all_problem()
    problem_dict = gen_id_problem_dict(all_problems)
    # print(problem_dict[1])

    # sys.exit(0)
    with open('分组刷题_算法.md', 'w') as f:
        # f.write('# problems\n')
        # for h2 in ["分组刷题", "分组刷题_算法", "探索初级算法", "探索中级算法"][:2]:
        for h2 in ["分组刷题_算法"]:
            f.write('# 分组刷题-算法\n')
            for h3 in sorted(res[h2]):
                h3_content = res[h2][h3]
                f.write(f'## {h3}\n')
                if isinstance(h3_content, dict):
                    for h4, h4_content in res[h2][h3].items():
                        h4 = del_prefix_num(h4)
                        f.write(f'### {h4}\n')
                        for pid, title, path in sorted(h4_content, key=lambda x: x[0]):
                            solution = []
                            with open(path, 'r') as fs:
                                for line in fs:
                                    if line.strip():
                                        solution.append(line.rstrip())
                            solution = "\n".join(solution)
                            f.write(f'#### {pid}.{title}\n')
                            content = problem_dict.get(pid, "")
                            if content:
                                content = content.split('\n')
                                content = content[1:]
                                content[1] = "####" + content[1]
                                content = '\n'.join(content)
                            f.write(f'{content}\n')
                            f.write(f'''##### solution
```python
{solution}
```
>
''')
                else:
                    for pid, title, path in sorted(h3_content, key=lambda x: x[0]):
                        solution = []
                        with open(path, 'r') as fs:
                            for line in fs:
                                if line.strip():
                                    solution.append(line.rstrip())
                        solution = "\n".join(solution)
                        f.write(f'#### {pid}.{title}\n')
                        content = problem_dict.get(pid, "")
                        if content:
                            content = content.split('\n')
                            content = content[1:]
                            content[1] = "###" + content[1]
                            content = '\n'.join(content)
                        f.write(f'{content}\n')
                        f.write(f'''##### solution
```python
{solution}
```
>
''')



