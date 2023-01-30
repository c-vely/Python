import logging

'''
if __name__ == '__main__':  # ---> 기본이 warninig 이상일 때 작동
    logger = logging.getLogger("main")
    # steam_handler = logging.FileHandler(
    #     "my.log", mode="a", encoding="utf8")
    # logger.addHandler(steam_handler)

    logger.debug("틀렸어")
    logger.info("확인행!!")
    logger.warning("조심해")
    logger.error("에러났어!")
    logger.critical("망했어")

'''
    
    
'''
if __name__ == '__main__':
    logger = logging.getLogger("main")
    logging.basicConfig(level=logging.DEBUG)  # ---> 요렇게 기본 셋팅을 하고
    logger.setLevel(logging.ERROR)  # ---> 범위을 지정해 주면 됨
    
    logger.debug("틀렸어")
    logger.info("확인행!!")
    logger.warning("조심해")
    logger.error("에러났어!")
    logger.critical("망했어")

'''


 
if __name__ == '__main__':
    logger = logging.getLogger("main")
    logging.basicConfig(level=logging.DEBUG)
    logger.setLevel(logging.ERROR)
    
    # 보통 핸들러 등록해서 사용
    steam_handler = logging.FileHandler(
        "my.log", mode="a", encoding="utf8")  # ---> my.log 파일에 출력
    logger.addHandler(steam_handler)

    logger.debug("틀렸어")
    logger.info("확인행!!")
    logger.warning("조심해")
    logger.error("에러났어!")
    logger.critical("망했어")