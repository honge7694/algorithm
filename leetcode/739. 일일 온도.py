def dailyTemperatures(temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # result = []
        # for i in range(len(temperatures)):
        #     count = 0
        #     for j in range(i+1, len(temperatures)+1):
        #         count += 1
        #         if j == len(temperatures):
        #             result.append(0)
        #             break
        #         elif temperatures[i] < temperatures[j]:
        #             result.append(count)
        #             break
        # return result

        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)

        return result
        # result = [0] * len(temperatures)  # 결과 리스트를 0으로 초기화
        # stack = []  # 온도를 저장할 스택

        # for i in range(len(temperatures)):
        #     # 스택이 비어있지 않고 현재 온도가 스택의 가장 위에 있는 온도보다 높다면
        #     while stack and temperatures[i] > temperatures[stack[-1]]:
        #         j = stack.pop()  # 스택에서 온도 인덱스를 꺼내서
        #         result[j] = i - j # 결과를 업데이트
        #     stack.append(i) # 현재 온도 인덱스를 스택에 추가

temperatures = [73,74,75,71,69,72,76,73]
temperatures2 = [30,40,50,60]
print(dailyTemperatures(temperatures))