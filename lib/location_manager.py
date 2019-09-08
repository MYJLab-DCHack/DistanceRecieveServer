import numpy as np
import math

class LocationManager():
    def __init__(self):
        self.data = [
       {
           "name": "bori",
           "distance": math.sqrt(20),
           "x": 0.0,
           "y":9.0
           },
       {
           "name": "saka",
           "distance": math.sqrt(17),
           "x": 1.0,
           "y": 1.0
           },
       {
           "name": "marutaku",
           "distance": math.sqrt(13),
           "x": 4.0,
           "y": 2.0 },
       {
           "name": "sho",
           "distance": math.sqrt(20),
           "x": 6.0,
           "y": 7.0
           }
       ]

    def setup(self):
        np.set_printoptions(threshold=np.inf)
        np.set_printoptions(linewidth=200)

    def getLocation(self, devide_unit, width):
        if len(self.data) == 0:
            return None
        elif len(self.data) == 1:
            return self.data[0]["x"], self.data[0]["y"]
        elif len(self.data) == 2:
            x_mid = (self.data[0]["x"] + self.data[1]["x"]) / 2
            y_mid = (self.data[0]["y"] + self.data[1]["y"]) / 2
            return x_mid, y_mid

        xs = [user["x"] for user in self.data]
        ys = [user["y"] for user in self.data]
        x_min = min(xs)
        x_max = max(xs)
        y_min = min(ys)
        y_max = max(ys)
    
        mesh = np.zeros((math.ceil((y_max - y_min) / devide_unit), math.ceil((x_max - x_min) / devide_unit)))
        for user in self.data:
            mapdata = []
            for i in np.arange(y_min, y_max, devide_unit):
                row = []
                for j in np.arange(x_min, x_max, devide_unit):
                    if abs((j-user["x"])**2 + (i-user["y"])**2 - user["distance"]**2) < width:
                        row.append(1)
                    else: 
                        row.append(0)
                mapdata.append(row)
            tmp_mesh = np.array(mapdata)
            mesh += tmp_mesh
        xax = [i + x_min for i in np.arange(x_min, x_max, devide_unit)]
        yax = [0] + [i + y_min for i in np.arange(y_min, y_max, devide_unit)]
        xaxis = np.zeros((1, len(xax)))
        yaxis = np.zeros((1, len(yax)))
        xaxis[:] = xax
        yaxis[:] = yax
        del xax, yax
        xmesh = np.vstack((xaxis, mesh))
        xymesh = np.hstack((yaxis.T, xmesh))
        print(xymesh)
        loc = np.unravel_index(np.argmax(mesh), mesh.shape)
        return loc[1] * devide_unit + x_min, loc[0] * devide_unit + y_min
    def calc_center(self):
        center_x = 0
        center_y = 0
        for data in self.data:
            center_x += data["x"]
            center_y += data["y"]
        return center_x / len(self.data), center_y / len(self.data)
    def update_distance(self, user_id, distance):
        for data in self.data:
            if data["name"] == user_id:
                data["distance"] = distance



if __name__ == '__main__':
    manager = LocationManager()
    # メッシュの細かさ、1なら整数
    devide_unit = 0.2
    # 誤差の想定大きくなればなるほどアバウトになる
    # 1 ~ 5とかで試す
    width = 1
    x, y = manager.getLocation(devide_unit, width)
    print("現在地は {}, {} です".format(x, y))
    center_x, center_y = manager.calc_center()
    print(f"中心は {x}, {y} です")
    manager.update_distance('marutaku', 10)
    manager.update_distance('sho', 1)
    manager.update_distance('bori', 4)
    x, y = manager.getLocation(devide_unit, width)
    print(manager.data[2])
    print("現在地は {}, {} です".format(x, y))
    center_x, center_y = manager.calc_center()
    print(f"中心は {x}, {y} です")
