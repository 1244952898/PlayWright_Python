import schedule as schedule


def jb():
    print("测试")
schedule.every(3).seconds.do(jb)
schedule.run_pending()

jb()