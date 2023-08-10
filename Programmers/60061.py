# 구조물이 제대로 설치되어 있는지 확인하는 함수
def check_wall(structure):
    for x, y, a in structure:
        # 기둥일 경우
        if a == 0:
            # 바닥에 있는 경우
            if y == 0:
                continue
            # 보의 한쪽 끝 부분 위에 있는 경우
            elif [x - 1, y, 1] in structure or [x, y, 1] in structure:
                continue
            # 다른 기둥 위에 있는 경우 
            elif [x, y - 1, 0] in structure:
                continue
            else:
                return False

        # 보일 경우 
        if a == 1:
            # 한쪽 끝 부분이 기둥 위에 있는 경우 
            if [x, y - 1, 0] in structure or [x + 1, y - 1, 0] in structure:
                continue
            # 양쪽 끝 부분이 다른 보와 동시에 연결되어 있는 경우 
            elif [x - 1, y, 1] in structure and [x + 1, y, 1] in structure:
                continue
            else:
                return False

    return True


def solution(n, build_frame):
    structure = []

    for frame in build_frame:
        x, y, a, b = frame
        # 삭제하는 경우 
        if b == 0:
            # 우선 삭제하고
            structure.remove([x, y, a])
            # 구조물이 조건에 맞지 않는다면
            if not check_wall(structure):
                # 다시 추가 
                structure.append([x, y, a])

        # 설치하는 경우 
        if b == 1:
            # 우선 추가하고
            structure.append([x, y, a])
            # 구조물이 조건에 맞지 않는다면
            if not check_wall(structure):
                # 다시 삭제
                structure.remove([x, y, a])

    structure.sort()
    return structure
