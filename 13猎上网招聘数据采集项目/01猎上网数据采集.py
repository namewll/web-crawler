import requests
from openpyxl import load_workbook
import time
import random
from concurrent.futures import ThreadPoolExecutor

wb = load_workbook('./米聘推荐平台数据库.xlsx')
ws = wb.active

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "HOSPAN": "70672a63b9774a74b7b69a81e1dcc78e;9fb3276d7226465397ab05bff5e939e3",
    "Referer": "https://hh.hunteron.com/greatPosition.html",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Chromium\";v=\"146\", \"Not-A.Brand\";v=\"24\", \"Microsoft Edge\";v=\"146\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "_c_WBKFRo": "oJDNvJK8lxWmRAvHhU0VAZjCVxaFX5ZqrnDwNevO",
    "hh_userid": "228599",
    "Hm_lvt_dcc6428c06d1b43f81c07b3ac6a94336": "1774068740,1774232181,1774241893,1774261859",
    "HMACCOUNT": "67A7773FF32FE2A7",
    "registrationReferrer": "https://hh.hunteron.com/positions.html",
    "token": "a05639097d0448609e14f34051351aff",
    "Hm_lpvt_dcc6428c06d1b43f81c07b3ac6a94336": "1774261939"
}

# 把两个接口地址分开定义，避免覆盖
LIST_URL = "https://hh.hunteron.com/api/v5/q/position/platform"
DETAIL_URL = "https://hh.hunteron.com/api/v5/position/positionDetail"


