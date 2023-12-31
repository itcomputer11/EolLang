import logger
import compute

def FileRun(dir):
    if not dir.lower().endswith(".eol"):
        logger.printError("0% 완료")
        return "0% 완료"
    
    logger.printInfo(f'\"{dir}\" 가 실행되었습니다.')
    
    code_list = []
    
    with open(dir, "r", encoding='UTF8') as f: # 
        for line in f: code_list.append(line.strip())
    
    Run(code_list)

def Run(code):
    code_list = []
    counter = 0
    accepted_list = list("나는.,빠름느림토끼달팽이느슨엄격춤춤망겜이라는게임을해 ")
    print_text = ""
    pointer = 0
    
    for line in code.split("\n"): code_list.append(line.strip())
    
    for line in code_list:
        counter+=1
        
        for com in list(line): # 알맞지 않은 문자가 들어가 있을 경우
            if com not in accepted_list:
                logger.printError("과부하!")
                return "과부하!"
        
        if counter == 1 and line != "나는": # 오류 처리
            logger.printError("0% 완료")
            return "0% 완료"
        elif counter == len(code_list):
            if line == "이라는 게임을 해":
                logger.printing(print_text)
                logger.printInfo("축하합니다!")
                return f"{print_text}\n[info] 축하합니다!"
            else:
                logger.printError("99% 완료")
                return "99% 완료"
        
        if line == "": continue 

        try:
            if line.endswith("춤"):
                print_text += str(compute.lineToInteger(line[:-1]))
        
            if line.endswith("춤망겜"):
                print_text += chr(int(compute.lineToInteger(str(line[:-3])))) # 유니코드 변환
            
            if line == "불":
                pointer+=1
            
            if line == "얼":
                pointer-=1
            
            if line == "행성":
                logger.printing(pointer)
        except:
            logger.printError(f"{int(98 / counter)}% 완료")
            return f"{int(98 / counter)}% 완료"