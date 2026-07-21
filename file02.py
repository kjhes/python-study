# log.txt에서 INFO/WARNING/ERROR 개수 분석

#f = open("log.txt", "r") 
with open("log.txt", "r") as f:

    info_count = 0
    warning_count = 0
    error_count = 0

    print("[로그 내용]")

    for line in f:
        clean_line = line.strip()
        print(clean_line)

        if "INFO" in clean_line:
            info_count += 1
        elif "WARNING" in clean_line:
            warning_count += 1
        elif "ERROR" in clean_line:
            error_count += 1

#f.close()

print("\n[요약 결과]")
print("INFO 개수:", info_count)
print("WARNING 개수:", warning_count)
print("ERROR 개수:", error_count)