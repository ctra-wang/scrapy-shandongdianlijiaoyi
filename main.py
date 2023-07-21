# This is a sample Python script.
import json

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests


def print_hi(pagenum):
    headers = {"Content-Type": "application/json"}
    header = {
        "Accept": "application/json, text/plain, */*",
        # "Host": "pmos.sd.sgcc.com.cn",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    }
    # https://pmos.sd.sgcc.com.cn/px-settlement-infpubquery/ipDisclosureApply/getLatest
    url = "https://pmos.sd.sgcc.com.cn/px-settlement-infpubquery/ipDisclosureApply/getHot"
    url = "https://pmos.sd.sgcc.com.cn/px-settlement-infpubquery/ipDisclosureApply/getLatest"

    # [57-61]
    payload = {"pageInfo": {"pageNum": pagenum, "pageSize": 10}, "data": {"marketId": "PHBSD"}}
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    json_data = json.loads(response.text)

    # print(json_data)

    for item in json_data["data"]["list"]:
        if "工作日报" in item["title"]:
            # count += count
            # print(item["attachment"].split(",")[0].split(":")[1])
            id = item["attachment"].split(",")[0].split(":")[1]
            print("-------------")
            print(id.replace("\"", ""))
            url = "https://pmos.sd.sgcc.com.cn/px-settlement-infpubmeex/fileService/preview?fileId=" + id.replace(
                "\"",
                "") + "#toolbar=0"
            response = requests.get(url)
            with open(item["title"] + ".pdf", "wb") as f:
                f.write(response.content)

    # response = requests.post(url, data=payload)
    # # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # url = "https://pmos.sd.sgcc.com.cn/px-settlement-infpubmeex/fileService/preview?fileId=n83ef4c4426814d2abf886e277c2a9bdc#toolbar=0"
    # response = requests.get(url)
    #
    # with open("example.pdf", "wb") as f:
    #     f.write(response.content)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(62, 64):
        print("当前i为：" + str(i))
        print_hi(i)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
