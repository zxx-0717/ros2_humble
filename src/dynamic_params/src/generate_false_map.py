

def generate_false_map(src):
        dst = []
        max_val = 255.0
        map = [[0,0,0,114],[0,0,1,185],[1,0,0,114],[ 1,0,1,174],[0,1,0,114],[ 0,1,1,185],[1,1,0,114], [1,1,1,0]]
        sum = 0
        for i in range(8):
                sum += map[i][3]
        weights = [0 for x in range(8)]
        cumsum = [0 for x in range(8)]
        for i in range(7):
                weights[i] = sum / map[i][3]
                cumsum[i+1] = cumsum[i] + map[i][3] / sum
        height_ = src.shape[0]
        width_ = src.shape[1]

        for v in range(height_):
                for u in range(width_):
                        val = min(max(src[v][u], 0.0), 1.0)
                        i = 0
                        for i in range(7):
                                if val < cumsum[i + 1]:
                                        break
                        w = 1.0 - (val - cumsum[i]) * weights[i]
                        r = int((w * map[i][0] + (1.0 - w) * map[i + 1][0]) * 255.0)
                        g = int((w * map[i][1] + (1.0 - w) * map[i + 1][1]) * 255.0)
                        b = int((w * map[i][2] + (1.0 - w) * map[i + 1][2]) * 255.0)

                        dst.append([b, g, r])

        return dst