def parse(item):
    gx_time=item['refreshTime']
    fb_time=item['publishTime']
    gs=item['enterpriseName']
    gs_scale=item['enterpriseScaleDesc']
    zw_type=item['positionType']
    fk_time=item['recommendFeedbackTime']
    zw_id=item['positionId']
    gs_logo=item['enterpriseLogo']
    try:
        item_id = item['positionId']
        detail_params = {
            "positionId": f"{item_id}",
            "_": f"{int(time.time() * 1000)}"
        }
        url = "https://hh.hunteron.com/api/v5/position/positionDetailAttach"
        res1 = session.get(url, headers=headers, cookies=cookies, params=detail_params)
        url = "https://hh.hunteron.com/api/v1/enterprise/detail/getById"
        params = {
            "enterpriseId": "80190",
            "_": "1774261938861"
        }
        res2 = requests.get(url, headers=headers, cookies=cookies, params=params)
        hy_name=','.join(res2.json()['data']['industryDictNames'])
        lx_people=res1.json()['data']['spaViews'][0]['mobilePhone']
        lx_phone=res1.json()['data']['spaViews'][0]['userName']
        yx_time='有效期：>3个月'
        time.sleep(random.uniform(1, 3))
        res = session.get(DETAIL_URL, params=detail_params, timeout=10)
        res.raise_for_status()
        data = res.json()
        fz_state = f"{item['developStageDesc']} {data['data']['coCreationVO']['enterpriseVO']['developPlate']}"
        job_name = data['data']['positionTitle']
        salary = data['data']['annualSalaryDesc']
        hight = data['data']['maxBaseAnnualSalary']
        low = data['data']['minShowAnnualSalary']
        gd_salary = data['data']['fixedRewardAmount']
        sf_mimi=data['data']['isPrivate']
        nl_need=data['data']['ageRequired']
        dh_text=data['data']['degreeRequiredStr']+"\n"+data['data']['openReasonStr']+"\n"+data['data']['functionStr']
        zy_thing=data['data']['coCreationVO']['enterpriseVO']['mainManagement']
        yj_type=data['data']['rewardExplainContent']['groups'][0]['items'][0]['commissionRoleType']
        sf_need_people=data['data']['ifRecruitPosition']
        chch=data['data']['coCreationVO']['reCheckRepeat']
        fz_what=data['data']['positionAssignName']
        gz_xingzhi=data['data']['coCreationVO']['enterpriseVO']['styleNew']
        tj_rate=data['data']['latestPositionRewardInfo']['commissionPaRate']
        RPO_zhiw=data['data']['positionClientType']
        ACN_zhiw=data['data']['acnPositionStatistics']['positionId']
        lb_AI=''
        for i in data['data']['aiList']:
            for j in i['conditions']:
                lb_AI+=(j['conditionKey']+':'+j['conditionValue']+'\n')
        chg_zhq=data['data']['payWay']
        place = data['data']['positionSurveyView']['positionSurveyBaseBean']['interviewAddress']

        head_count = data['data']['headCount']
        degreeRequired = data['data']['positionExtraItem']['degreeRequired']
        worYearRequired = data['data']['positionExtraItem']['worYearRequired']
        rewardExplainContent = ''.join(
            data['data']['rewardExplainContent']['groups'][0]['items'][0]['frontShowStr'].split(' ')[1:])
        lightspotCompany = data['data']['coCreationVO']['lightspotCompany']
        lightspotData = data['data']['coCreationVO']['lightspotData']
        openTime = data['data']['coCreationVO']['openTime']
        workAddress = data['data']['locations'][0]['workCityName'] + data['data']['locations'][0]['workAddress']
        bestPortrait = data['data']['coCreationVO']['bestPortrait']
        secondPortrait = data['data']['coCreationVO']['secondPortrait']
        rejectPortrait = data['data']['coCreationVO']['rejectPortrait']
        softDiathetic = data['data']['coCreationVO']['softDiathetic']
        manage =data['data']['coCreationVO']['functionTypeDescription']
        if data['data']['coCreationVO']['functionTypeDescription']=='1':
            manage='否'
        annualSalaryDesc = data['data']['annualSalaryDesc']

        salarymake = f"税前年薪:{data['data']['annualSalaryDesc']},薪资构成:{data['data']['positionSurveyView']['positionSurveyBaseBean']['salaryRuleConstitute']},社保福利:{data['data']['positionSurveyView']['positionSurveyBaseBean']['socialSecurityBenefits']},假期福利:{data['data']['positionSurveyView']['positionSurveyBaseBean']['holidayBenefits']},住房福利:{data['data']['positionSurveyView']['positionSurveyBaseBean']['housingBenefits']},通信交通:{data['data']['positionSurveyView']['positionSurveyBaseBean']['phoneTrafficBenefits']}"
        interviewRotationNum = data['data']['positionSurveyView']['positionSurveyBaseBean']['interviewRotationNum']
        interview_process = ''
        for i in data['data']['positionSurveyView']['positionSurveyBaseBean']['interviewProcessJson']:
            interview_process += (i['interviewRotationNum'] + i['interviewer'] + i['interviewValue'])
        ifOtherPlace = data['data']['positionSurveyView']['positionSurveyBaseBean']['ifOtherPlace']
        if ifOtherPlace==1:
            ifOtherPlace='是'
        if ifOtherPlace==0:
            ifOtherPlace='否'
        reimbursementProcess = data['data']['positionSurveyView']['positionSurveyBaseBean']['reimbursementProcess']
        jobzhize = data['data']['jobDescription']+","+data['data']['jobRequirement']
        oneComment = data['data']['coCreationVO']['enterpriseVO']['oneComment']
        to_Industry = data['data']['positionIndustry']
        company_defile_infor = data['data']['coCreationVO']['enterpriseVO']['info']
        website = data['data']['coCreationVO']['enterpriseVO']['website']
        styleNew = data['data']['coCreationVO']['enterpriseVO']['styleNew']
        establishYear = data['data']['coCreationVO']['enterpriseVO']['establishYear']
        jiesuan_styple = data['data']['payWay']
        jiesuan_node = data['data']['payNode']
        if jiesuan_node==2:
            jiesuan_node='过保结算'
        fen_rate = ''
        for i in data['data']['rewardExplainContent']['groups']:
            fen_rate += i['title']
            for j in i['items']:
                fen_rate += j['frontShowStr']
        reportTo_person = data['data']['reportTo']

        content.append(
            [dh_text, job_name, place, hy_name,job_name, company_defile_infor, company_defile_infor, rewardExplainContent,
             low, hight, reportTo_person, jobzhize, styleNew, fz_what, yj_type, fen_rate, tj_rate, gd_salary, sf_mimi, sf_need_people, openTime, gz_xingzhi,
             word1, chch, gs_logo, company_defile_infor, company_defile_infor, styleNew, gs_scale, website, salarymake, place,
             worYearRequired, degreeRequired, head_count, nl_need, fb_time, lx_people, lx_phone, yx_time, fk_time, fb_time, gx_time, lightspotCompany, lightspotData,
             openTime, bestPortrait, secondPortrait, rejectPortrait, softDiathetic, manage, place,
             interviewRotationNum, interview_process, ifOtherPlace, reimbursementProcess, establishYear, fz_state, zy_thing,
             jiesuan_node, jiesuan_styple, chg_zhq, yj_type, fen_rate, RPO_zhiw, ACN_zhiw, lb_AI, zw_id])
        print(f"成功抓取职位：{job_name}")
    except Exception as e:
        print(f"抓取职位详情失败：{e}")
    time.sleep(random.uniform(3, 5))


if __name__ == '__main__':
    word1 = input('请输入搜索关键字：')
    content = []

    for page in range(1, 3):
        session = requests.Session()
        session.headers.update(headers)
        session.cookies.update(cookies)

        list_params = {
            "type": "1",
            "pageNo": f"{page}",
            "pageSize": "20",
            "keyword": f"{word1}",
            "boostId": f"{word1}",
            "boostType": "1",
            "conditionLine": f"搜索关键词：{word1}；",
            "source": "positionChannel",
            "_": f"{int(time.time() * 1000)}"  # 每次都生成新时间戳
        }

        try:
            response = session.get(LIST_URL, params=list_params, timeout=3)
            response.raise_for_status()  # 主动抛出HTTP错误
            print(f"第{page}页列表请求状态码：{response.status_code}")
            items = response.json()['data']['list']
        except Exception as e:
            print(f"第{page}页列表请求失败：{e}")
            print(f"响应内容：{response.text[:300]}")
            continue
        with ThreadPoolExecutor(max_workers=5)as executor:
            executor.map(parse,items)

    for row in content:
        ws.append(row)
    wb.save(f'{word1}.xlsx')
    print("✅ 全部抓取完成！")