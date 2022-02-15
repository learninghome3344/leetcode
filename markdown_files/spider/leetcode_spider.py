#-*-coding:GBK -*-
import os
import requests, json
import re

# ��ȡ��Ŀ�ķ�����������Ĳ��ͣ����������һЩ�޸������õط��ϸ�����Ҫ��
# https://wanakiki.github.io/2020/leetcode-spider/
Remove = ["</?p>", "</?ul>", "</?ol>", "</li>", "</sup>"]
Replace = [["&nbsp;", " "], ["&quot;", '"'], ["&lt;", "<"], ["&gt;", ">"],
           ["&le;", "��"], ["&ge;", "��"], ["<sup>", "^"], ["&#39", "'"],
           ["&times;", "x"], ["&ldquo;", "��"], ["&rdquo;", "��"],
           [" *<strong> *", " **"], [" *</strong> *", "** "],
           [" *<code> *", " `"], [" *</code> *", "` "], ["<pre>", "```\n"],
           ["</pre>", "\n```\n"], ["<em> *</em>", ""], [" *<em> *", " *"],
           [" *</em> *", "* "], ["</?div.*?>", ""], ["	*</?li>", "- "]]


def convert(src):
    if not src:
        return ""
    # pre�ڲ�Ԥ����
    def remove_label_in_pre(matched):
        tmp = matched.group()
        tmp = re.sub("<[^>p]*>", "", tmp)  # ��ƥ��>��p
        return tmp

    src = re.sub("<pre>[\s\S]*?</pre>", remove_label_in_pre,
                 src)  # ע��˴���̰��ƥ�䣬��Ϊ�����ж��ʾ��
    # ����ֱ��ɾ���ı�ǩ
    for curPattern in Remove:
        src = re.sub(curPattern, "", src)
    # ��Ҫ�滻���ݵı�ǩ
    for curPattern, curRepl in Replace:
        src = re.sub(curPattern, curRepl, src)
    return src


def get_today_name() -> str:
    """
        ��ȡ�����ÿ��һ��� slug
    """
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    session = requests.Session()
    url = "https://leetcode-cn.com/graphql"
    params = {
        'oprationName':
        "questionOfToday",
        'query':
        '''
        query questionOfToday {
            todayRecord {
                question {
                    questionFrontendId
                    questionTitleSlug
                    __typename
                }
                lastSubmission {
                    id
                    __typename
                }
                date
                userStatus
                __typename
            }
        }
        '''
    }
    json_data = json.dumps(params).encode('utf8')
    headers = {
        'User-Agent': user_agent,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Referer': 'https://leetcode-cn.com/problemset/all/'
    }
    resp = session.post(url, data=json_data, headers=headers, timeout=10)
    resp.encoding = 'utf8'
    content = resp.json()
    # ��Ŀ��ϸ��Ϣ
    # print(content)
    question = content['data']['todayRecord'][0]['question']
    return question['questionTitleSlug']


def get_today_url():
    return "https://leetcode-cn.com/problems/" + get_today_name


def get_all(slug: str) -> dict:
    """������Ŀ�� id ��ȡ��Ŀ�����֣����ݣ�����飬��ǩ������ json ��ʽ�� dict ����
    """
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
    session = requests.Session()
    url = "https://leetcode-cn.com/graphql"
    params = {
        'operationName':
        "getQuestionDetail",
        'variables': {
            'titleSlug': slug
        },
        'query':
        '''query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                questionFrontendId
                title
                titleSlug
                content
                translatedTitle
                translatedContent
                difficulty
                topicTags {
                    name
                    slug
                    translatedName
                    __typename
                }
                codeSnippets {
                    lang
                    langSlug
                    code
                    __typename
                }
                __typename
            }
        }'''
    }
    json_data = json.dumps(params).encode('utf8')
    headers = {
        'User-Agent': user_agent,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Referer': 'https://leetcode-cn.com/problems/' + slug
    }
    resp = session.post(url, data=json_data, headers=headers, timeout=10)
    resp.encoding = 'utf8'
    content = resp.json()
    # ��Ŀ��ϸ��Ϣ
    # print(content)
    question = content['data']['question']
    return question


def get_problem_content(slug: str) -> str:
    question = get_all(slug)
    res = convert(question['translatedContent'])
    # �����ĺ������ϱ�ǩ
    res += "\n \n**��ǩ**\n"
    tags = question['topicTags']
    for tag in tags:
        if tag['translatedName'] != None:
            tagName = tag['translatedName']
        else:
            tagName = tag['name']
        res += "`" + tagName + "` "

    return res + "\n"


