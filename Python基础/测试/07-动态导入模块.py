import importlib
import sys


def main():
    print("sys path=" + str(sys.path))

    # 特别注意，动态导入一个模块前要确保在环境变量中能找到该模块。
    # 需要将需要导入的模块路径动态加入到系统环境变量中，
    # 这种导入是临时导入，并不会真的添加到系统环境变量中，程序结束就会还原
    sys.path.append("../../common")
    print("sys path=" + str(sys.path))
    # __import__的使用，python内部使用
    ship1 = __import__("ship")
    shipa = ship1.Ship("bigFish", 12, 30)
    shipa.msg()

    # 使用importlib模块的import_module("")来动态导入，官方推荐
    ship2 = importlib.import_module("ship")
    shipb = ship2.Ship("smallFish", 123, 39)
    shipb.msg()

    # 动态导入和setattr结合使用给shipb对象动态添加属性或方法
    if not hasattr(shipb, "run"):
        print("shipb has not the run method")
        setattr(shipb, "run", run)
        shipb.run(shipb.name)


def run(name):
    print(name+"run normal")


if __name__ == "__main__":
    main()