def get_solution_by_lang(slug: str, lang: str) -> str:
    """
        ��ȡ������Ŀ�Ķ�Ӧ���Եĺ���

        ֧�ֵĲ�������

        C++ Java Python Python3 C C# JavaScript Ruby Swift Go Scala Kotlin
        Rust PHP TypeScript Racket
    """
    question = get_all(slug)
    # ��ȡ��Ӧ���Եĺ���
    codeSnippets = question['codeSnippets']
    for x in codeSnippets:
        if x['lang'] == lang:
            return x['code']


def gen_markdown(path, content, title, url):
    """ ���� markdown �ļ�
    """
    file = open(path, 'a', encoding="utf-8")
    markdowncontenct = """# {titlename}
[{Url}]({Url}) 
## ԭ��
{Content}

## 
```python

```
>
""".format(titlename=title, Url=url, Content=content)
    file.write(markdowncontenct)
    # print(path)
    file.close()


def gen_gofile(path: str, title: str, url: str, func: str) -> None:
    """ ���� solution_test.go �ļ�
    
    """
    file = open(path, 'a', encoding="utf-8")
    go_content = """package leetcode

import (
	"reflect"
	"testing"
)

// {0}
// {1}
{2}
func TestSolution(t *testing.T) {{
	testCases := []struct {{
		desc string
		want 
	}}{{
		{{
            want: ,
		}},
	}}
	for _, tC := range testCases {{
		t.Run(tC.desc, func(t *testing.T) {{
			get := 
			if !reflect.DeepEqual(tC.want,get){{
				t.Errorf("input: %+v get: %v\\n",tC,get)
			}}
		}})
	}}
}}
""".format(title.replace(" ", ""), url, func)
    file.write(go_content)
    print(path)
    file.close()


def gen_go_mod(path: str) -> None:
    """
        ���� go.mod �ļ�
    """
    file = open(path, 'a', encoding="utf-8")
    file.write("module leetcode\ngo 1.15")
    file.close()


def gen_files(url: str, file_name: str):
    """
        ���� url ���ɶ�Ӧ���ļ�

        �� url Ϊ��ʱ�Զ���ȡÿ��һ��
        �� url ��Ϊ��ʱ��ȡ��Ӧ����Ŀ
    """
    if url.startswith("https://leetcode-cn.com/problems/"):
        slug = url.replace("https://leetcode-cn.com/problems/", "",
                           1).strip('/')
    elif len(url) > 0:
        print(
            "Wrong URL ! Please Check\n.It should be like https://leetcode-cn.com/problems/evaluate-division/"
        )
    else:
        slug = get_today_name()
    url = "https://leetcode-cn.com/problems/" + slug
    question = get_all(slug=slug)
    title = question['questionFrontendId'] + '.' + question['translatedTitle']

    content = get_problem_content(slug)

    # func = get_solution_by_lang(slug, 'Go')
    content = re.sub(r'\n\n\n\n*', "\n", content)  # �滻��������з�

    base_dir = os.getcwd()
    # newfolder = os.path.join(base_dir,
    #                          title.replace(". ", ".").replace(" ", "-"))
    # if not os.path.exists(newfolder):
    #     os.makedirs(newfolder)
    #     print("create new folder ", newfolder)
    # else:
    #     print("already exist folder:", newfolder)

    # ���� markdown �ļ�
    filepath = os.path.join(base_dir, file_name)
    gen_markdown(filepath, content, title, url)

    """
    # ���� solution_test.go �ļ�
    filepath = os.path.join(base_dir, newfolder, "solution_test.go")
    gen_gofile(filepath, title, url, func)

    # ���� go.mod �ļ�
    filepath = os.path.join(base_dir, newfolder, "go.mod")
    gen_go_mod(filepath)
    """
    
    return


if __name__ == '__main__':
    # ֻ���޸���� url ����
    # ������Ŀ����Ϊ https://leetcode-cn.com/problems/evaluate-division/ ��ֱ��ȫ�����Ƽ���
    # �� url Ϊ�յ�ʱ����ȡÿ��һ��

    d = {}
    with open("id2slug.txt", "r") as f:
        for line in f:
            line = line.strip().split("\t")
            if not line:
                continue
            d[int(line[0])] = line[1]

    for id in range(1, 1+max(d.keys())):
        if id % 10 == 0:
            print(id)
        if (id-1) // 100 < 16:
            continue
        try:
            url = "https://leetcode-cn.com/problems/" + d[id]
            file_name = "leetcode_cn_" + str((id-1) // 100) + ".md"
            gen_files(url=url, file_name=file_name)
        except Exception as e:
            print(e)
            print("����"+ url)
            with open("error.txt", 'a') as f:
                f.write(url +"\n")